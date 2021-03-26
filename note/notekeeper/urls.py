
from django.urls import path

from . import views

app_name = 'notekeeper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_new_note', views.create_new_note, name='create_new_note'),
    path('<int:pk>/update', views.update_note, name='update_note'),
    path('<int:pk>/', views.DetailView.as_view(), name='single_note'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit_single_note'),
    path('<int:note_pk>/delete', views.delete_note, name='delete_note')
]