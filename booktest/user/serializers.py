from rest_framework import serializers
from .models import UserBook


class UserBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = ('__all__')

    def create(self, validated_data):
        return UserBook.objects.create(**validated_data)
