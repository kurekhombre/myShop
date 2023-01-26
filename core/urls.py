from django.urls import path
from .views import frontpage, shop, sign_up, log_in
from django.contrib.auth import views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', sign_up, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('login/', log_in, name='login'),
    path('shop/', shop, name='shop')
]