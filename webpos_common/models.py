from django.db import models

from webpos_common.utils import get_now


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, help_text="수정 일시")
    deleted_at = models.DateTimeField(null=True, help_text="삭제 일시")

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = get_now()
        super(BaseModel, self).save()
