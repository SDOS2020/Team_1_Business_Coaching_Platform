from user.models import CustomUser
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ViewSet):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = CustomUser.objects.get_object_or_404(pk = request.data['pk'])
        if user.is_coach and request.user.is_coachee and \
                (Connection.objects.filter(coach = user.coach, coachee = request.user.coachee, accepted = True).exists()):
            posts = Post.objects.filter(coach_id=request.user.coach.id,coachee = request.user.coachee)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        elif user.is_coachee and request.user.is_coach and \
             (Connection.objects.filter(coach=request.user.coach, coachee=user.coachee, accepted=True).exists()):
            posts = Post.objects.filter(coachee_id=request.user.coachee.id,coach = request.user.coach)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        return Response([], status=status.HTTP_400_BAD_REQUEST)


    def create(self, request):
        user = CustomUser.objects.get_object_or_404(pk = request.data['pk'])
        if user.is_coach and request.user.is_coachee and \
                (Connection.objects.filter(coach = user.coach, coachee = request.user.coachee, accepted = True).exists()):
            post = Post.objects.create(coach = user.coach, coachee = request.user.coachee)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()#for the last 2 lines
            serializer = PostSerializer(post)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        elif  user.is_coachee and request.user.is_coach and \
                (Connection.objects.filter(coach = request.user.coach, coachee = user.coachee, accepted = True).exists()):
            post = Post.objects.create(coach = request.user.coach, coachee = user.coachee)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response([], status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, post_pk = None):
        if request.user.is_coach and request.user.coach.id == request.data['coach']['id'] and post_pk:
            post = Post.objects.get_object_or_404(pk = post_pk, coach = request.user.coach)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.user.is_coachee and request.user.coachee.id == request.data['coachee']['id'] and post_pk:
            post = Post.objects.get_object_or_404(pk=post_pk, coach=request.user.coach)
            post.title = request.data['title']
            post.content = request.data['content']
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        if request.user.is_coach and request.user.coach.id == request.data['coach']['id'] and post_pk:
            post = Post.objects.get_object_or_404(pk=post_pk, coach=request.user.coach)
            post.delete()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.user.is_coachee and request.user.coachee.id == request.data['coachee']['id'] and post_pk:
            post = Post.objects.get_object_or_404(pk=post_pk, coach=request.user.coach)
            post.delete()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response([], status = status.HTTP_400_BAD_REQUEST)
