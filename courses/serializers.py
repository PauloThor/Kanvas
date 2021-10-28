from rest_framework import serializers
from accounts.serializers import UserSerializer

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    users = UserSerializer(many=True)