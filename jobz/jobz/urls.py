from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from service.views import ServiceViewSet
from user.views import UserViewSet, ProviderViewSet, ProviderList
from search.views import OccupationViewSet
from provider_presentation.views import ProviderPresentationViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from schedule.views import ScheduleViewSet
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"service", ServiceViewSet)
router.register(r"user", UserViewSet)
router.register(r"provider", ProviderViewSet)
router.register(r"occupation", OccupationViewSet)
router.register(r"providerPresentation", ProviderPresentationViewSet)
router.register(r"schedule", ScheduleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("authentication.urls")),
    path('provider/<str:name>/<int:occupation>', ProviderList.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
