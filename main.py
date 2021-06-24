import jsonparse
import re

strs=jsonparse.strs
str=strs[3]
strset=[]
value=[]
str=str.replace(" ","")
print(str)
print()
def lookstr(str):
  m=re.search("\"[0-9A-Za-z]*\"",str)
  #print(m.group())
  return m.group()

def lookvalue_str(str):
  m=re.search("\:\"*[0-9A-Za-z]*\"*",str)
  #print(m.group())
  return m.group()

def lookvalue_empty(str):
  m=re.search("\:\{\}",str)
  #print(m.group())
  return m.group()

def lookvalue_emptylist(str):
  m=re.search("\:\[\]",str)
  return m.group()

def lookvalue_list(str):
  m=re.search("\:\[[0-9,]*\]|\:\[[\"0-9a-zA-Z,]*\"]*\]|\:\[[true|false|,]*\]",str)
  return m.group()

def lookvalue_numeric(str):
  m=re.search("\:[0-9]*",str)
  return m.group()

def lookvalue_boolean(str):
  m=re.search("\:true|\:false",str)
  return m.group()

def lookvalue(str):
  if(str[str.find(":")+1]=='{'):
    if(str[str.find(":")+2]=='}'):
      return lookvalue_empty(str)
    else:
      m=re.search("\:\{[\"0-9A-Za-z,:]*\}",str)
      return m.group()

  elif (str[str.find(":")+1]=='"'):
    return lookvalue_str(str)

  elif(str[str.find(":")+1]=='['):
    if(str[str.find(":")+2]==']'):
      return lookvalue_emptylist(str)
    else:
      return lookvalue_list(str)

  elif (str[str.find(":")+1].isnumeric()):
    return lookvalue_numeric(str)

  elif("true" in str[str.find(":")+1:str.find(":")+6] or "false" in str[str.find(":")+1:str.find(":")+6]):
    return lookvalue_boolean(str)

for i in range(str.count(',')+1):
  try:
    strset.append(lookstr(str))
    str=str.replace(lookstr(str),"",1)
    #looksemicolon(str)
    value.append(lookvalue(str))
    str=str.replace(lookvalue(str),"",1)
  except AttributeError:
    break
  '''
  print(strset)
  print()
  print(value)
  print()
  print(str)
  print()
  '''
  str=str.replace(',',"",1)

print("String Tag in JSON:")
print(strset)
print()
print("Values in JSON:")
print(value)

