from django.db import models

class Users(models.Model):
	email = models.CharField(max_length=256, default="")
	last_password_redefinition = models.DateTimeField((""), auto_now=True, auto_now_add=False)
	email_verified = models.BooleanField(default=False)
	password = models.CharField(max_length=256)
	created_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)
	last_update_at = models.DateTimeField((""), auto_now=True, auto_now_add=False)


	def __str__(self) -> str:
		return self.email