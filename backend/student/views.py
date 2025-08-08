from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.serializers import StudentSerializer, StudentStatsSerializer, SubjectSerializer, ResidenceSerializer, RegistrationSerializer, DashboardStatsSerializer
from student.models import Student, Residence, Subject, Registration
from django.http import JsonResponse as Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Residence, Student, Subject

# Create your views here.
class StudentLogin(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     reg_number = request.data.get("reg_number");
    #     queryset = Student.objects.get(reg_number=reg_number)
    #     try:
    #         student = Student.objects.get(reg_number=reg_number)
    #     except Student.DoesNotExist:
    #         Response({
    #             "message": "Failed To Login"
    #         })

    #     return Response(
    #         {
    #             "logged-user": student
    #         }
    #     )

    def get_queryset(self):
        user = self.request.user
        print(self.request)
        try:
            Student.objects.get(id=user.id)
        except Student.DoesNotExist:
            print("error")
            # return Response(
            #     {
            #         "message": "User Not Found"
            #     }
            # )




class SubjectsView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]

class SubjectRegistration(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

class RegisteredSubjects(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
<<<<<<< HEAD
=======

class EditStudentView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
>>>>>>> 840c1ce ( add backend and frontend folders)
