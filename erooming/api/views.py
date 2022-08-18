from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from api.models import Routine, User_Routine
from api.serializer import RoutineSerializer, UserRoutineSerializer
from django.views.decorators.csrf import csrf_exempt

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

