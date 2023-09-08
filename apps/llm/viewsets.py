from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Agent
from .models import Conversation, ConversationMessage
from .serializers import AgentSerializer
from .serializers import ConversationSerializer, ConversationMessageSerializer

from apps.core.viewsets import BaseViewSet


# Create your views here.
class ConversationViewSet(BaseViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        ConversationMessage.objects.filter(chat_id=instance.id).delete()
        instance.delete()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse({"chats": serializer.data})

    @action(detail=True, methods=['get'])
    def messages(self, request, pk=None):
        conversation: Conversation = self.get_object()
        messages = ConversationMessage.objects.filter(chat_id=conversation.id).order_by('date_created')
        serializer = ConversationMessageSerializer(messages, many=True)
        return Response(serializer.data)


class AgentViewSet(BaseViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    lookup_field = 'token'

    def destroy(self, request, *args, **kwargs):
        agent: Agent = self.get_object()
        agent.is_active = False
        agent.save()
        return Response(status=204)

    def update(self, request, *args, **kwargs):
        agent: Agent = self.get_object()
        agent.type = request.data.get('agent_type')
        agent.save()
        return Response(AgentSerializer(agent).data)
