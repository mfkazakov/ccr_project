from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

router.register('remarkable_places', UploadRemarkablePlacesViewSet, basename='remarkable_places')

urlpatterns = router.urls

