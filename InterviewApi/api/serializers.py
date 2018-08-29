from rest_framework import serializers
from .models import Currency

#
# class CurrenciesSerializer(serializers.ModelSerializer):
#     currency_name = serializers.RelatedField(source='currency', read_only=True)
#
#     class Meta:
#         model = Currencies
#         fields = ("created_at", "currency_name")

#
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("name", "value")