from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['color', 'cover']
    search_fields = ['color']

    def get_permissions(self):
        if self.action == "create":
            permission_class = [IsAdminUser]
        else:
            permission_class = [IsOwnerOrReadOnly]

        return [permission() for permission in permission_class]