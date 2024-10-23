from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page_view, name="random_student"),
    path('students', views.students_page_view, name = "all students")
]