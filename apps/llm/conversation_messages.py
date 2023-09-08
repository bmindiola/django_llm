import os
from typing import List

import django
from channels.db import database_sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from .models import ConversationMessage


class ConversationMessageRepository:

    @database_sync_to_async
    def get_chat_messages(self, chat_id: str, order_by='timestamp') -> List[ConversationMessage]:
        # Retrieve the chat history for `chat_id` from the database
        return list(ConversationMessage.objects.filter(chat_id=chat_id).order_by(order_by))

    @database_sync_to_async
    def save_message(self, message: str, sender: str, chat_id: str):
        # Save the message to the database
        ConversationMessage.objects.create(sender=sender, content=message, chat_id=chat_id)
