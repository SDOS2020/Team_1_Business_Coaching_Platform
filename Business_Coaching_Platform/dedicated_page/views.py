from user.models import CustomUser
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from user.views import connection_exists, get_all_connections
from django.db.models import Q
import html

# Create your views here.
@login_required
def dedicated_page(request,pk):
    print("Hi")
    other_user = get_object_or_404(CustomUser, pk=pk)
    if connection_exists(request.user, other_user):
        return render(request, 'dedicated_page/post_form.html',{"con":other_user})#change con with connection
    else:
        print("Doesn't exist")
    return redirect('dashboard')

@login_required
def create_post(request,pk):
    other_user = get_object_or_404(CustomUser, pk=pk)
    if connection_exists(request.user, other_user):
        return render(request, 'dedicated_page/post_form.html',{"con":other_user})#change con with connection
    return redirect('dashboard')

@login_required
def post_view(request):
    if request.user.is_coach:
        connections = Connection.objects.filter(coach = request.user.coach, accepted = True)
        return render(request, 'dedicated_page/chat.html', {'connections' : connections})
    elif request.user.is_coachee:
        connections = Connection.objects.filter(coachee = request.user.coachee, accepted = True)
        return render(request, 'dedicated_page/chat.html', {'connections' : connections})
    return redirect('home')


class PostViewSet(viewsets.ViewSet):
    """
        A viewset for viewing and editing post instances.
    """
    http_method_names = ['list','get', 'post', 'head','put','create','retrieve','delete']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Get posts between the authenticated user and one of his/her connection (whose pk is specified)
        """
        # print("HEllo")
        # connections = get_all_connections(request.user)
        # chats = [ChatSerializer(get_chats_between_users(connection.coach.user, connection.coachee.user), many = True).data for connection in connections]
        # return Response(chats)


        # connections = get_all_connections(request.user)
        # posts = [PostSerializer(get_posts_between_users(connection.coach.user, connection.coachee.user), many = True).data for connection in connections]
        # return Response(posts)
        other_user = get_object_or_404(CustomUser, pk = request.data['pk'])
        if connection_exists(request.user, other_user):
            posts = get_posts_between_users(request.user, other_user)
            serializer = PostSerializer(posts, many = True)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        Creates a Post between authenticated user and one of his/her connection
        """
        print("My pk is",request.user.pk)
        print("Hi, create me!")
        other_user = get_object_or_404(CustomUser, pk = request.data['pk'])
        if connection_exists(request.user, other_user):
            post = Post.objects.create(creator = request.user, viewer = other_user, content = html.escape(request.data['content']))
            serializer = PostSerializer(post)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response([], status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, post_pk = None):
        """
        Updates the Post having primary key as post_pk
        """
        if post_pk and request.user.id == request.data['creator']['id']:
            post = Post.objects.get_object_or_404(pk = post_pk, creator = request.user)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk = None):
        """
         Get posts between the authenticated user and one of his/her connection (whose pk is specified)
        """
        other_user = get_object_or_404(CustomUser, pk = pk)
        if connection_exists(request.user, other_user):
            posts = get_posts_between_users(request.user, other_user)
            serializer = PostSerializer(posts, many = True)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk = None):
        """
        Deletes the Post having primary key as post_pk
        """
        if post_pk and request.user.id == request.data['creator']['id']:
            post = Post.objects.get_object_or_404(pk = post_pk, creator = request.user)
            post.delete()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response([], status=status.HTTP_400_BAD_REQUEST)


def get_posts_between_users(user1, user2):
    """
    Returns all post objects between 2 users sorted by date posted.
    Note: It does not check if they are a connection
    """
    return Post.objects.filter(Q(creator = user1, viewer = user2) | Q(creator = user2, viewer = user1)).order_by('date_posted')