from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.llm import urls as llm_urls

router = DefaultRouter()
llm_urls.register(router)

urlpatterns = [
    path('v1/', include(router.urls)),
]
