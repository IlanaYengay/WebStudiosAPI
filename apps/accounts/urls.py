from rest_framework.routers import DefaultRouter
from .views import CustomUserView


router = DefaultRouter()

router.register('users', CustomUserView, basename='users')

urlpatterns = router.urls