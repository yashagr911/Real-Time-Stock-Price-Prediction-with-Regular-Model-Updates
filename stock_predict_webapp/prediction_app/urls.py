from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_stock_prices, name='predict_stock_prices'),
]
