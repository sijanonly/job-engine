from django.db import models
from django.utils.translation import ugettext_lazy as _


class Job(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name=_("title"),
        help_text=_("Enter the job title")
    )
    description = models.TextField(null=True)
    url = models.URLField(max_length=500, blank=True, default='')

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        ordering = ("title",)

    def __str__(self):
        return self.title
