from rest_framework import serializers
from URLshortener.models import URL, UserSavedLink

class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ('__all__',)


class UserSavedLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = UserSavedLink
        fields = ('__all__',)