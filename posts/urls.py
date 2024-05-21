# url 매핑
# posts > urls.py
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewsets', PostModelViewSet)

app_name = 'posts'

urlpatterns = [
    path('list/', GetAPIView.as_view()),
    path('comment/', PostAPIView1.as_view()),
    #path('post/', PostAPIView.as_view()),
    # path('post/', PostAPIView2.as_view()),
    # path('post/', PostAPI_FBV),
    # path('list/', PostListAPIView.as_view()),
    # path('createOrlist/byMixin/', PostListCreateMixin.as_view()),
    # path('createOrlist/byGeneric/', PostListCreateGeneric.as_view()),
    #path('', include(router.urls)),
]