from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from todoApi.serializers import TaskSerializer, CommentSerializer
from todoApi.models import Task


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def taskList(request):
	paginator = PageNumberPagination()
	tasks = Task.objects.all().order_by('-id')
    context = paginator.paginate_queryset(tasks, request)
    serializer = MyModelSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
	paginator = PageNumberPagination()
	tasks = Task.objects.get(id=pk)
	context = paginator.paginate_queryset(tasks, request)
	serializer = TaskSerializer(context, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = CommentSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

