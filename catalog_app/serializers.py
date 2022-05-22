from rest_framework import serializers
from .models import Category
from members_app.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")
    edition = serializers.CharField(source="get_edition_display")
    owner = UserSerializer()
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1