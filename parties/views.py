from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *


class PartiesView(APIView):
    def get(self, request, format=None):
        data = Costumers.objects.all()
        serializer = Costumersserializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = Costumersserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, safe=False)
