from django.db import models
from django.urls import reverse


class Trip(models.Model):
    MOOD_CHOICES = [
        ('coastal', 'Coastal'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('heritage', 'Heritage'),
        ('wild', 'Wild'),
    ]

    title = models.CharField(max_length=120)
    origin = models.CharField(max_length=80)
    destination = models.CharField(max_length=80)
    tagline = models.CharField(max_length=160)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    start_date = models.DateField()
    days = models.PositiveSmallIntegerField()
    distance_km = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    cover_color = models.CharField(max_length=32, default='#0f766e')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'start_date', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trip_detail', args=[self.pk])

    @property
    def average_daily_distance(self):
        return round(self.distance_km / self.days)


class Stop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='stops')
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=220)
    drive_time = models.CharField(max_length=40)
    overnight = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        unique_together = ['trip', 'order']

    def __str__(self):
        return f'{self.order}. {self.name}'

# Create your models here.
