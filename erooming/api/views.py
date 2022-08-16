from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.models import User, Routine, User_Routine
from api.serializer import UserSerializer, RoutineSerializer, UserRoutineSerializer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'POST'])
def routine_list(request):
    if request.method == "GET":
        routines = Routine.objects.all()
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RoutineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT'])
def routine_list_put(request, pk):
    if request.method == "PUT":
        routine = Routine.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = UserRoutineSerializer(routine, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def user_routine(request):
    if request.method == "GET":
        user_routines = User_Routine.objects.all()
        serializer = UserRoutineSerializer(user_routines, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserRoutineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['PUT'])
def user_routine_put(request, pk):
    if request.method == "PUT":
        user_routine = User_Routine.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = UserRoutineSerializer(user_routine, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

