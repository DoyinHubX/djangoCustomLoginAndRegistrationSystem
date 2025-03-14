from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, ProfileView, CustomLoginView
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Home page view
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  # Redirect to index page after logout
]



