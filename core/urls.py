from django.urls import path
from .views import frontpage, shop

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop')
]