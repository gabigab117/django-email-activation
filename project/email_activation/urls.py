from django.urls import path
from .views import signup_view, logout_view, LoginUser, activate

urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout', logout_view, name="logout"),
    path('activate/<uidb64>/<token>', activate, name="activate")
]
