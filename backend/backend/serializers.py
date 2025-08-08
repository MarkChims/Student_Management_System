from django.contrib.auth.models import User
from rest_framework import serializers
from student.models import (
    Level,
    Subject,
    Student,
    Admin,
    Dormitory,
    Room,
    Residence,
    Registration
)

# ========== Student and Admin Serializer ==========

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    reg_number = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = ['id', 'user', 'reg_number', 'gender', 'profile_image', 'level']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # Update user fields explicitly
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        # Update student fields explicitly
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['user', 'admin_id', 'gender', 'profile_image']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin
# Level
class  LevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id","code", "name"]
        model = Level

# Subject
class SubjectSerializer(serializers.ModelSerializer):
    level = LevelSerializer()
    class Meta:
        fields = ["id", "code", "name", "level", "duration", "methodologies"]
        model = Subject

# Dormitory Related Serializers
class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "code", "name", "status", "capacity", "dorm_image"]
        model = Dormitory

class RoomSerializer(serializers.ModelSerializer):
    dorm = DormitorySerializer()
    class Meta:
        fields = ["id", "code", "name", "status", "capacity", "dorm", "floor"]
        model = Room

class ResidenceSerializer(serializers.ModelSerializer):
    dorm = DormitorySerializer()
    student = StudentSerializer()
    room = RoomSerializer()
    class Meta:
        fields = ["id", "room", "dorm", "student"]
        model = Residence

class RegistrationSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    student = StudentSerializer() 
    class Meta:
        fields = ["id", "subject", "student"]
        model = Registration


class DashboardStatsSerializer(serializers.Serializer):
    month_residences = serializers.IntegerField()
    total_students = serializers.IntegerField()
    students_with_subjects = serializers.IntegerField()


class StudentStatsSerializer(serializers.Serializer):
    male_count = serializers.IntegerField()
    female_count = serializers.IntegerField()
    total_count = serializers.IntegerField()
