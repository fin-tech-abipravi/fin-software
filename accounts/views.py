from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail

present_time = datetime.now()

'{:%H:%M:%S}'.format(present_time)
updated_time = datetime.now() + timedelta(hours=2)


@api_view(['POST'])
def loginuser(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    if UserField.objects.filter(username=username).exists() and UserField.objects.filter(password=password):
        response_data = {
            'authKey': setAuth(username),
            'time_expire': updated_time,    
            'user': username
        }
        return Response(response_data)
    else:
        return Response("Not Logged...")


def setAuth(username):
    authKey = secrets.token_hex(20)
    value = {'Auth': authKey, 'expires': updated_time, 'user': username}
    expire_time = updated_time
    print(value)
    print(authKey)
    serializer = Authserializers(data=value)
    if serializer.is_valid():
        serializer.save()
    else:
        print(value)
    return authKey


@api_view(['POST'])
def createUser(request):
    serializer = UserFieldserializers(data = request.data)
    name = request.data.get('username')
    if serializer.is_valid():
        subject = 'User Created Successfully'
        message = f'Hi {name}, thank you for registering in FINSOFT-ABIPRAVI.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.data.get('email_address'), ]
        try:
            send_mail( subject, message, email_from, recipient_list)
            serializer.save()
        except BaseException as e:
            print("error", e)
            return Response(e)
    else:
        print(request.data, "invalid data got")
    
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request):
    data = UserField.objects.all()
    serializer = UserFieldserializers(data, many =True)
    return Response(serializer.data)
