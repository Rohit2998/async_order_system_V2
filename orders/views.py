from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .models import Product  
from .serializers import ProductSerializer 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer