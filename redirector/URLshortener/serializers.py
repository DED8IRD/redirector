from rest_framework import serializers
from django.contrib.auth.models import User
from URLshortener.models import URL, UserSavedLink

class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'


class UserSavedLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = URLSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserSavedLink
        fields = '__all__'
