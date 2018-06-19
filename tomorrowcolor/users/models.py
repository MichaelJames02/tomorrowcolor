from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class Company(models.Model):
	company_name = models.CharField(max_length=20)
	company_location = models.CharField(max_length=20)
	number_of_employees = models.IntegerField() 
	employees_avarage_salary = models. BigIntegerField()
	created_day_and_time = DateTimeField(auto_now=True)

	class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

	def __str__(self):
		return self.company_name
