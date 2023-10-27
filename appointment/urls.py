from django.urls import path,include
from . import views


urlpatterns = [
   # path('', views.index,name ='user_index'),
   path('', views.UserData,name ='user_insert')
    
    
]
 