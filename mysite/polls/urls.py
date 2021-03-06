from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('index2/', views.index2, name='index2'),
    path('booked/', views.booked, name='booked'),

    path('review/<int:shop_area>/', views.review, name='review'),
    path('shop_detail/', views.shop_detail, name='shop_detail'),

    path('booking/<int:shop_area>/', views.booking, name='booking'),

    path('register/', views.register, name='register'),
    path('guide/', views.guide, name='guide'),

    path('profile/', views.profile, name='profile'),


    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),


    path('edit_shop/<int:shop_id>/', views.edit_shop, name='edit_shop'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_pic/', views.edit_pic, name='edit_pic'),

    path('delete/<int:shop_area>/', views.delete_shop, name='delete_shop'),
    path('delete/', views.delete, name='delete'),

    path('adminx/', views.adminx, name='adminx')

]

