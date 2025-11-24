from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('userlog/', views.userlog, name='userlog'),
    path('logindetail/', views.logindetail, name='logindetail'),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('views/',views.view,name="view"),
    path('update/<str:pk>',views.update,name="update"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('detailview/<str:pk>',views.detailview,name="detailview"),
]
