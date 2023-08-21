# band/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),

    # Home (login) view
    path('login/', auth_views.LoginView.as_view(template_name='home.html'), name='login'),

    # Logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Explicit login URL
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # Password reset with custom templates and email
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
    ), name='password_reset'),

    # Password reset done
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html',
    ), name='password_reset_done'),

    # Password reset confirm
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
    ), name='password_reset_confirm'),

    # Password reset complete
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),

    # Custom login URL
    path('login/', auth_views.LoginView.as_view(template_name='path/to/login.html'), name='login'),
]
