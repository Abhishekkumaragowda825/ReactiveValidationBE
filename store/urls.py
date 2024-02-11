from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('getStudents', views.get_students),
    path('createStudent', views.create_student),
    path('deleteStudent/id=<int:pk>', views.delete_student),
    path('updateStudent', views.update_student)
]