from django.urls import path
from product import views

urlpatterns = [

    path('product',views.ProductListCreate.as_view()),
    path('product/<int:id>',views.ProductUpdateDelete.as_view()),
    path('card',views.CardListCreate.as_view()),
    path('card/<int:id>',views.CardUpdateDelete.as_view()),
]