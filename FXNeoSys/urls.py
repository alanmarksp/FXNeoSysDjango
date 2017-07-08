from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from authentications.views import AuthenticationView
from traders.views import TraderView
from trading_accounts.views import TradingAccountView

router = DefaultRouter()

router.register(r'authentications', AuthenticationView, base_name='authentications')
router.register(r'traders', TraderView, base_name='traders')
router.register(r'trading_accounts', TradingAccountView, base_name='trading_accounts')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/1.0/', include(router.urls)),
]
