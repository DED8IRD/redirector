from django.urls import path
from URLshortener import views

app_name = 'URLshortener'
urlpatterns = [
	path('', views.index, name='index'),
	path('links/', views.links, name='links'),
	path('save/<code>/', views.save_link, name='save'),
	path('delete/<int:pk>/', views.delete_link, name='delete'),
	path('<code>/', views.shortened_redirect, name='redirect'),
]
