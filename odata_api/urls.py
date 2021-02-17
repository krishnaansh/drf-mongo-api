from django.conf.urls import url, re_path
from django.urls import path, include
from rest_framework import routers
from odata_api.views import *
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.routers import Route, DynamicRoute


from rest_framework import renderers

product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'get' : 'reterive',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'delete'

})
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, r"tool")

urlpatterns = [
    path("api/", include(router.urls)),
    # path('add-products/', product_list, name='product_list')
]
