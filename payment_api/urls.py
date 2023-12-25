from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register('item', ItemViewSet, 'item')


urlpatterns = router.urls
