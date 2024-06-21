from django.urls import path
from . import views
from .views import register_view, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('add_project/', views.add_project, name='add_project'),
    path('add_portfolio/', views.portfolio_view, name='add_portfolio'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
