from rest_framework import serializers
from . models import ( Costumerdetails, Collectionlist, Dlammounts,
Ammountinhand, Expence, Expencetotal, Closeup, Closedown,
Otherammountin, Otherammountout, Inversment, Others )

class Costumerdetailsserializer(serializers.ModelSerializer):
	class Meta:
		model = Costumerdetails
		fields = '__all__'

class CostumerListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        cost_mapping = {cust.id: cust for cust in instance}
        data_mapping = {item['id']: item for item in validated_data}
        ret = []
        for prod_id, data in data_mapping.items():
            cost = cost_mapping.get(prod_id, None)
            if cost is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(cost, data))

        return ret

class BulkCostumerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
   
    class Meta:
        model = Costumerdetails
        fields = '__all__'
        list_serializer_class = CostumerListSerializer   

class Collectionlistserializer(serializers.ModelSerializer):
	class Meta:
		model = Collectionlist
		fields = '__all__'

class CollectionListBulkSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        clistitems = [Collectionlist(**item) for item in validated_data]
        return Collectionlist.objects.bulk_create(clistitems)

class CollectionBulkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectionlist
        list_serializer_class = CollectionListBulkSerializer
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
