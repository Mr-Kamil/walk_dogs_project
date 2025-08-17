from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'walkers', WalkerViewSet)
router.register(r'walks', WalkViewSet)

urlpatterns = router.urls
