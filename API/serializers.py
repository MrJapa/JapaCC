from rest_framework import serializers
from Japa.models import NyBestilling

class NyBestillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NyBestilling
        fields = '__all__'

