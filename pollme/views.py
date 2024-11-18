from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request,'home.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django import forms  # Replace with your actual form
