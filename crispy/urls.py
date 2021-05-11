from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('crispy/', views.crispy_signup, name='crispy_signup'),
    path('customized_crispy/', views.customized_crispy_signup, name='customized_crispy_signup'),
    path('crispy_helpers/', views.crispy_helpers_signup, name='crispy_helpers_signup'),
]
