from django.db import models
from django.conf import settings
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from apps.accounts.utils import get_current_user

class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created_by'
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created_by'
    )

    class Meta:
        abstract = True

    def has_changed(self, field):
        current_value = getattr(self, field)
        previous_model = self.__class__.objects.get(pk=self.pk)
        previous_value = getattr(previous_model, field)
        return current_value != previous_value

    def save(self, *args, **kwargs):
        current_user = get_current_user()
        if current_user and not self.created_by:
            self.created_by = current_user
        elif current_user and self.deleted_by and self.has_changed('deleted_at'):
            self.deleted_by = current_user
        super().save(*args, **kwargs)