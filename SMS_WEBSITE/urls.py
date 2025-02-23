
from django.urls import path 
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('logout',views.logout_user, name='logout'),
   path('register',views.register_user, name='register'),
   path('records/<int:pk>/', views.record_detail, name='records'),
   path('delete/<int:pk>/',  views.delete_detail , name='delete'),
   path('add_record',views.add_record, name='add_record'),
   path('update/<int:pk>/',  views.update_record , name='update'),



]