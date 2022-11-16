from django.urls import path

from app import views


urlpatterns = [
    path('', views.index, name='main'),
    path('hot/', views.hot_handler, name='hot'),
    path('tag/<str:tag_name>/', views.tag_handler, name='tag'),
    path('question/<int:question_id>/', views.question_handler, name='question'),
    path('login/', views.login_handler, name='login'),
    path('signup/', views.signup_handler, name='signup'),
    path('ask/', views.ask_handler, name='ask'),
]