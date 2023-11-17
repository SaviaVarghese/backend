from rest_framework import serializers
from blog.models import BlogModel
from blog.models import UserModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=('__all__')