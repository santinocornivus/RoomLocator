from django.urls import path,include
from .views import index,UserRegisterView #,CustomLoginView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('',index ,name='index'),
    # path('login/',CustomLoginView.as_view() , name = "login"),
    path('oauth/', include('social_django.urls', namespace='social')), 
     path('accounts/', include('allauth.urls')),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('', TemplateView.as_view(template_name="homepage/index.htm")),
    ]
