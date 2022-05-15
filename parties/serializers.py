from rest_framework import serializers
from . models import Parties, Partyloans


class PartiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'


class PartyloansSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partyloans
        fields = '__all__'
