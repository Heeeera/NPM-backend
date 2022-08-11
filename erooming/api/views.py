from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.models import User, Routine, User_Routine
from api.serializer import UserSerializer, RoutineSerializer, UserRoutineSerializer
from django.views.decorators.csrf import csrf_exempt


def users_list(request):
    if request.method == "GET":
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        return JsonResponse(userSerializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        userSerializer = UserSerializer(data=data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse(userSerializer.data, status=201)
        return JsonResponse(userSerializer.errors, status=400)

@csrf_exempt
def routine_list(request):
    if request.method == "GET":
        routine  = Routine.objects.all()
        routineSerializer = RoutineSerializer(routine, many=True)
        return JsonResponse(routineSerializer.data, json_dumps_params={"ensure_ascii":False}, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        userSerializer = RoutineSerializer(data=data)
        if userSerializer.is_valid():
            userSerializer.save()
            return JsonResponse(userSerializer.data, status=201)
        return JsonResponse(userSerializer.errors, status=400)