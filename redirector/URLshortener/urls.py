from django.urls import path, include
from rest_framework.routers import DefaultRouter
from URLshortener import views


router = DefaultRouter()
router.register('urls', views.URLViewSet)
router.register('saved_links', views.UserSavedLinkViewSet)

app_name = 'URLshortener'
urlpatterns = [
	path('', views.index, name='index'),
    path('api/', include(router.urls), name='api'),    
	path('links/', views.links, name='links'),
	path('save/<code>/', views.save_link, name='save'),
	path('delete/<int:pk>/', views.delete_link, name='delete'),
	path('<code>/', views.shortened_redirect, name='redirect'),
]
