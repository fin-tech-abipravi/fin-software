from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from accounts.models import *
from accounts.serializers import *
from datetime import datetime


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


class ClosedCostumerView(APIView):
    def get(self, request, pk, format=None):
        if(check_auth(pk) == True):
            data = Costumers.objects.all()
            serializer = Costumersserializer(data, many=True)
            return Response(serializer.data)
        return Response({"Error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, pk, format=None):
        if(check_auth(pk) == True):
            serializer = Costumersserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, safe=False)
        return Response({"Error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)


class ClosedCostumerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Costumers.objects.filter(costumer_id=pk)
        except Costumers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = Costumersserializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = Costumersserializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClosedLoanView(APIView):
    def get(self, request, pk, format=None):
        if(check_auth(pk) == True):
            data = Loandetails.objects.all()
            serializer = LoanDetailsserializer(data, many=True)
            return Response(serializer.data)
        return Response({"Error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, pk, format=None):
        if(check_auth(pk) == True):
            serializer = LoanDetailsserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, safe=False)
        return Response({"Error": "Token expired"}, status=status.HTTP_401_UNAUTHORIZED)


class ClosedLoanDetailView(APIView):
    def get_object(self, pk):
        try:
            return Loandetails.objects.get(id=pk)
        except Loandetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = LoanDetailsserializer(data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = LoanDetailsserializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
