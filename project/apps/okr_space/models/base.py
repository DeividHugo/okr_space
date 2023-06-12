from django.db import models
from django.conf import settings
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from apps.accounts.utils import get_current_user

class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def has_changed(self, field):
        current_value = getattr(self, field)
        previous_model = self.__class__.objects.get(pk=self.pk)
        previous_value = getattr(previous_model, field)
        return current_value != previous_value
