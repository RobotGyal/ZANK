from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import (
    SignUpView,
    UserProfile,
)

app_name = 'accounts'
# include a url pattern for the login Page
# include a url pattewrn for the signup page

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/',
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name="logout"),
    path('<int:pk>/',
         UserProfile.as_view(),
         name="user-profile"),
]
