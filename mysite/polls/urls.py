from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),
    path('create/', views.create, name='create_poll'),
    path('detail/<int:poll_id>/comment/', views.comment, name='create_comment'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout')

]