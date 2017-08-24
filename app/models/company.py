from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(null=True, blank=True)
	owner = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class CompanyMember(models.Model):
	company = models.ForeignKey(Company, related_name='Company')
	member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
	date_joined = models.DateTimeField(auto_now=True)

	
	class Meta:
		unique_together = (("company", "member"),)

	def __str__(self):
		return '{}-{}'.format(self.company, self.member.username)

