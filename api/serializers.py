from rest_framework import serializers
from . models import ( Costumerdetails, Collectionlist, Dlammounts,
Ammountinhand, Expence, Expencetotal, Closeup, Closedown,
Otherammountin, Otherammountout, Inversment, Others )

class Costumerdetailsserializer(serializers.ModelSerializer):
	class Meta:
		model = Costumerdetails
		fields = '__all__'
class Collectionlistserializer(serializers.ModelSerializer):
	class Meta:
		model = Collectionlist
		fields = '__all__'

class Dlammountsserializer(serializers.ModelSerializer):
	class Meta:
		model = Dlammounts
		fields = '__all__'

class Ammountinhandserializer(serializers.ModelSerializer):
	class Meta:
		model = Ammountinhand
		fields = '__all__'

class Expenceserializer(serializers.ModelSerializer):
	class Meta:
		model = Expence
		fields = '__all__'

class Expencetotalserializer(serializers.ModelSerializer):
	class Meta:
		model = Expencetotal
		fields = '__all__'

class Closeupserializer(serializers.ModelSerializer):
	class Meta:
		model = Closeup
		fields = '__all__'

class Closedownserializer(serializers.ModelSerializer):
	class Meta:
		model = Closedown
		fields = '__all__'

class Otherammountinserializer(serializers.ModelSerializer):
	class Meta:
		model = Otherammountin
		fields = '__all__'

class Otherammountoutserializer(serializers.ModelSerializer):
	class Meta:
		model = Otherammountout
		fields = '__all__'

class Inversmentserializer(serializers.ModelSerializer):
	class Meta:
		model = Inversment
		fields = '__all__'

class Othersserializer(serializers.ModelSerializer):
	class Meta:
		model = Others
		fields = '__all__'