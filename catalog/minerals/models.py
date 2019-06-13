from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255, blank=True)
    image_caption = models.TextField(blank=True)
    category = models.CharField(max_length=255, blank=True)
    formula = models.TextField(blank=True)
    strunz_classification = models.CharField(max_length=255, blank=True)
    color = models.TextField(blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.TextField(blank=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True)
    cleavage = models.CharField(max_length=255, blank=True)
    mohs_scale_hardness = models.CharField(max_length=255, blank=True)
    luster = models.CharField(max_length=255, blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.CharField(max_length=255, blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    crystal_habit = models.TextField(blank=True)
    specific_gravity = models.CharField(max_length=255, blank=True)
    group = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
    