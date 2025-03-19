import socket
import json
import requests

#--------------------------------------------------

refresh_request = 'refresh/'
get_request = 'query/'

#--------------------------------------------------

def CanConnect(address: str, port: int):
  sock = socket.socket()
  try:
    sock.connect((address, port))
    return True
  except:
    return False
  finally:
    sock.close()

#--------------------------------------------------

def GetDataFromServer(address: str, port: int, filter):
  if not CanConnect(address, port):
    return list()
  address_str = 'http://' + address + ':' + str(port) + '/' + get_request
  '''
  filter = {
    'salary_min':'0',
    'salary_max':'10000000',
    'salary_currency':'RUR',
    'experience_id':'noExperience',
    'area_id':'1'
  }
  '''
  json_string = json.dumps(filter)
  response = requests.get(address_str,data=json_string,headers={'Content-Type': 'application/json'})
  if response.status_code != 200:
    return list()
  try:
    json_data = json.loads(response.text)
    return json_data
  except json.JSONDecodeError:
    return list()

#--------------------------------------------------

def RefreshServerData(address: str, port: int):
  if not CanConnect(address, port): return {'status':'failure'}
  address_str = "http://{}:{}/{}".format(address,port,refresh_request) #'http://' + address + ':' + str(port) + '/' + refresh_request
  response = requests.get(address_str)
  return json.loads(response.text)

#--------------------------------------------------


