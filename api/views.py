from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .pagination import CustomPagination
from .serializers import *
from rest_framework.views import APIView


class CategoryListView(APIView, CustomPagination):
    def get(self, request):
        data = Category.objects.get_queryset().order_by('id')
        results = self.paginate_queryset(data, request, view=self)
        serialized = CategorySerializer(results, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(status=401)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        instance = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = Category.objects.get(id=pk)
        category = CategorySerializer(instance, data=request.data, partial=True)
        if category.is_valid():
            category.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(message, status=401)

    def delete(self, request, pk):
        instance = Category.objects.get(id=pk)
        if instance:
            instance.delete()
        message = {'error': 0, 'message': 'Success'}
        return Response(message, status=200)


""" ===================== Product views ================================="""


class ProductListView(APIView, CustomPagination):
    def get(self, request):
        data = Product.objects.get_queryset().order_by('id')
        results = self.paginate_queryset(data, request, view=self)
        serialized = ProductSerializer(results, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(message, status=401)


class ProductDetailView(APIView):
    def get(self, request, pk):
        instance = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = Product.objects.get(id=pk)
        product = ProductSerializer(instance, data=request.data, partial=True)
        if product.is_valid():
            product.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(message, status=401)

    def delete(self, request, pk):
        instance = Product.objects.get(id=pk)
        if instance:
            instance.delete()
        message = {'error': 0, 'message': 'Success'}
        return Response(message, status=200)


""" ===================== Item views ================================="""


class ItemListView(APIView, CustomPagination):
    def get(self, request):
        data = Item.objects.get_queryset().order_by('id')
        results = self.paginate_queryset(data, request, view=self)
        serialized = ItemSerializer(results, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request):
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            item.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(message, status=401)


class ItemDetailView(APIView):
    def get(self, request, pk):
        instance = Item.objects.get(id=pk)
        serializer = ItemSerializer(instance)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        instance = Item.objects.get(id=pk)
        item = ItemSerializer(instance, data=request.data, partial=True)
        if item.is_valid():
            item.save()
            message = {'error': 0, 'message': 'Success'}
            return Response(message, status=200)
        message = {'error': -1, 'message': 'Not valid'}
        return Response(message, status=401)

    def delete(self, request, pk):
        instance = Item.objects.get(id=pk)
        if instance:
            instance.delete()
        message = {'error': 0, 'message': 'Success'}
        return Response(message, status=200)
