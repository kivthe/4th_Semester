from dataclasses import dataclass

# Area struct
@dataclass
class Area:
  id: int
  name: str
  url: str

# EmployerElement struct
@dataclass
class EmployerElement:
  id: int
  name: str
  url: str
  alternate_url: str
  logo_urls: set
  vacancies_url: str
  open_vacancies: int

# Employer struct
@dataclass
class Employer:
  id: str
  trusted: bool
  accredited_it_employer: bool
  name: str
  type: str
  description: str
  site_url: str
  alternate_url: str
  vacancies_url: str
  logo_urls: set
  relations: set
  area: Area
  industries: set
  branded_description: str
  branding: any
  insider_interviews: set
  open_vacancies: int

# Salary struct
@dataclass
class Salary:
  min: int
  max: int
  currency: str
  gross: bool

# Metro struct
@dataclass
class Metro:
  station_name: str
  line_name: str
  station_id: str
  line_id: str
  lat: float
  lng: float

# Address struct
@dataclass
class Address:
  city: str
  street: str
  building: str
  lat: float
  lng: float
  description: str
  raw: str
  metro: Metro
  metro_stations: set # : Metro
  id: str

# Snipper struct
@dataclass
class Snippet:
  requiremnet: str
  responsibility: str

@dataclass
class IDName:
  id: str
  name: str

# Vacancy struct
@dataclass
class Vacancy:
  id: str
  #premium: bool
  name: str
  #department: any
  hast_test: bool
  #respone_letter_required: bool
  area_id: str
  area_name: str
  salary_min: str
  salary_max:str
  salary_currency: str
  salary_gross: bool
  type_id: str
  type_name: str
  #address: Address
  address_raw: str
  #response_url: str
  #sort_point_distance: any
  #published_at: str
  #created_at: str
  #archived: bool
  #apply_alternate_url: str
  #show_logo_in_search: any
  #insider_interview: any
  url: str
  alternate_url: str
  #relations: set
  #employer: EmployerElement
  snippet_requirement: str
  snippet_responsibility: str
  #contacts: list
  schedule_id: str
  schedule_name: str
  #working_days: set
  #working_time_intervals: set
  #working_time_modes: set
  #accept_temporary: bool
  experience_id: str
  experience_name: str
  employemnt_id: str
  employment_name: str
  #adv_response_url: str
  #is_adv_vacancy: bool
  #adv_context: any
  key_skills: list


