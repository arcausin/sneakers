from django.urls import path
from . import views

app_name = 'sneakers'
urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('detail/<id>', views.detail_view, name='detail_view'),
    path('create', views.create, name='create'),
    path('update/<id>', views.update_view, name='update_view'),
    path('delete/<id>', views.delete_view, name='delete_view'),
]
