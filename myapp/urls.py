from rest_framework import routers
from myapp.views import Personviewset

router=routers.SimpleRouter()
router.register(r'persons',Personviewset)
urlpatterns=router.urls