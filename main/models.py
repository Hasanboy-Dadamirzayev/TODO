from django.db import models

class Todo(models.Model):
    nom = models.CharField(max_length=255)
    batafsil = models.TextField(null=True, blank=True)
    y_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
