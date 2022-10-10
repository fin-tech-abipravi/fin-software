from rest_framework import serializers
from .models import AuthTFfield, UserField, AccessUsers

class Authserializers(serializers.ModelSerializer):
	class Meta:
		model = AuthTFfield
		fields = '__all__'


class UserFieldserializers(serializers.ModelSerializer):
	class Meta:
		model = UserField
		fields = '__all__'

class AccessUsersserializers(serializers.ModelSerializer):
	class Meta:
		model = AccessUsers
		fields = '__all__'