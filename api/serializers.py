from django.contrib.auth.models import Group, User
from rest_framework import serializers

from newspaper.models import Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', "first_name", "last_name"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

        
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ["id", "name"]
        