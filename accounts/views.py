from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
	politicians = Politicians.objects.all()
	categories = Politician_Category.objects.all()
	parties = Parties.objects.all()

	context = {'politicians':politicians,'categories':categories, 'parties':parties}
	return render(request,'accounts/dashboard.html',context)


def candidates(request):
	candidates = Politicians.objects.all()
	context = {'candidates':candidates}
	return render(request,'accounts/candidates.html',context)


def politicians(request,pk):
	candidates = Politicians.objects.get(id=pk)
	context = {'candidates':candidates}
	return render(request,'accounts/politician.html')


