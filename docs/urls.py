from django.urls import path
from .views import createDocs, listDocs, updateDocs, deleteDocs

urlpatterns = [
    path('', listDocs, name='listDocs'),
    path('new', createDocs, name='createDocs'),
    path('update/<int:id>', updateDocs, name='updateDocs'),
    path('delete/<int:id>', deleteDocs, name='deleteDocs')
]
