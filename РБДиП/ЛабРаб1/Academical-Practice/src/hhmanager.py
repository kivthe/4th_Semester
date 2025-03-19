import requests
from src import hhtypes
import copy

#--------------------------------------------------

hhvacancies = 'http://api.hh.ru/vacancies'
hhemployers = 'http://api.hh.ru/employers'
hhareas     = 'http://api.hh.ru/areas'

#--------------------------------------------------

# Vacancy key skills collection skills
# Pros: More information
# Cons: More response time and routing

collect_key_skills = True

#--------------------------------------------------
def GetVacancyCount(self) -> int:
  response = requests.get(hhvacancies)
  if response.ok:
    return response.json().get('found')
  else:
    return -1
#--------------------------------------------------
def GetEmployerCount(self) -> int:
  response = requests.get(hhemployers)
  if response.ok:
    return response.json().get('found')
  else:
    return -1
#--------------------------------------------------

def SetVacancyAreaIf(vacancy, json_data) -> None:
  if json_data['area'] is not None:
    vacancy.area_id   = json_data['area']['id']
    vacancy.area_name = json_data['area']['name']
#--------------------------------------------------

def SetVacancySalaryIf(vacancy, json_data) -> None:
  if json_data['salary'] is not None:
    vacancy.salary_min = json_data['salary']['from']
    vacancy.salary_max = json_data['salary']['to']
    vacancy.salary_currency = json_data['salary']['currency']
    vacancy.salary_gross = json_data['salary']['gross']

#--------------------------------------------------

def SetVacancyTypeIf(vacancy, json_data) -> None:
  if json_data['type'] is not None:
    vacancy.type_id = json_data['type']['id']
    vacancy.type_name = json_data['type']['name']

#--------------------------------------------------

def SetVacancyAddrIf(vacancy, json_data) -> None:
  if json_data['address'] is not None:
    vacancy.address_raw = json_data['address']['raw']

#--------------------------------------------------

def SetVacancySnippetIf(vacancy, json_data) -> None:
  if json_data['snippet'] is not None:
    vacancy.snippet_requirement = json_data['snippet']['requirement']
    vacancy.snippet_responsibility = json_data['snippet']['responsibility']

#--------------------------------------------------

def SetVacancyScheduleIf(vacancy, json_data) -> None:
  if json_data['schedule'] is not None:
    vacancy.schedule_id = json_data['schedule']['id']
    vacancy.schedule_name = json_data['schedule']['name']

#--------------------------------------------------

def SetVacancyExperienceIf(vacancy, json_data) -> None:
  if json_data['experience'] is not None:
    vacancy.experience_id   = json_data['experience']['id']
    vacancy.experience_name = json_data['experience']['name']

#--------------------------------------------------

def SetVacancyEmploymentIf(vacancy, json_data) -> None:
  if vacancy['employment'] is not None:
    vacancy.employemnt_id = json_data['employment']['id']
    vacancy.employment_name = json_data['employment']['name']

#--------------------------------------------------

def GetVacancies() -> list[hhtypes.Vacancy]:
  response = requests.get(hhvacancies)
  if not response.ok: return list()
  pages_count = response.json().get('pages')
  # Hard-coded limiter to how many pages the program can request
  pages_count //= 10
  vacancies = list()
  for i in range(pages_count):
    # Get parameters from a specific page
    params = {'page' : i}
    response = requests.get(hhvacancies,params=params)
    if not response.ok: break
    json_file = response.json()
    # Parse each vacancy items in the list of received vacancies from the page
    for vacancy_data in json_file['items']:
      vacancy = hhtypes.Vacancy
      vacancy.id = vacancy_data['id']
      vacancy.name = vacancy_data['name']
      vacancy.hast_test = vacancy_data['has_test']
      SetVacancyAreaIf(vacancy, vacancy_data)
      SetVacancySalaryIf(vacancy, vacancy_data)
      SetVacancyTypeIf(vacancy, vacancy_data)
      SetVacancyAddrIf(vacancy, vacancy_data)
      vacancy.url = vacancy['url']
      vacancy.alternate_url = vacancy['alternate_url']
      SetVacancySnippetIf(vacancy, vacancy_data)
      SetVacancyScheduleIf(vacancy, vacancy_data)
      SetVacancyExperienceIf(vacancy, vacancy_data)
      SetVacancyEmploymentIf(vacancy, vacancy_data)
      vacancy.key_skills = list()
      if vacancy.url and collect_key_skills:
        response = requests.get(vacancy.url)
        if response.ok:
          file = response.json()
          for skill in file['key_skills']:
            vacancy.key_skills.append(skill['name'])
            #print(skill['name'])
      vacancies.append(copy.deepcopy(vacancy))
  return vacancies
#--------------------------------------------------

def CheckFilterJson(json_data) -> bool:
  return (json_data['salary_min'] is not None) and (json_data['salary_max'] is not None) and (json_data['salary_currency'] is not None) and (json_data['area_id'] is not None) and (json_data['expereince_id'] is not None)

#--------------------------------------------------