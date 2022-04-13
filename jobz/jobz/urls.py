from django.urls import include, path
from rest_framework import routers
from service.views import ServiceViewSet
from user.views import UserViewSet, ProviderViewSet
from search.views import OccupationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from schedule.views import ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'service', ServiceViewSet)
router.register(r'user', UserViewSet)
router.register(r'provider', ProviderViewSet)
router.register(r'occupation', OccupationViewSet)
router.register(r'schedule', ScheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('authentication.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]