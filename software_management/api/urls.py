from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'software_management'
router = NetBoxRouter()
router.register('software-version', views.SoftwareVersionViewSet)
urlpatterns = router.urls