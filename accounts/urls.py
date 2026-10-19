from django.urls import path
from .views import SignUpView,password_reset_preview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        "password_reset/",
        password_reset_preview,
        name="password_reset",
    ),
    path(
            "reset/<uidb64>/<token>/",
            auth_views.PasswordResetConfirmView.as_view(
                template_name="registration/password_reset_confirm.html",
            ),
            name="password_reset_confirm",
        ),
]

