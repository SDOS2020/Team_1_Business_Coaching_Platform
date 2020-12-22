from django.test import TestCase
from dashboard.models import Chat
from user.models import CustomUser

# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        creator = CustomUser.objects.create(age=50,is_coach = True,email="raghav@gmail.com")
        viewer = CustomUser.objects.create(age=27,is_coachee = True,email="paras@gmail.com")
        print(CustomUser.objects.all())
        Chat.objects.create(sender = creator,receiver = viewer, message = "Hello world!")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_str(self):
        creator = CustomUser.objects.all()[0]
        viewer = CustomUser.objects.all()[1]
        content = "Hello world!"
        post = Chat.objects.all()[0]
        expected_object_name = f'{creator} -> {viewer} : {content}'
        self.assertEqual(expected_object_name, str(post))

