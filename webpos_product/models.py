from django.db import models

from webpos_common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=128, help_text="이름")
    price = models.IntegerField(default=0, help_text="가격")

    def __str__(self):
        return f"#{self.id} {self.name}"

