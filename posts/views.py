from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from accounts.models import Account, Follow
from rest_framework import pagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page'


class PostsView(generics.ListCreateAPIView):
    '''
        Create and list post of the session user
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return self.queryset.filter(owner=account)
    
    def perform_create(self, serializer):
        account = Account.objects.get(user=self.request.user)
        serializer.save(owner=account)

posts_view = PostsView.as_view()


class PostsRetrieveUpdateView(generics.DestroyAPIView):
    '''
        Create and list post of the session user
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return self.queryset.filter(owner=account)
    
    def delete(self,request, pk):
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        account = Account.objects.get(user=self.request.user)

        if post.owner == account:
            post.delete()
            return Response(status=204)
        return Response('Usário não possui permissão para deleter esse post', status=status.HTTP_400_BAD_REQUEST)

posts_detail_view = PostsRetrieveUpdateView.as_view()


class FeedsView(generics.ListAPIView):
    '''
        List post of another users, exclude session user
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        posts = Post.objects.exclude(owner=account).order_by('created_at')
        return posts
    
feeds_view = FeedsView.as_view()


class FeedsUserView(generics.ListAPIView):
    '''
        Filter post by username
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination


    def get_queryset(self):
        username = self.kwargs['username']
        account = Account.objects.get(user__username=username)
        return self.queryset.filter(owner=account).order_by('created_at')

feeds_username_view = FeedsUserView.as_view()


class FeedsFollowingView(generics.ListAPIView):
    '''
        Filter post by follow users
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        following_ids = Follow.objects.filter(user=account).values_list('follow', flat=True)
        return Post.objects.filter(owner__in=following_ids)
    
feeds_following_view = FeedsFollowingView.as_view()