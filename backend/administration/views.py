from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.serializers import (
    DashboardStatsSerializer,
    StudentSerializer,
    StudentStatsSerializer,
    SubjectSerializer,
    ResidenceSerializer,
    DormitorySerializer,
    LevelSerializer,
    RoomSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from student.models import Registration, Student, Residence, Subject, Dormitory, Level, Room
import random
from django.http import JsonResponse as Response
# Views That Add New Items To  The Database

class StudentRegistration(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class SubjectRegistration(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class DormitoryRegistration(generics.CreateAPIView):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"occupants": Residence.objects.filter(dorm=self.id).count()})

class LevelRegistration(generics.CreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]

class RoomRegistration(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class ResidenceApproval(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student_id = request.data.get("student")
        dorm_id = request.data.get("dorm")

        try:
            dorm = Dormitory.objects.get(id=dorm_id)
            student = Student.objects.get(id=student_id)
        except (Dormitory.DoesNotExist, Student.DoesNotExist):
            return Response(
                {"error": "Dorm or Student not found"}
            )

        # Find all rooms in this dorm
        rooms = Room.objects.filter(dorm=dorm)

        # Filter rooms with available space
        available_rooms = []
        for room in rooms:
            current_occupants = Residence.objects.filter(room=room).count()
            if current_occupants < room.capacity:
                available_rooms.append(room)

        if not available_rooms:
            return Response(
                {"error": "No available rooms in this dorm"}
            )

        # Randomly pick a free room
        selected_room = random.choice(available_rooms)

        # Create Residence
        residence = Residence.objects.create(
            student=student, dorm=dorm, room=selected_room
        )

        return Response(
            {
                "message": f"Student {student.reg_number} allocated to room {selected_room} in dorm {dorm.name}",
                "residence_id": residence.id,
            },
        )

    def perform_create(self, serializer):
        if not serializer.is_valid:
            print("Serializer Not Valid", serializer.errors)
        else:
            serializer.save()


# Views That Get Information From The Database
class StudentsList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class DormList(generics.ListAPIView):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
    permission_classes = [IsAuthenticated]

class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class ResList(generics.ListAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer
    permission_classes = [IsAuthenticated]

class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

# Dashboard Items
class StudentStatsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        male_count = Student.objects.filter(gender__iexact="Male").count()
        female_count = Student.objects.filter(gender__iexact="Female").count()
        total_count = Student.objects.count()

        data = {
            "male_count": male_count,
            "female_count": female_count,
            "total_count": total_count
        }

        serializer = StudentStatsSerializer(data)
        return Response(serializer.data)
    
class DashboardStatsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Get month/year from query params (default to current)
        month = int(request.query_params.get("month", now().month))
        year = int(request.query_params.get("year", now().year))

        # Students allocated to residences this month
        month_residences = Residence.objects.filter(
            date__month=month,
            date__year=year
        ).count()

        # Total students
        total_students = Student.objects.count()

        # Students registered for at least 1 subject (via Registration)
        students_with_subjects = Registration.objects.values('student').distinct().count()

        data = {
            "month_residences": month_residences,
            "total_students": total_students,
            "students_with_subjects": students_with_subjects
        }

        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)


# Delete Items from Database
class DeleteStudent(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Allow deletion of any student
        return Student.objects.all()


class EditStudentView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]