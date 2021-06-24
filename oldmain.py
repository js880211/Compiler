'''
************
Deprecated last edited at 2021/6/24
************
Switcher=0
StringFlag=0
ValueFlag=0
DataList=[]
json='{ "String1" : "1" ,"String2":2,"String3":"3","String4":4 }'

def getString(json,i):
    String=""
    while(1):
        if(json[i]=='"'):
            #print(String+" : String")
            DataList.append(String)
            String=""
            break
        String+=json[i]
        i=i+1

def blank():
  pass

def getValueString(json,i):
  value=""
  IsString=0
  while(1):
    if(json[i]==' '):
      blank()
    elif(json[i]=='"'):
      IsString=1
    elif(json[i]=='}' or json[i]==','):
      if(IsString==0):
        if(value.isnumeric()):
          value=int(value)
          #print(str(value)+" : value")
          DataList.append(value)
      elif(IsString==1):
        DataList.append(value)
      break
  
    #print(value+" : value")
    if(json[i]==" "):
      blank()
    else:
      value+=json[i]
    i+=1

def getValueNumber(json,i):
  pass


for i in range(0,len(json)):
    if(json[i]=='"' and StringFlag==0):
        getString(json,i+1)
        print("getstr")
        StringFlag=1
    if (json[i]==" "):
      blank()
    if(json[i]==":" and ValueFlag==0):
        getValueString(json,i+1)
        ValueFlag = 1
        print("getvalue")
    if(json[i]==","):
      ValueFlag = 0
      StringFlag = 0

print(DataList)
'''