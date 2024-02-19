from smtplib import SMTPAuthenticationError

from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.http import require_POST

from email_activation.forms import SignUpForm
from email_activation.verification import send_email_verification, email_verification_token


def index_view(request):
    return render(request, "account/index.html")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            try:
                send_email_verification(request, user)
                messages.add_message(request, level=messages.INFO,
                                     message="Success message")
            except SMTPAuthenticationError:
                messages.add_message(request, level=messages.INFO,
                                     message="Fail message")
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, "account/signup.html", context={"form": form})


def activate(request, uidb64, token):
    """
        Activates a user account.

        This function is responsible for handling the account activation process. It decodes the user ID from base64 and
        retrieves the corresponding user object. If the user exists and the provided token is valid, the user's account
        is activated. It displays a success message upon successful activation or an error message if the activation fails.

        Args:
            request: The HTTP request object.
            uidb64: A base64-encoded string representing the user's ID.
            token: A token for verifying the user's email address.

        Returns:
            HttpResponse: Redirects to the landing page after attempting to activate the account, with a success or error message.
        """
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.INFO, "Success !")
        return redirect("index")
    else:
        messages.add_message(request, messages.INFO,
                             "Fail !")
        return redirect("index")


class LoginUser(LoginView):
    template_name = "account/login.html"
    next_page = reverse_lazy("index")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("index")
