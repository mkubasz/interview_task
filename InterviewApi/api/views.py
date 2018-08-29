from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.response import Response

class CurrenciesView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class DetailsView(APIView):
    def get(self, request, pk):
        name: str = pk
        if name:
            query = Currency.objects.filter(name=name.upper()).first()
            if not query:
                return JsonResponse({
                    'status_code': 404,
                    'error': 'The resource was not found'
                })
        else:
            return JsonResponse({
                'status_code': 404,
                'error': 'The resource was not found'
            })

        return Response({"id": query.id, "name": query.name, "value": query.value})