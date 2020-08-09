from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# Utils models
from model_utils.models import TimeStampedModel


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        error_messages={
            'unique': _('A user with that email already exist')
        }
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.username


class BaseUser(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=_('Phone number must be entered in the format: +9999999. Up to 10-15 digits allowed')
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    profile_image = models.URLField(_("Your profile photo"), blank=True)
    birthday = models.DateField(_("Day of Birthday"), null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = self.user.username
        super(BaseUser, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
