from rest_framework import viewsets, generics
from .models import User
from .serializers import AccountSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
