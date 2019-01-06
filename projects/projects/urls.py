from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/employees/', views.EmployeeList.as_view()),
]
