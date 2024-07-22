from django.urls import path, include  # Importa include
from rest_framework import viewsets, routers
from .models import Item, Category, Stock
from .serializers import ItemSerializer, CategorySerializer, StockSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'stocks', StockViewSet)


urlpatterns = [
    path('', include(router.urls)),
]