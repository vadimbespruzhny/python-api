from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=120)
    parameter = models.ForeignKey(
        "Parameter", related_name="parameter", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    parameter_name = models.CharField(max_length=60)
    parameter_type = models.CharField(max_length=60)
    parameter_value = models.IntegerField(null=True)
    user = models.ForeignKey("User", related_name="params",
                             null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.parameter_name
