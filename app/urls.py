from django.urls import path
from . import views

urlpatterns=[
    path('',views.demo,name='demo'),
    path('user_login',views.user_login,name='user_login'),
    path('hassanmenu',views.hassanmenu,name='hassanmenu'),
    path('commande/', views.commande, name='commande'),
    path('listh/', views.listh, name='listh'),
]