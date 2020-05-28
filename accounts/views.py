from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'accounts/dashboard.html')


def candidates(request):
	return render(request,'accounts/candidates.html')