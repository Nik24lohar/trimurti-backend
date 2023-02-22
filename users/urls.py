from django.urls import path
from users import views

urlpatterns = [

    path('user/<str:email>',views.userAPIView.as_view()),
    path('',views.UserList.as_view()),
]