from django.contrib import admin
from django.urls import path
from . import views

app_name="food"
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:item_id>/',views.detail,name='detail'),
    path('add_item/',views.add_item,name="add_item"),
    path('update_item/<int:item_id>/',views.update_item,name="update_item"),
    path('delete_item/<int:item_id>/',views.delete_item,name='delete_item')

]
