from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, rwquest):
        cache_key = 'products_list'
        
        if not cache.get(cache_key):
            print('cache_miss')
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            json_raspinse = serializer.data
            cache.set(cache_key, json_raspinse, 20)
        json_raspinse = cache.get(cache_key)
        return Response(json_raspinse)