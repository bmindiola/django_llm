from rest_framework.routers import DefaultRouter

from .viewsets import ConversationViewSet, AgentViewSet


def register(router: DefaultRouter):
    router.register(r'conversations', ConversationViewSet)
    router.register(r'agents', AgentViewSet)
