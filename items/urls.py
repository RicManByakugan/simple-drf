from django.urls import path
from .views import getAllItems, AddItem, UpdateItem, DeleteItem

urlpatterns = [
    path('items/all', getAllItems, name='getAllItems'),
    path('items/add', AddItem, name='AddItem'),
    path('items/update/<int:id>', UpdateItem, name='UpdateItem'),
    path('items/delete/<int:id>', DeleteItem, name='DeleteItem'),
]