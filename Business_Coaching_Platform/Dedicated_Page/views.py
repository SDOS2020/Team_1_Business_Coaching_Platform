from user.models import CustomUser
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from user.views import connection_exists, get_all_connections


class PostViewSet(viewsets.ViewSet):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, pk = None):
        """
        Get posts between the authenticated user and one of his/her connection (whose pk is specified)
        """
        other_user = get_object_or_404(CustomUser, pk = pk)
        if connection_exists(request.user, other_user):
            posts = get_posts_between_users(request.user, other_user)
            serializer = PostSerializer(posts, many = True)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        Creates a Post between authenticated user and one of his/her connection
        """
        other_user = get_object_or_404(CustomUser, pk = request.data['pk'])
        if connection_exists(request.user, other_user):
            post = Post.objects.create(creator = request.user, viewer = other_user, message = html.escape(request.data['content']))
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
        return Response([], status=status.HTTP_400_BAD_REQUEST)

        # if request.user.is_coach and request.user.coach.id == request.data['coach']['id'] and post_pk:
        #     post = Post.objects.get_object_or_404(pk = post_pk, coach = request.user.coach)
        #     post.title = request.data['title']
        #     post.content = request.data['content']
        #     post.save()
        #     serializer = PostSerializer(post)
        #     return Response(serializer.data)
        # elif request.user.is_coachee and request.user.coachee.id == request.data['coachee']['id'] and post_pk:
        #     post = Post.objects.get_object_or_404(pk=post_pk, coach=request.user.coach)
        #     post.title = request.data['title']
        #     post.content = request.data['content']
        #     post.save()
        #     serializer = PostSerializer(post)
        #     return Response(serializer.data)
        # return Response([], status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk = None):
        """
        Deletes the Post having primary key as post_pk
        """
        if post_pk and request.user.id == request.data['creator']['id']:
            post = Post.objects.get_object_or_404(pk = post_pk, creator = request.user)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            serializer = PostSerializer(post)
        return Response([], status=status.HTTP_400_BAD_REQUEST)


def get_posts_between_users(user1, user2):
    """
    Returns all post objects between 2 users sorted by date posted.
    Note: It does not check if they are a connection
    """
    return Post.objects.filter(Q(creator = user1, viewer = user2) | Q(creator = user2, viewer = user1)).order_by('-date_posted')