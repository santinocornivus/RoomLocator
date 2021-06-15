from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import SignUpForm

# Create your views here.

class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'Registration/register.html'
	redirect_authenticated_user = True
	success_url = reverse_lazy('index')
	def form_valid(self,form):
		user = form.save()
		if user is not None:
			login(self.request , user)
		return super(UserRegisterView, self).form_valid(form)

	def get(self , *args , **kwargs):
		if self.request.user.is_authenticated:
			return redirect('index')
		return super(UserRegisterView,self).get(*args,**kwargs)


class CustomLoginView(LoginView):
	template_name = 'Registration/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('index')

	def get(self , *args , **kwargs):
		if self.request.user.is_authenticated:
			return redirect('index')
		return super(UserRegisterView,self).get(*args,**kwargs)


def home(request):
	return render(request,'members/home.html')

def index(request):
	return render(request,'homepage/index.html')