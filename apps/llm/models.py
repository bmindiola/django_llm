import uuid

from django.db import models
from apps.core.models import BaseModel


# Create your models here.
class Conversation(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SenderMessage(models.TextChoices):
    USER = 'user', 'The sender is the user'
    AI = 'ai', 'The sender is the IA'


class ConversationMessage(BaseModel):
    conversation = models.ForeignKey(
        Conversation,
        related_name='messages',
        on_delete=models.CASCADE
    )
    sender = models.CharField(
        max_length=15,
        choices=SenderMessage.choices,
    )
    content = models.TextField()


class Agent(BaseModel):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    token = models.CharField(
        max_length=255,
        default='agent_' + str(uuid.uuid4()),
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name
