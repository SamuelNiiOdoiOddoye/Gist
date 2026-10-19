from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

urlpatterns = [
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
        ),
        name="password_reset_confirm",
    ),
]