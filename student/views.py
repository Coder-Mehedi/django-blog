from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentResult

class StudentResultView(APIView):
    def get(self, request, roll):
        std = StudentResult.objects.get(roll=roll)
        student_name = std.name
        student_result = std.result
        return Response({'name':student_name, 'result':student_result})