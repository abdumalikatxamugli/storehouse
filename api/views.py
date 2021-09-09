from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET',])
def categories_list(request):
	data=Category.objects.all()
	serialized=CategorySerializer(data, many=True)	
	return Response(serialized.data)


@api_view(['POST',])
def categories_create(request):
	category=CategorySerializer(data=request.data)
	if category.is_valid():	
		category.save()
		message={'error':0, 'message':'Success'}
		return Response(message, status=200)
	message={'error':-1, message:'Not valid'}
	return Response(status=401)

@api_view(['PATCH',])
def categories_update(request, pk):
	instance=Category.objects.get(id=pk)
	category=CategorySerializer(instance, data=request.data, partial=True)
	print(category)
	if category.is_valid():	
		category.save()
		message={'error':0, 'message':'Success'}
		return Response(message, status=200)
	message={'error':-1, 'message':'Not valid'}
	return Response(message, status=401)

@api_view(['DELETE',])
def categories_delete(request, pk):
	instance=Category.objects.get(id=pk)
	if instance:
		instance.delete()
	message={'error':0, 'message':'Success'}
	return Response(message, status=200)
