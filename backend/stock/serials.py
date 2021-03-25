from rest_framework import serializers
from .models import Stock
class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'