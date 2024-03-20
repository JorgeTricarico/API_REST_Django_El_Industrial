from django.urls import path, include
from rest_framework import routers
from producto import views
from producto import views
#urlpatterns = []

router = routers.DefaultRouter()

router.register(r'producto', views.ProductoViewSet, 'producto')
router.register(r'productos-scraping', views.ProductoScrapingViewSet, 'productos-scraping')

urlpatterns = [
    path('', include(router.urls)),
    path('productos-scraping/', views.ProductoScrapingViewSet.as_view({'post': 'create'}), name='productos-scraping'),
    path('productos-scraping/', views.ProductoScrapingViewSet.as_view({'get': 'list'}), name='productos-scraping'),
]

