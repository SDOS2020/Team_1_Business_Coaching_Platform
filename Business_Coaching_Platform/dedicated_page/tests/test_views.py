from django.test import TestCase
from dedicated_page.models import Post
from user.models import CustomUser,Connection,Coach,Coachee # Required to assign User as a borrower
from django.urls import reverse

# Create your tests here.
class PostViewsTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = CustomUser.objects.create(age=50,is_coach = True,email="raghav@gmail.com")
        test_user1.set_password('1X<ISRUkw+tuK')
        test_user2 =  CustomUser.objects.create(age=27,is_coachee = True,email="paras@gmail.com")
        test_user2.set_password('2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()
        post = Post.objects.create(creator= test_user1,viewer = test_user2,content = "Hello world!")
        post.save()
        # creator = CustomUser.objects.create(age=50,is_coach = True,email="raghav@gmail.com")
        # viewer = CustomUser.objects.create(age=27,is_coach = True,email="paras@gmail.com")
        # print(CustomUser.objects.all())
        # # viewer = CustomUser.objects.all()[1]
        # post = Post.objects.create(creator= creator,viewer = viewer,content = "Hello world!")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_basic(self):
        self.assertEqual(1,int(1))

    def test_connected_users_cannot_access_dedicated_page(self):
        test_user1 = CustomUser.objects.filter(email="raghav@gmail.com").first()
        test_user2 = CustomUser.objects.filter(email="paras@gmail.com").first()
        test_coach = Coach.objects.create(user=test_user1,first_name='Raghav',last_name='Arora',description='experienced')
        test_coachee = Coachee.objects.create(user=test_user2,first_name='Paras',last_name='Mehrotra')
        login = self.client.login(email='raghav@gmail.com', password='1X<ISRUkw+tuK')
        self.assertTrue(login)
        response1 = self.client.get(reverse('login'))
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get(f'/dedicated_page/{test_user2.pk}',follow=True)
        self.assertTemplateUsed(response2,'home/home.html')

    def test_connected_users_can_access_dedicated_page(self):
        test_user1 = CustomUser.objects.filter(email="raghav@gmail.com").first()
        test_user2 = CustomUser.objects.filter(email="paras@gmail.com").first()
        test_coach = Coach.objects.create(user=test_user1, first_name='Raghav', last_name='Arora',
                                          description='experienced')
        test_coachee = Coachee.objects.create(user=test_user2, first_name='Paras', last_name='Mehrotra')
        login = self.client.login(email='raghav@gmail.com', password='1X<ISRUkw+tuK')
        self.assertTrue(login)
        response1 = self.client.get(reverse('login'))
        self.assertEqual(response1.status_code, 200)

        connection = Connection.objects.create(coach=test_coach,coachee= test_coachee,accepted =True)
        connection.save()
        response2 = self.client.get(f'/dedicated_page/{test_user2.pk}', follow=True)
        self.assertTemplateUsed(response2, 'dedicated_page/dedicated_page.html')

        # print("rs1", response2.redirect_chain)


        # self.assertTemplateUsed(response, 'dashboard/coach_dashboard.html')

        # self.assertTemplateUsed(response, 'dashboard/coach_dashboard.html')
        # # Check our user is logged in
        # self.assertEqual(str(response.context['user']), 'testuser1')
        # # Check that we got a response "success"
        # self.assertEqual(response.status_code, 200)
        #
        # # Check we used correct template
        # self.assertTemplateUsed(response, 'catalog/bookinstance_list_borrowed_user.html')

    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get('/dedicated_page/authors/')
    #     self.assertEqual(response.status_code, 200)