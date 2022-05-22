from unicodedata import category
from django.shortcuts import render

from catalog_app.models import Category
from .models import User
# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from catalog_app.models import Category
from catalog_app.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from location_app.models import RackItem


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_class = [AllowAny]
        else:
            permission_class = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_class]

    @action(detail=True)
    def my_books(self, request, pk=None):
        queryset = Category.objects.filter(
            owner__id = pk
        )
        serializer = BookSerializer(queryset, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True)
    def my_book_on_location(self, request, pk=None):
        queryset = RackItem.objects.filter(
            category__owner__id=pk
        ).values_list("category__id", flat=True)
        categories = Category.objects.filter(
            id__in=queryset
        )
        serializer = BookSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)