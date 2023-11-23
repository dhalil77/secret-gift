from django.urls import path
from . import views

urlpatterns = [
    # ............ FOR VIEWS .........
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('participation/', views.participation, name='participation'),
    path('secrets/', views.secrets, name='secrets'),
    # path('signout/', views.signout, name='signout'),

]