from django.db import models


class ContactRequest(models.Model):
    name = models.CharField(max_length=150)
    business = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    message = models.TextField()

    legal_agreement = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    contacted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} — {self.business or 'No business name'}"