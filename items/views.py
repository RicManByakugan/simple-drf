from django.shortcuts import render
from .models import Items
from .serializers import ItemSerializers, CreateItemDTO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def getAllItems(request):
    try:
        items = Items.objects.all()
        serializer = ItemSerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def AddItem(request):
    try:
        data = CreateItemDTO(data=request.data)
        data.is_valid(raise_exception=True)
        item = Items.objects.create(**data.validated_data)
        serializer = ItemSerializers(item)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def UpdateItem(request, id):
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CreateItemDTO(item, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteItem(request, id):
    try:
        item = Items.objects.get(id=id)
        item.delete()
        return Response({"status": "success", "data": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Items.DoesNotExist:
        return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_404_NOT_FOUND)