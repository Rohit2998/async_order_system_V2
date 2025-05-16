from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet,ProductViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)  # ✅ Add this line


urlpatterns = [
    path('', include(router.urls)),
    
]