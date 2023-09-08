import uuid

from django.db import models
from django.utils.timezone import now


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.date_modified = now()
        return super(BaseModel, self).save(force_insert, force_update, using, update_fields)
