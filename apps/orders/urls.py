from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ImageViewSet


router = DefaultRouter()

router.register(r'orders', OrderViewSet)
router.register(r'images', ImageViewSet)


urlpatterns = router.urls