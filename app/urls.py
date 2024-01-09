from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('editTask/<str:pk>',views.editTask,name='editTask'),
    path('makeComplete/<str:pk>',views.makeComplete,name='makeComplete'),
    path('deleteTask/<str:pk>',views.deleteTask,name='deleteTask'),
    path('markAsComplete/<str:pk>',views.markAsComplete,name='markAsComplete')
    
    
]
