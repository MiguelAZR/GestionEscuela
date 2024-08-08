from rest_framework.routers import DefaultRouter
from users.api.views import (
    UserApiViewSet
)


router_users = DefaultRouter()
router_users.register(
    prefix="usuarios", basename="users", viewset=UserApiViewSet
)
