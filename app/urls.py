from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
urlpatterns=[
    path("",views.index,name='index'),
    path("js", views.index_js, name="index-js"),

]

router=DefaultRouter()
router.register("api/categories",views.CategoryViewSet,basename="categories")
router.register("api/random_list",views.RandomListViewSet,basename="random_list")

urlpatterns += router.urls