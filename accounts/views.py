from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
	politicians = Politicians.objects.all()
	categories = Politician_Category.objects.all()

	context = {'politicians':politicians,'categories':categories}
	return render(request,'accounts/dashboard.html',context)


def candidates(request):
	return render(request,'accounts/candidates.html')

