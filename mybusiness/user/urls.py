from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

app_name = 'user'

router = routers.DefaultRouter()
router.register(r'v1/users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
