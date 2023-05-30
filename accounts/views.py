from rest_framework import viewsets, generics
from .models import Account
from .serializers import AccountCreateSerializer


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