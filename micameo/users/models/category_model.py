from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(
        _("Category"),
        max_length=30,
        unique=True,
        error_messages={
            'unique': _("A category with that name already exist")
        }
    )

    def __str__(self):
        return self.name


class SubCategory(TimeStampedModel):
    sub_name = models.CharField(
        _("Sub category"),
        max_length=30,
        unique=True,
        error_messages={
            'unique': _("A category with that name already exist")
        }
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name
