from rest_framework import serializers
from .models import AuthTFfield, UserField

class Authserializers(serializers.ModelSerializer):
	class Meta:
		model = AuthTFfield
		fields = '__all__'


class UserFieldserializers(serializers.ModelSerializer):
	class Meta:
		model = UserField
		fields = '__all__'