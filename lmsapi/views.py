from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Teacher, Student
from lmsapi.serializers import TeacherSerializer, StudentSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# using plain class based view i.e. APIView
class TeacherApiView(APIView):
    def get_object_instance(self, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            return teacher
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # get single teacher by id
    def get(self, request, pk):
        teacher = self.get_object_instance(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    # update teacher by id
    def put(self, request, pk):
        teacher = self.get_object_instance(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        teacher = self.get_object_instance(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeacherApiListCreateView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
