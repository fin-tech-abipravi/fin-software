from rest_framework import serializers
from . models import *


class Costumersserializer(serializers.ModelSerializer):
	class Meta:
		model = Costumers
		fields = '__all__'


class LoanDetailsserializer(serializers.ModelSerializer):
	class Meta:
		model = Loandetails
		fields = '__all__'
