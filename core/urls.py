from django.urls import path
from .views import frontpage, shop, signup, login

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('shop/', shop, name='shop')
]