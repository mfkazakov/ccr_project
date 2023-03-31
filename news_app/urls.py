from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

router.register('news', NewsViewSet, basename='news')

urlpatterns = router.urls
