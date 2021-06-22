import jsonparse
import re

strs=jsonparse.strs
str=strs[3]
strset=[]
value=[]
str=str.replace(" ","")
print(str)

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

def lookvalue(str):
  if(str[str.find(":")+1]=='{'):
    if(str[str.find(":")+2]=='}'):
      return lookvalue_empty(str)
  elif (str[str.find(":")+1]=='"'):
    return lookvalue_str(str)
  else:
    lookstr(str)
    lookvalue(str)
#str2=str2.replace(lookstr(str2),"")


for i in range(str.count(',')+1):
  strset.append(lookstr(str))
  str=str.replace(lookstr(str),"")
  #looksemicolon(str)
  value.append(lookvalue(str))
  str=str.replace(lookvalue(str),"")

  print(strset)

  print(value)

  print(str)

  str=str.replace(',',"",1)



