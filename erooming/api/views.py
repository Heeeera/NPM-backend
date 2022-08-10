from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.models import Users, Routine, User_Routine
from api.serializer import UsersSerializer, RoutineSerializer, UserRoutineSerializer
import json

def users_list(request):
    if request.method == "GET":
        users = Users.objects.all()
        userSerializer = UsersSerializer(users, many=True)
        return JsonResponse(userSerializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        userSerializer = UsersSerializer(data=data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse(userSerializer.data, status=201)
        return JsonResponse(userSerializer.errors, status=400)

def routine_list(request):
    if request.method == "GET":
        routine  = Routine.objects.all()
        routineSerializer = RoutineSerializer(routine, many=True)
        return JsonResponse(routineSerializer.data,json_dumps_params={"ensure_ascii":False},safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        userSerializer = RoutineSerializer(data=data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse(userSerializer.data, status=201)
        return JsonResponse(userSerializer.errors, status=400)


# Create your views here.
