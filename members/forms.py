from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	Email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
	First_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'First_name'}))
	Last_name = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last_name'}))

	class Meta:
		model = User
		fields = ('Email','username','First_name','Last_name','password1','password2')


	def __init__(self,*args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'