from rest_framework import serializers

from apps.core.models import BaseModel


class BaseSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BaseModel
        abstract = True
        exclude = (
            'date_created',
            'date_modified'
        )