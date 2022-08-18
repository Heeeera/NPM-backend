from rest_framework import serializers
from api.models import Routine, User_Routine
from allauth.socialaccount.models import SocialAccount

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ['id', 'title', 'max_people_number', 'now_people_number',
                  'description', 'start_date', 'end_date', 'max_count', 'created_at', 'status']


class UserRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Routine
        fields = ['id', 'user_id', 'routine_id',
                  'now_count', 'max_count', 'created_at', 'updated_at', 'is_host']


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ['id', 'provider', 'uid', 'last_login', 'date_joined', 'user_id', 'extra_data']