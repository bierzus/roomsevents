from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EventList, EventDetail, CustomerBookList, CustomerBookDetail

app_name = 'event'

prefix = 'v1'

urlpatterns = [
    # Business:
    path(f'{prefix}/event', EventList.as_view(), name='all_events'),
    path(f'{prefix}/event/', EventList.as_view(), name='new_event'),
    path(f'{prefix}/event/<int:pk>', EventDetail.as_view(), name='get_event'),
    path(f'{prefix}/event/<int:pk>', EventDetail.as_view(), name='delete_event'),
    # Customer:
    path(f'{prefix}/event/customer', CustomerBookList.as_view(), name='all_public_events'),
    path(f'{prefix}/event/customer/', CustomerBookList.as_view(), name='new_customer_book'),
    path(f'{prefix}/event/<int:pk>/customer/', CustomerBookDetail.as_view(), name='cancel_customer_book')
]

urlpatterns = format_suffix_patterns(urlpatterns)
