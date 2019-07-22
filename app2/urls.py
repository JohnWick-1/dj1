
from rest_framework import routers
from .views import CountryViewSet


router = routers.SimpleRouter()
router.register(r'country', CountryViewSet)


urlpatterns = router.urls
