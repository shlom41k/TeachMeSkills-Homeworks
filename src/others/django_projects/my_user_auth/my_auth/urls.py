from django.urls import path
from django.conf import settings
from .views import IndexView, RegisterView, LoginView, HomeView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('home/', HomeView.as_view(), name="home"),
]
