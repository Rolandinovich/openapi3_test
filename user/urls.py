from django.conf.urls import url
from django.urls import re_path, path

from rest_framework.routers import DefaultRouter, SimpleRouter, Route

from user.views import UserViewSet

router = DefaultRouter()


class UserRetrieveRouter(SimpleRouter):
    routes = [
        Route(url=r'^{prefix}/$',
              mapping={'get': 'retrieve',
                       'put': 'update',
                       'patch': 'update'},
              name='{basename}-detail',
              detail=True,
              initkwargs={'suffix': 'Detail'}),
    ]


user_router = UserRetrieveRouter()
user_router.register(r'user', UserViewSet, basename='user_info')
urlpatterns = user_router.urls
