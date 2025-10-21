from django.shortcuts import render

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('full_name')
    serializer_class = StudentSerializer
