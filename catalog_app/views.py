from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_class = [IsAdminUser]
        else:
            permission_class = [IsOwnerOrReadOnly]

        return [permission() for permission in permission_class]