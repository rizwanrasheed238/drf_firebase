from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers,UserSerializer
from .models import Task, NotificationStatus
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.generics import CreateAPIView
import pyrebase
config={
    "apiKey": "AIzaSyCLdPBF57xanUzG-g2julG0-FacYOie8rg",
    "authDomain": "django-task-83e44.firebaseapp.com",
    "databaseURL": "https://django-task-83e44-default-rtdb.firebaseio.com",
    "projectId": "django-task-83e44",
    "storageBucket": "django-task-83e44.appspot.com",
    "messagingSenderId": "912055235853",
    "appId": "1:912055235853:web:54d0364c2e76a8a0d52c44",
    "measurementId": "G-64W3GRNQF7"

}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

def bin(request):
    username=database.child('User Details').child("Username").get().val()
    password=database.child('User Details').child("Password").get().val()
    context={
        "username":username,
        "password":password,
    }
    success = True
    response = "Notification sent successfully"
    notification = NotificationStatus.objects.create(
        username=username,
        success=success,
        response=response
    )
    notification.save()

    return Response(context)


@api_view(['POST'])
def createbin(request):
    username=request.data.get('username')
    password=request.data.get('password')

    return Response(status=201)



class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers

class DueTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all().order_by('date_created').filter(completed=False)

class CreateuserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class CompletedTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all().order_by('date_created').filter(completed=True)


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()

