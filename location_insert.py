import requests,re,json,string,sys,pycountry,pymongo
from collections import Counter
string_value = str(sys.argv[1])
print string_value
response = requests.get('http://english.ctrip.com/hotels/tool/ibuKeyWordSearchV2?keyword='+string_value)
data= response.content
stringdata = re.sub('[()]','',data)#removing '(',')' from data
jsondata = json.loads(stringdata)#converting into json data
IntIcity = []
IntIcity.append([d for d in jsondata['result'] if d['type'] == 'Intlcity'])
new_vals = IntIcity[0] 
nlod=[{k:d[k] for k in ('cityid','cityname','countryname','code','type','provincename')} for d in new_vals]
#attribbute name convertions and updating into final list
keyMap={'cityid':'_id','countryname':'country','code':'country_code','type':'type','cityname':'city','provincename':'state'}
final_li=[]
for r in nlod:
	final_li.append({keyMap[k]: v for k, v in r.items()})
#To find country code
mapping = {country.name: country.alpha_2 for country in pycountry.countries}
for sub in final_li:
	sub['_id']=int(sub['_id'])
	sub['country_code']= mapping.get(sub['country'])
for r in range(len(final_li)):
		print(str(r)) +" :   city     "+ final_li[r]['city'] +' country  '+final_li[r]['country'] 
k = int(input("Enter your choice :"))
# data base connections and insertion 
try:
	connection = pymongo.MongoClient('localhost',27017)
	db = connection.CT
	record = db.locations
	record.insert(final_li[k])
except pymongo.errors.DuplicateKeyError, e:
	print 'location is already avilable collection ,   ' + str(e)
except pymongo.errors.ConnectionFailure, e:
	print 'connection lost,           '+ str(e)