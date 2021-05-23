from django.db import models

# Create your models here.
class BaseModel(models.Model):

    

    class Meta:
        verbose_name = _("BaseModel")
        verbose_name_plural = _("BaseModels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BaseModel_detail", kwargs={"pk": self.pk})
