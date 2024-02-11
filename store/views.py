import json
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Student

@api_view(['GET'])
def get_students(request): 
    data = Student.objects.values()
    return JsonResponse(list(data), safe=False)

@api_view(['POST'])
def create_student(request):
    instance = Student(name=request.data['name'],lname=request.data['lname'],
                    email=request.data['email'],gender=request.data['gender'],
                    message=request.data['message'], country=request.data['country'])
    instance.save()
    return Response("200 ok")

@api_view(['DELETE'])
def delete_student(request,pk):
    instance = Student.objects.get(id=pk)
    instance.delete()
    return Response("200 ok")

@api_view(['PUT'])
def update_student(request):
    instance = Student.objects.get(id=request.data['id'])
    instance.name=request.data['name']
    instance.lname=request.data['lname']
    instance.email=request.data['email']
    instance.gender=request.data['gender'],
    instance.message=request.data['message']
    instance.country=request.data['country']
    instance.save()
    return Response("200 ok")

