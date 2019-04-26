from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('index2/', views.index2, name='index2'),
    path('review/<int:shop_area>', views.review, name='review'),

    path('detail/<int:poll_id>/', views.detail, name='poll_detail'),
    path('create/', views.create, name='create_poll'),
    path('detail/<int:poll_id>/comment/', views.comment, name='create_comment'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('update/<int:poll_id>', views.update, name='update_poll'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('<int:question_id>/add-choice/', views.add_choice, name='add_choice'),
    path('api/<int:question_id>/add-choice/', views.add_choice_api, name='add_choice_api')
]