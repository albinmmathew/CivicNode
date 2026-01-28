from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Categories
class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)
	is_emergency = models.BooleanField(default=False)

	def __str__(self):
		return self.name
	
# Issues
class Issue(models.Model):
	STATUS_CHOICE = (
		('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )

	title = models.CharField(max_length=200)
	description = models.TextField()

	category = models.ForeignKey(Category, on_delete=models.PROTECT)  #Prevents deletion of category if in use
	location = models.CharField(max_length=255)

	created_by = models.ForeignKey(
		User,
		on_delete=models.CASCADE,	#if user is deleted -> all their created records are deleted
		related_name='issues_created'  #allows reverse access
	)

	assigned_to = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,  #on user deletion, beccomes null
		null=True,   #can store NULL
		blank=True,  #optional field
		related_name='issues_assigned'
	)

	status = models.CharField(
		max_length=20,
		choices=STATUS_CHOICE,
		default='PENDING'
	)

	created_at = models.DateTimeField(auto_now_add=True)

	def is_emergency(self):
		return self.category.is_emergency
	
	def __str__(self):
		return self.title