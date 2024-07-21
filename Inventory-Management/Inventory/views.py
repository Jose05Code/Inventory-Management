from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item

# Item
class ItemView(APIView):
    def get(self, request, item_id=None):
        '''List all items if item_id is None, else show item details'''
        if item_id:
            try:
                item = Item.objects.get(id=item_id)
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        '''Create a new item'''
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, item_id=None):
        if not item_id:
            return Response({'error': 'Method PUT not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id=None):
        if not item_id:
            return Response({'error': 'Method DELETE not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

    