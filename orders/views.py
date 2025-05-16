from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .models import Product  # Already imported
from .serializers import ProductSerializer  # Add this import

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer