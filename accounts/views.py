from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

User = get_user_model()


def password_reset_preview(request):
    form = PasswordResetForm(request.POST or None)

    if request.method == "POST":
        if not form.is_valid():
            return render(
                request,
                "registration/password_reset_form.html",
                {"form": form},
            )

        email = form.cleaned_data["email"]
        users = User._default_manager.filter(
            email__iexact=email,
            is_active=True,
        )

        for user in users:
            if user.has_usable_password():
                context = {
                    "email": user.email,
                    "domain": request.get_host(),
                    "site_name": request.get_host(),
                    "protocol": "https" if request.is_secure() else "http",
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    "token": default_token_generator.make_token(user),
                }

                return render(
                    request,
                    "registration/template_email.html",
                    context,
                )

        # Do not reveal whether an account exists.
        return render(
            request,
            "registration/password_reset_done.html",
        )

    return render(
        request,
        "registration/password_reset_form.html",
        {"form": form},
    )