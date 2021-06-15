from django.urls import path

from . import views

urlpatterns =[
	path("",views.index,name="home"),
	# path('contact/',contactView,name='contact'),
	# path('success/',successView,name='success'),
]