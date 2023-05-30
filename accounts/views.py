from rest_framework import viewsets, generics
from .models import Account, Follow
from .serializers import AccountCreateSerializer, FollowSerializer


class CreateAccountView(generics.ListCreateAPIView):
    '''
        Create and list user
    '''
    queryset = Account.objects.all().order_by('user__username')
    serializer_class = AccountCreateSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class DeleteAccountView(generics.DestroyAPIView):
    '''
        Delete user
    '''
    queryset = Account.objects.all().order_by('user__username')
    serializer_class = AccountCreateSerializer

create_list_view = CreateAccountView.as_view()
delete_list_view = DeleteAccountView.as_view()


class CreateFollowView(generics.ListCreateAPIView):
    '''
        Create and list user
    '''
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        account = Account.objects.get(user=self.request.user)
        follow = Account.objects.get(user__username=self.request.data['follow'])
        return serializer.save(user=account, follow=follow)


class DeleteFollowView(generics.DestroyAPIView):
    '''
        Delete user
    '''
    queryset = Follow.objects.all().order_by('user__username')
    serializer_class = FollowSerializer

create_follow_list_view = CreateFollowView.as_view()
delete_follow_list_view = DeleteFollowView.as_view()


