import stripe

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from payment_api import models
from payment_api.models import Item
from payment_api.serializers import ItemSerializer


class ItemViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except models.Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return render(request, template_name='items.html', context={
            'item': serializer.data,
        })
