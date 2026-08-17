from django.db import models


class Runer(models.Model):
    username = models.CharField(primary_key=True, max_length=50, db_index=True, null=False)


class Run(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    athlete = models.ForeignKey(Runer, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)
