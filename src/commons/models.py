from django.db import models
from model_utils.models import SoftDeletableModel, UUIDModel


class AbstractModel(SoftDeletableModel, UUIDModel, models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
