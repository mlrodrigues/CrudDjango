from django.db import models

class Companies(models.Model):
	name = models.CharField(max_length=256)
	created_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)
	last_update_at = models.DateTimeField((""), auto_now=True, auto_now_add=False)
	locale = models.CharField( max_length=50, default="-03:00")
	lang = models.CharField(max_length=5, default="pt")

	created_by = models.OneToOneField("users.Users", on_delete=models.CASCADE, related_name="%(class)s_users")
	users = models.ManyToManyField("users.Users")

	def __str__(self) -> str:
		return self.name