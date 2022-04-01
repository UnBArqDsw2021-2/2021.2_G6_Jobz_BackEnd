from django.urls import include, path
from rest_framework import routers
from service.views import ServiceViewSet
from user.views import UserViewSet, ProviderViewSet
from search.views import OccupationViewSet

router = routers.DefaultRouter()
router.register(r'service', ServiceViewSet)
router.register(r'user', UserViewSet)
router.register(r'provider', ProviderViewSet)
router.register(r'occupation', OccupationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]