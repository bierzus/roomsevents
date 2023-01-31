from .models import Room
from .serializers import RoomSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from event.models import Event


class RoomList(APIView):
    """
    List all rooms, or create a new room.
    """

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetail(APIView):
    """
    Retrieve, update or delete a room instance.
    """

    permission_classes = [permissions.IsAdminUser]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        room = self.get_object(pk)
        events = Event.objects.filter(room=room)
        if not events:
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
