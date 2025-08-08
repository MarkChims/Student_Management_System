from django.contrib import admin
from django.urls import path
from student.views import StudentLogin, SubjectRegistration as RegisterSub, RegisteredSubjects
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from administration.views import (
    StudentRegistration,
    SubjectRegistration,
    DormitoryRegistration,
    LevelRegistration,
    RoomRegistration,
    ResidenceApproval,
    StudentsList,
    DormList,
    ResList,
    RoomList,
    SubjectList,
    DeleteStudent,
    DashboardStatsView,
    StudentStatsView,
    EditStudentView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Login Into Sytem For Token Generation and Refresh
    path("login/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="refresh"),


    # Students Urls
    path("student/login/", StudentLogin.as_view()),
    path("student/register/", RegisterSub.as_view()),
    path("student/registered/", RegisteredSubjects.as_view()),

    # Admin Urls
    # Create New Database Items
    path("staff/add-student", StudentRegistration.as_view()),
    path("staff/add-subject", SubjectRegistration.as_view()),
    path("staff/add-dorm", DormitoryRegistration.as_view()),
    path("staff/add-room", RoomRegistration.as_view()),
    path("staff/add-level", LevelRegistration.as_view()),
    path("staff/approve-accomodation", ResidenceApproval.as_view()),

    # Dashboard
    path("staff/dashboardstats", DashboardStatsView.as_view(), name="dashboard-stats"),
    path("staff/studentsstats", StudentStatsView.as_view(), name="student-stats"),

    # Edit 
    path("staff/student-edit/<int:pk>/", EditStudentView.as_view()),


    # Retrieve Database Items
    path("staff/student-list", StudentsList.as_view()),
    path("staff/dorm-list", DormList.as_view()),
    path("staff/res-list", ResList.as_view()),
    path("staff/room-list", RoomList.as_view()),
    path("staff/subject-list", SubjectList.as_view()),

    # Delete Items From Database
    path("staff/delete-student/<int:pk>/", DeleteStudent.as_view())
]

# Add media server url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
