from django.contrib import admin
from django.urls import path
from . import views

app_name = "employee_app"
urlpatterns = [
    path('template/', views.CheckView.as_view(), name="template"),
    path('inform/<pk>/', views.HourList.as_view(), name="inform"),
]
