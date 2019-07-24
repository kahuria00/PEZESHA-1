from django.shortcuts import render
from .forms import UserForm
from .forms import LoginForm
from .models import User


from django.shortcuts import redirect



def register_user(request):
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("login_user")
	else:
		form=UserForm()
	return render (request,"register_user.html",{"form":form})


def login_user(request):
	if request.method=="POST":
		form=LoginForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form=LoginForm()
	return render(request,"login_user.html",{"form":form})

def list_user(request):
	user=User.objects.all()
	return render(request,"list_user.html",{"user":user})

def edit_user(request,pk):
	user=User.objects.get(pk=pk)
	if request.method=="POST":
		form=UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
	else:
		form=UserForm(instance=user)
	return render(request,"edit_user.html",{"form":form})

# Create your views here.
