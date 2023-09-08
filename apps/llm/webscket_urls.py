from django.urls import path
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/conversation/', consumers.ConversationConsumer.as_asgi()),

    # Websocket URL for a given chat_id
    re_path(r'ws/conversation/(?P<chat_id>\w+)/$', consumers.ConversationConsumer.as_asgi()),
]