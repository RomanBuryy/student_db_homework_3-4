from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=256, blank=False)
    leader = models.OneToOneField('Student', blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
