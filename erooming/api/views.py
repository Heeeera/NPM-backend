import profile
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from api.models import Routine, User_Routine
from api.serializer import RoutineSerializer, UserRoutineSerializer, SocialAccountSerializer
from django.views.decorators.csrf import csrf_exempt
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse
import json

@csrf_exempt
@api_view(['GET', 'POST'])
def routine_list(request):
    if request.method == "GET":
        routine_status = request.GET.get("status", None)

        routines = Routine.objects.all()
        serializer = RoutineSerializer(routines, many=True)
        
        if routine_status:
            routines = Routine.objects.filter(status=routine_status)
            if len(routines) != 0:
                serializer = RoutineSerializer(routines, many=True)
                return Response(serializer.data)
            else:
                return Response(None)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RoutineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PATCH'])
def routine_list_patch(request, pk):
    if request.method == "PATCH":
        routine = Routine.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = RoutineSerializer(routine, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def user_routine(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id', None)
        routine_id = request.GET.get('routine_id', None)

        user_routines = User_Routine.objects.all()
        serializer = UserRoutineSerializer(user_routines, many=True)
        if user_id and routine_id:
            user_routine = User_Routine.objects.filter(user_id=user_id, routine_id=routine_id)
            if len(user_routine) != 0:
                serializer = UserRoutineSerializer(user_routine[0])
                return Response(serializer.data)
            else:
                return Response(None)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserRoutineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def all_user_routines(request):
    if request.method == "GET":
        routine_id = request.GET.get('routine_id', None)
        if routine_id:
            user_routine = User_Routine.objects.filter(routine_id=routine_id)
            if len(user_routine) != 0:
                serializer = UserRoutineSerializer(user_routine, many=True)
                return Response(serializer.data)
            else:
                return Response(None)

@csrf_exempt
@api_view(['GET', 'PATCH'])
def user_routine_patch(request, pk):
    if request.method == "GET":
        user_routine = User_Routine.objects.get(pk=pk)
        serializer = UserRoutineSerializer(user_routine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == "PATCH":
        user_routine = User_Routine.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = UserRoutineSerializer(user_routine, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def user_routine_delete(request, uk, rk):
    if request.method =="DELETE":
        user_routine = User_Routine.objects.filter(user_id=uk, routine_id=rk)
        user_routine.delete()
        return Response("Deleted", status=status.HTTP_200_OK)
    return Response("ERROR",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def user_routine_list(request,pk):
    if request.method == "GET":
        user_routine = User_Routine.objects.filter(user_id=pk)
        if(user_routine !=0):
            serializer = UserRoutineSerializer(user_routine, many=True)
            return_list = []
            for userAndRoutine in serializer.data:
                routine_model = Routine.objects.filter(id=userAndRoutine['routine_id'])
                serial = RoutineSerializer(routine_model[0])
                return_list.append(serial.data)
            return Response(return_list)

@csrf_exempt
@api_view(['GET'])
def social_account_profile(request, pk):
    if request.method == "GET":
        social_account = SocialAccount.objects.get(user=pk)
        serializer = SocialAccountSerializer(social_account)
        
        extra_data = serializer.data['extra_data']
        profile_url = ""
        for el in extra_data.split("'"):
            if "https" in el:
                profile_url = el
        
        response = {"profile_url" : profile_url}
        return Response(response)
        