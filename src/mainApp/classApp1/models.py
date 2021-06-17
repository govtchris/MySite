from django.db import models


class djangoClasses1(models.Model):
    Title = models.CharField(max_length=60, default='', blank=True, null=False)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=100, default="", blank=True, null=False)
    Duration = models.FloatField(default=1, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Title
