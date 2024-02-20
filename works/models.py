from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Work(models.Model):
    image = models.ImageField(upload_to='images/')
    project_name = models.CharField(max_length=100)
    project_link = models.URLField(_("Project link"), max_length=500, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')
        ordering = ['id']
