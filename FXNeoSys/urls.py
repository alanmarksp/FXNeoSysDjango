from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from authentications.views import AuthenticationView

router = DefaultRouter()

router.register(r'authenticate', AuthenticationView, base_name='authentication')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/1.0/', include(router.urls)),
]
