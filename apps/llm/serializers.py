from .models import Conversation, ConversationMessage, Agent
from apps.core.serializers import BaseSerializer


class ConversationSerializer(BaseSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'name', 'created_at', 'updated_at']


class ConversationMessageSerializer(BaseSerializer):
    class Meta:
        model = ConversationMessage
        fields = ['id', 'content', 'chat', 'sender', 'timestamp']


class AgentSerializer(BaseSerializer):
    class Meta:
        model = Agent
        fields = ['name', 'agent_type', 'token', 'created_at', 'updated_at', 'is_active']
