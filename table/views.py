from django.http import HttpResponse
from .models import Task
from django.shortcuts import render


def week(request, week_name):
    daily_task = Task.objects.get(week_name=week_name)
    return HttpResponse(f"{daily_task.task}")

def home(request):
    html = """
    <p><a href=' http://127.0.0.1:8000/table/Dushanba'>Monday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Seshanba'>Thuestday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Chorshanba'>Wednesday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Payshanba'>Thostday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Juma'>Friday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Shanba'>Saturday<p/>
    <p><a href=' http://127.0.0.1:8000/table/Yakshanba'>Sunday<p/>
    """
    return HttpResponse(html)
