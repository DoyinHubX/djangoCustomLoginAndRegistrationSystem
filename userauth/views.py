from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

# Homepage view
def index(request):
    return render(request, 'userauth/index.html')

# Registration View
class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'userauth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')
    success_message = "Registration successful. Welcome!"

    def form_valid(self, form):
        # Save the user and log them in
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'userauth/login.html'
    redirect_authenticated_user = True  # Redirect logged-in users away from the login page

# Profile View (Requires Authentication)
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userauth/profile.html'

