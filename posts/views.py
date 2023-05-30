from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from accounts.models import Account
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page'


class PostsView(generics.CreateAPIView):
    '''
        Create and list post of the session user
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        account = Account.objects.get(user=self.request.user)
        serializer.save(owner=account)

posts_view = PostsView.as_view()


class FeedsView(generics.ListAPIView):
    '''
        List post of another users, exclude session user
    '''
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        print(self.request.query_params)
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
        
        account = Account.objects.get(user=self.request.user)
        return self.queryset.filter(owner=account)

feeds_username_view = FeedsUserView.as_view()



