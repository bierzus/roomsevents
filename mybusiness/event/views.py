from .models import Event, CustomerBook
from .serializers import EventSerializer, CustomerBookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class EventList(APIView):
    """
    List all events, or create a new event.
    """

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete a event instance.
    """

    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerBookList(APIView):
    """

    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Only public type!!
        """
        event = Event.objects.filter(type=1)
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerBookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerBookDetail(APIView):
    """

    """

    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return CustomerBook.objects.get(pk=pk)
        except CustomerBook.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        custom_book = self.get_object(pk)
        custom_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

