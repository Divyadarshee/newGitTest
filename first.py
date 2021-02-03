import requests
import time


base_url="https://octopus.honeywell.com"


#ap1: this api call(GET) gets all the lifecycles in Spaces-1

api1= requests.get(base_url + "/api/Spaces-1/lifecycles/all/", headers={"X-Octopus-ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M","X-NuGet-ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M"},params={"ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M"})
api1Data = api1.json()


def urlParse(id):
    return (base_url + "/api/Spaces-1/lifecycles/" + id + "/projects/")

#All_lifecycle_id: stores all the lifecycles id for the given space- Spaces-1
All_lifecycle_id=[]


for x in api1Data:
    All_lifecycle_id.append(x['Id'])

#Unused_lifecycle_id: stores all the unused lifecycles
Unused_lifecycle_id=[]

#counter: to enable timed sleep calls (sleep every 50 api calls)
counter=0

#ap2: this api call(GET) gets all the lifecycles which have an empty response

for x in All_lifecycle_id:
    counter+=1
    if counter%50 ==0:
        time.sleep(5)
    api2 = requests.get(urlParse(x), headers={"X-Octopus-ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M","X-NuGet-ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M"},params={"ApiKey":"API-UZZN5WMCLYFDHDDEOQS69T1S5M"})
#    api2 = requests.get(urlParse(x), headers={"X-Octopus-ApiKey":"API-0GMPUPYVLXMUAHCC2JGIASSIKZG","X-NuGet-ApiKeyAPI-0GMPUPYVLXMUAHCC2JGIASSIKZG"},params={"ApiKey":"API-0GMPUPYVLXMUAHCC2JGIASSIKZG"})

    api2Data=api2.json()
    if not len(api2Data):
        Unused_lifecycle_id.append(x)


#print(All_lifecycle_id)
print(len(All_lifecycle_id))

#Storing all the unused lifecyles id in Lifecycles_3.txt file

f=open('Lifecycles_3.txt','w')
for ele in Unused_lifecycle_id:
    f.write(ele+'\n')

f.close()
print(len(Unused_lifecycle_id))