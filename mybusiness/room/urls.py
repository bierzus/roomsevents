from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RoomList, RoomDetail

app_name = 'room'

prefix = 'v1'

urlpatterns = [
    # Business:
    path(f'{prefix}/room', RoomList.as_view(), name='all_rooms'),
    path(f'{prefix}/room/', RoomList.as_view(), name='new_room'),
    path(f'{prefix}/room/<int:pk>', RoomDetail.as_view(), name='get_room'),
    path(f'{prefix}/room/<int:pk>', RoomDetail.as_view(), name='delete_room')
]

urlpatterns = format_suffix_patterns(urlpatterns)
