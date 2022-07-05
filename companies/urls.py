from django.urls import path
from .views import listCompanies, createCompanies, updateCompanies, deleteCompanies

urlpatterns = [
    path('', listCompanies, name='listCompanies'),
    path('new', createCompanies, name='createCompanies'),
    path('update/<int:id>', updateCompanies, name='updateCompanies'),
    path('delete/<int:id>', deleteCompanies, name='deleteCompanies')
]
