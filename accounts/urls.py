from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ResgisterView, login_view, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/logup/', ResgisterView.as_view()),
    path("api/login/", obtain_auth_token),   
    path("api/loginp/", login_view),  #endpoit login personalizado
    path("api/logout/", LogoutView.as_view())
]
    
