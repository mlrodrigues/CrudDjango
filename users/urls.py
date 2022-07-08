from django.urls import path
from .views import listUsers, createUsers, updateUsers, deleteUsers

urlpatterns = [
    path('', listUsers, name='listUsers'),
    path('new', createUsers, name='createUsers'),
    path('update/<int:id>', updateUsers, name='update_Users'),
    path('delete/<int:id>', deleteUsers, name='deleteUsers')
]
