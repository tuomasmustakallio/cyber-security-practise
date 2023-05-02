from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json



@login_required
def addView(request):
	if request.method == "POST":
		iban_num = request.POST["iban"]
		user = request.user
		newAccount = Account.objects.create(owner = user, iban = iban_num)
	return redirect('/')


@login_required
def homePageView(request):
	user = request.user
	owned_accs = Account.objects.filter(owner = user)
	owned_ibans = [x.iban for x in owned_accs]
	return render(request, 'pages/index.html', {'accounts': owned_accs})
