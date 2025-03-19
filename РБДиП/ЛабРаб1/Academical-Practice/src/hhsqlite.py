from django.db.utils import OperationalError
from main.models import VacancyModel
from src import hhtypes

#--------------------------------------------------

def CreateVacancyRecord(vacancy=hhtypes.Vacancy) -> None:
  skills_string = ''
  if vacancy.key_skills:
    for skill in vacancy.key_skills:
      skills_string = skills_string + skill + ", "
  new_record = VacancyModel(id=vacancy.id,
                            name=vacancy.name,
                            has_test=vacancy.hast_test,
                            area_id=vacancy.area_id,
                            area_name=vacancy.area_name,
                            salary_max=vacancy.salary_max,
                            salary_min=vacancy.salary_min,
                            salary_currency=vacancy.salary_currency,
                            salary_gross=vacancy.salary_gross,
                            type_id=vacancy.type_id,
                            type_name=vacancy.type_name,
                            address_raw=vacancy.address_raw,
                            url=vacancy.url,
                            alternate_url=vacancy.alternate_url,
                            snippet_requirement=vacancy.snippet_requirement,
                            snippet_responsibility=vacancy.snippet_responsibility,
                            schedule_id = vacancy.schedule_id,
                            schedule_name = vacancy.schedule_name,
                            experience_id=vacancy.experience_id,
                            experience_name=vacancy.experience_name,
                            employment_id=vacancy.employemnt_id,
                            employment_name=vacancy.employment_name,
                            key_skills=skills_string)
  new_record.save()

#--------------------------------------------------

def CheckVacancyModelExistence() -> bool:
    try:
        VacancyModel.objects.exists()
        return True
    except OperationalError:
        return False

#--------------------------------------------------

def GetVacancyRecordsCount() -> int:
   return VacancyModel.objects.count()

#--------------------------------------------------

def GetVacancyFromModel(primary_key: str) -> hhtypes.Vacancy:
  if not CheckVacancyModelExistence(): return hhtypes.Vacancy()
  try:
    object = VacancyModel.objects.get(pk=primary_key)
    vacancy = hhtypes.Vacancy
    vacancy.id = object.id
    vacancy.name = object.name

    vacancy.area_id = object.area_id
    vacancy.area_name = object.area_name

    vacancy.salary_max = object.salary_max
    vacancy.salary_min = object.salary_min
    vacancy.salary_currency = object.salary_currency
    vacancy.salary_gross = object.salary_gross

    vacancy.type_id = object.type_id
    vacancy.type_name = object.type_name

    vacancy.address_raw = object.address_raw

    vacancy.url = object.url
    vacancy.alternate_url = object.alternate_url

    vacancy.snippet_requirement = object.snippet_requirement
    vacancy.snippet_responsibility = object.snippet_responsibility

    vacancy.schedule_id = object.schedule_id
    vacancy.schedule_name = object.schedule_name

    vacancy.experience_id = object.experience_id
    vacancy.experience_name = object.experience_name

    vacancy.employemnt_id = object.employment_id
    vacancy.employment_name = object.employemnt_name

    return vacancy

  except VacancyModel.DoesNotExist:
    return hhtypes.Vacancy()
  
#--------------------------------------------------

def PrintAllVacancies() -> None:
   all = VacancyModel.objects.all()
   for item in all:
    print(item.id, item.name, item.area_name, item.salary_max, item.salary_currency, item.experience_name, item.alternate_url)