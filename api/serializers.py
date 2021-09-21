from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('mymethod')

    def mymethod(self, obj):
        return obj.category_id.name

    class Meta:
        model = Product
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    income_date = serializers.DateField(input_formats=["%Y-%m-%d"])

    class Meta:
        model = Item
        fields = '__all__'
