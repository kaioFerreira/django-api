from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import AcompanhamentoViewSet
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'acompanhamento100', AcompanhamentoViewSet.get, basename='acompanhamento')


urlpatterns = [
    # url(r'^', include(router.urls), name='acompanhamento'),
    path('acompanhamento100/', AcompanhamentoViewSet.get , name='acompanhamento-get'),
    path('acompanhamentopost/', AcompanhamentoViewSet.post , name='acompanhamento-set'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
