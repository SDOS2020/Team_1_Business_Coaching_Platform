from django.conf import settings
from user.models import CustomUser,Connection,Coach,Coachee
from .models import Post
from user.serializer import ConnectionSerializer
from .serializer import PostSerializer, UploadSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from user.views import connection_exists, get_all_connections, get_connection
from django.db.models import Q
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from .forms import customForm
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
import os


import html

# Create your views here.
# @requested_user_is_coach_or_connection
@login_required
def dedicated_page(request,pk):
    other_user = get_object_or_404(CustomUser, pk=pk)
    current_connection = get_connection(request.user, other_user)
    if current_connection:
        return render(request, 'dedicated_page/dedicated_page.html',{"con":other_user,"link":current_connection})#replace con with connection
    return redirect('home')


class PostViewSet(viewsets.ViewSet):
    """
        A viewset for viewing and editing post instances.
    """
    http_method_names = ['get', 'post', 'head','put','retrieve','delete']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    @action(detail='True',methods=['post'])
    def create_post(self, request):
        """
        Creates a Post between authenticated user and one of his/her connection
        """
        if request.method == 'POST':
            form = customForm(request.POST)
            if form.is_valid():
                other_user = get_object_or_404(CustomUser, pk=form.cleaned_data['pk'])
                if connection_exists(request.user, other_user):
                    post = Post.objects.create(creator=request.user, viewer=other_user,
                                               content=html.escape(form.cleaned_data['content']))
                    uploaded_file = request.FILES['file'] if 'file' in request.FILES else None
                    if uploaded_file:
                        fs = FileSystemStorage()
                        uploaded_file_name = fs.save(uploaded_file.name, uploaded_file)
                        uploaded_file_url = fs.url(uploaded_file_name)
                        post.uploaded_file_url = uploaded_file_url
                        post.uploaded_file_name = uploaded_file_name
                    post.save()
                    serializer = PostSerializer(post)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response([], status=status.HTTP_400_BAD_REQUEST)

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

    def delete(self, request):
        """
        Deletes the Post having primary key as post_pk
        """
        post_pk = request.data['post_pk']
        if post_pk:
            post = get_object_or_404(Post,pk=post_pk)
            if request.user.id == post.creator.id:
                post.delete()
                # file_name = post.uploaded_file_name
                # if file_name:
                #     fs = FileSystemStorage()
                #     file_path = os.path.join(settings.MEDIA_ROOT,file_name)
                #     fs.delete(file_path)
                serializer = PostSerializer(post)
                return Response(serializer.data)
        return Response([], status=status.HTTP_400_BAD_REQUEST)


# ViewSets define the view behavior.
class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)



def get_posts_between_users(user1, user2):
    """
    Returns all post objects between 2 users sorted by date posted.
    Note: It does not check if they are a connection
    """
    return Post.objects.filter(Q(creator = user1, viewer = user2) | Q(creator = user2, viewer = user1)).order_by('-date_posted')