from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register('buy', ItemViewSet, 'buy')

urlpatterns = router.urls
