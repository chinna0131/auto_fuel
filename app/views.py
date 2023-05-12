from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
def index(request):
    context = {'code': "success", 'message': "Welcome page", "result": {}}
    # return Response(context, status=status.HTTP_200_OK)
    print("index")
    return render(request, "html/test_h.html",context)


def login(request):
    context = {'code': "success", 'message': "Welcome page", "result": {}}
    # return Response(context, status=status.HTTP_200_OK)
    return render(request, "html/login.html",context)



