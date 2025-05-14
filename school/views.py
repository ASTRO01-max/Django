from django.shortcuts import render
from django.http import HttpResponse

def say_hi(request):
    return HttpResponse("Assalomu aleykom!")

def class_info(request):
    return HttpResponse("Sinfda 20ta o'quvchilar bor!")
