from django.urls import path 
from .import views

app_name = 'note'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('create/',views.CreateNote.as_view(),name='create'),
    path('delete/<pk>', views.DeletNote.as_view(), name='delete'),
    path('updates/<pk>', views.UpdateNote.as_view(), name='update'),
]
