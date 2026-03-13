from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ComentarioViewSet

urlpatterns = [

]

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register(r"posts/(?P<post_pk>\d+)/comentarios", ComentarioViewSet, basename="comentario")


urlpatterns += [
    path('api/', include(router.urls))
]