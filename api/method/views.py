from django.shortcuts import render
from django.http import HttpResponse

def get(request):
    return HttpResponse("GET!")

def post(request):
    return HttpResponse("POST!")

def put(request):
    return HttpResponse("PUT!")

def delete(request):
    return HttpResponse("DELETE!")