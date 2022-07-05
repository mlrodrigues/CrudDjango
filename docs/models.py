from django.db import models

class Docs(models.Model):
	nome = models.CharField(max_length=256)
	deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField((""), auto_now=False, auto_now_add=True)
	last_update_at = models.DateTimeField((""), auto_now=True, auto_now_add=False)
	date_limit_to_sign = models.DateTimeField()
	signed = models.BooleanField(default=False)

	company = models.ForeignKey("companies.Companies", on_delete=models.CASCADE)
	user = models.ForeignKey("users.Users", on_delete=models.CASCADE, related_name="%(class)s_users")
	

	def __str__(self) -> str:
		return self.nome