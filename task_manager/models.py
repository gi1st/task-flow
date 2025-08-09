from django.db import models
from django.core.exceptions import ValidationError


class Position(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude=exclude)
        if (
            Position.objects.filter(name__iexact=self.name)
            .exclude(pk=self.pk)
            .exists()
        ):
            raise ValidationError(
                {"name": "This name must be unique (case-insensitive)."}
            )

    def __str__(self):
        return self.name
