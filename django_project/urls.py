"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djano.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

User = get_user_model()

def password_reset_preview(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        users = User._default_manager.filter(email_iexact=email, is_active=True,)
        
        for user in users:
            if user.has_usable_password():
                context={
                    'email':user.email,
                    'domain':request.get_host(),
                    'site_name': request.get_host(),
                    'protocol': 'https' if request.is_secure() else 'http',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
                
                # avoid revealing whether an acount exists
                return render(request, 'registration/template_email.html', context)
            
            return render(request, 'registration/password_reset_done.html')
            
        

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
