json=' { "String" : "1" ,"number":2,"true":true,"false":false,"arraywithnumber":[1,2,3],"arraywithstring":["a","b"],"arraywithboolean":[true,false],"obj":{"1":"2"}}'
class flags:
  #將旗標集中
  def __init__(self):
    self.position=0
    self.objectnum=0
    self.currrentobjectnum=0
    self.left=[]

Done=0
strs=[]
def peeknextchar(json,flags):
  return(json[flags.position+1])
  
def tonextchar(flags):
  flags.position+=1

def EndOfObject(json,flags):
  flags.currrentobjectnum+=1
  if(flags.currrentobjectnum==flags.objectnum):
    global Done
    Done=1

def object(json,flags):
  while(1):
    if(json[flags.position]=='{'):
      flags.left.append(flags.position)
      #print(json[flags.position],end="")
      tonextchar(flags)
    if(peeknextchar(json,flags)!='}'):
      #print(json[flags.position],end="")
      tonextchar(flags)
    else:
      #print(json[flags.position],end="")
      tonextchar(flags)
      EndOfObject(json,flags)
      strs.append(json[flags.left.pop():flags.position+1])
    if(Done):
      #print(json[flags.position],end="")
      break

def value():
  pass

def String(json,flags):
  pass

flags=flags()

if(json.count('{')==json.count('}')):
  flags.objectnum=json.count('{')
  while(1):
    if(Done):
      break
    if(json[flags.position]=='{'):
      object(json,flags)
    else:
      tonextchar(flags)
    


print(strs)
