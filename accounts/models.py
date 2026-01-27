from django.db import models

from django.contrib.auth.models import User
# Create your models here.

#Uses default User model with Extra fields
class Profile(models.Model):
	ROLE_CHOICES = (
		(1, 'Citizen'),
		(2, 'Staff'),
		(3, 'Admin'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

	phone = models.CharField(max_length=15, blank=True)
	address = models.TextField(blank=True)

	def __str__(self):
		return f"{self.user.username} - {self.get_role_display()}"  