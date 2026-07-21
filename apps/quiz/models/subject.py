from django.db import models
from django.utils.text import slugify 

from apps.core.models import TimeStampedModel

class Subject(TimeStampedModel):
    """
    Represents a broad subject such as Python, Django, PostgreSQL, etc.
    """
    class Theme(models.TextChoices):
        BLUE = "blue", "Blue"
        GREEN = "green", "Green"
        YELLOW = "yellow", "Yellow"
        ORANGE = "orange", "Orange"
        PURPLE = "purple", "Purple"
        RED = "red", "Red"

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional icon name (e.g. python, database, django)"
    )
    theme = models.CharField(
        max_length=20,
        choices=Theme.choices,
        default=Theme.BLUE,
        help_text="Theme name for UI"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Subject"  # human-readable, descriptive name for a model field
        verbose_name_plural = "Subjects"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name