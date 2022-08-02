from django.db import models
from django.contrib.auth.models import User

class DocFile(models.Model):
    name = models.CharField(max_length=20)
    docfile = models.FileField()
    version = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '?v' + str(self.version)