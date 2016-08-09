from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Pin
from .serializers import PinSerializer
from rest_framework.decorators import api_view

# API
@login_required
@api_view(['GET', 'POST'])
def AllPins(request):

   if request.method == 'GET':
        pins = Pin.objects.all().order_by('-updated_on')
        serialiser = PinSerializer(pins, many=True)
        return Response(serialiser.data)

   elif request.method == 'POST':

        serialiser = Pin(data = request.data)
        if serialiser.is_valid:
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['DELETE', 'PUT'])
def Pin_update(request, id):

    selected_pin = None
    try:
        selected_pin = Pin.objects.all().get(pk=id)
    except selected_pin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        selected_pin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = PinSerializer(selected_pin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def TrendingPins(request, k):

    if request.method == 'GET':
        qualified_pins = Pin.objects.all().order_by('-likes')
        qualified_pins = qualified_pins[:k]
        serializer = PinSerializer(qualified_pins, many=True)
        return Response(serializer.data)



