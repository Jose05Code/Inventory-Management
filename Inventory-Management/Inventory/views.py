from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class Item_List_View(APIView):
    '''List all items or create a new item'''
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Item_Detail_View(APIView):
    '''Retrieve, update or delete an item'''
    
    def _get_item(self, item_id):
        '''Retrieve an item or return 404'''
        return get_object_or_404(Item, id=item_id)
    
    def get(self, request, item_id=None):
        item = self._get_item(item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, item_id=None):
        item = self._get_item(item_id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, item_id=None):
        item = self._get_item(item_id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)