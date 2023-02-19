from django.urls import path
from app_users import views
from Buddy import settings
from django.conf.urls.static import static


# app_name = 'app_users'
urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.ViewProfile.as_view(), name='profile'),
    path('profile-update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('change_pass/',views.change_pass, name = 'change_pass'),
    path('contact/', views.ContactView.as_view(), name="contact"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)