from django.db import models

# Create your models here.

class VacancyModel(models.Model):
  id = models.CharField(max_length=64, primary_key=True)
  name = models.CharField(max_length=64)
  has_test = models.BooleanField(null=True)
  area_id = models.CharField(max_length=64)
  area_name = models.CharField(max_length=64)
  salary_max = models.CharField(max_length=32,null=True)
  salary_min = models.CharField(max_length=32,null=True)
  salary_currency = models.CharField(max_length=32)
  salary_gross = models.BooleanField(null=True)
  type_id = models.CharField(max_length=64,null=True)
  type_name = models.CharField(max_length=64,null=True)
  address_raw = models.CharField(max_length=128,null=True)
  url = models.CharField(max_length=256,null=True)
  alternate_url = models.CharField(max_length=256,null=True)
  snippet_requirement = models.CharField(max_length=2048,null=True)
  snippet_responsibility = models.CharField(max_length=2048,null=True)
  schedule_id = models.CharField(max_length=128,null=True)
  schedule_name = models.CharField(max_length=128,null=True)
  experience_id = models.CharField(max_length=64)
  experience_name = models.CharField(max_length=64)
  employment_id = models.CharField(max_length=64,null=True)
  employment_name = models.CharField(max_length=64,null=True)
  key_skills = models.CharField(max_length=1024,null=True)

  def __str__(self):
    return self.name

