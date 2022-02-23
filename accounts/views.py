from django.shortcuts import render
from .models import *
import secrets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from encodedecode import *
from rest_framework.response import Response
from .serializers import *
from datetime import datetime, timedelta, date

from django.conf import settings
from django.core.mail import send_mail

present_time = datetime.now()

'{:%H:%M:%S}'.format(present_time)
updated_time = datetime.now() + timedelta(hours=2)


def check_auth(Authkey):
    # getting current date and time for validating the token expire time
    present_time = datetime.now()
    '{:%H:%M:%S}'.format(present_time)
    updated_time = datetime.now()
    if AuthTFfield.objects.filter(Auth=Authkey):
        Auth = AuthTFfield.objects.get(Auth=Authkey)
        serializer = Authserializers(Auth, many=False)
        expire_time = serializer.data.get('expires')
        # remove the z from the output time
        expire_time = expire_time.replace('Z', "")
        # Converting datetime form string format to Date Time format for verifing the expiring time
        expire_time = datetime.strptime(expire_time, '%Y-%m-%dT%H:%M:%S.%f')
        # checking wheather the current time is greater the expire time is true it will not login else it will login return the data to the user
        if updated_time > expire_time:
            return False
        else:
            return True


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
    # print(value)
    # print(authKey)
    serializer = Authserializers(data=value)
    if serializer.is_valid():
        serializer.save()
    else:
        print(value)
    return authKey


@api_view(['POST'])
def createUser(request):
    serializer = UserFieldserializers(data=request.data)
    name = request.data.get('username')
    if serializer.is_valid():
        serializer.save()
        subject = 'User Created Successfully'
        message = f'Hi {name}, thank you for registering in FINSOFT-ABIPRAVI.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.data.get('email_address'), ]
        try:
            send_mail(subject, message, email_from, recipient_list)
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
    serializer = UserFieldserializers(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def sendEmail(request, pk):
    if check_auth(pk) == True:
        name = request.data.get('name')
        cash = request.data.get('cash')
        closedcostumers = request.data.get('close')
        sendemail = request.data.get('email')
        financecompanycopy = 'praveenkumar.abipravi@outlook.in'

        subject = f'Cash In hand: {date.today()} - Abipravi Finance'
        message = f'''Hi {name}, 
        \n{date.today()}'s Data:
        \n========================
        \nCash In hand = {cash}
        \nClosed Costumers = {closedcostumers}
        \n\nThank you for using Abipravi Finance.
        
        \nRegards,
        \nPraveen Kumar,
        \nAbipravi Finance
        '''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [sendemail, financecompanycopy, ]
        try:
            send_mail(subject, message, email_from, recipient_list)
            return Response("Sent")
        except BaseException as e:
            print("error", e)
            return Response(e)

    else:
        return Response("Auth Failed")


@api_view(['POST'])
def sendHtmlEmail(request):
    if request.data.get("token") == "1234567890":
        subject = request.data.get('subject')
        mail_to = request.data.get('mail_to')
        message = request.data.get('body')
        email_from = settings.EMAIL_HOST_USER
        financecompanycopy = "praveenkumar.abipravi@outlook.in"
        recipient_list = [mail_to, financecompanycopy, ]
        try:
            send_mail(subject, message, email_from, recipient_list)
            return Response("Sent")
        except BaseException as e:
            print("error", e)
            return Response(e)
    else:
        return Response("Auth Failed")
