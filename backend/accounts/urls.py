from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('@<str:username>', views.ProfileView.as_view() , name = 'user_profile'),
    path('login', views.MyLoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), {'next_page': '/'}, name = 'logout'),
    path('singup', views.SingUpView.as_view(), name='singup'),
    path('password/reset', views.MyPasswordResetView.as_view(), name="password_reset"),
    path('password/complete', views.MyPasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password/reset/confirm/<str:uidb64>/<str:token>', views.MyPasswordResetConfirmView.as_view(), name = 'password_reset_confirm')
]
