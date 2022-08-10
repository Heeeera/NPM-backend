from rest_framework import serializers
from api.models import Users,Routine,User_Routine

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name','email']

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ['id','title','max_people_number','now_people_number','description','start_date','end_date','max_count','status']


class UserRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Routine
        fields = ['id','user_id','routine_id','now_count','max_count','is_host']
