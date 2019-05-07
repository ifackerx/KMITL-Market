from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('index2/', views.index2, name='index2'),
    path('booked/', views.booked, name='booked'),

    path('review/<int:shop_area>/', views.review, name='review'),
    path('shop_detail/', views.shop_detail, name='shop_detail'),

    path('booking/<int:shop_area>/', views.booking, name='booking'),

    path('register/', views.register, name='register'),


    path('profile/', views.profile, name='profile'),

    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),

    path('create/', views.create, name='create_poll'),
    path('detail/<int:poll_id>/comment/', views.comment, name='create_comment'),

    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),

    path('update/<int:poll_id>', views.update, name='update_poll'),
    path('<int:question_id>/add-choice/', views.add_choice, name='add_choice'),
    path('api/<int:question_id>/add-choice/', views.add_choice_api, name='add_choice_api'),

    path('edit_shop/<int:shop_id>/', views.edit_shop, name='edit_shop'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('delete/<int:shop_area>/', views.delete_shop, name='delete_shop'),
    path('delete/', views.delete, name='delete')

]

