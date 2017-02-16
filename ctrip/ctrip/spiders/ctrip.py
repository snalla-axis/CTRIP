import scrapy 
import json 
import pprint 
import requests
from scrapy.http import Request
import urllib
url = 'http://english.ctrip.com/Hotels/list/HotelJsonResult?'       
city = []
u_list = []
original_list = []
#pageno =[('2017-03-21','2017-03-22'),('2017-03-22','2017-03-23')]
d = [('2017-02-17','2017-02-18'),('2017-02-19','2017-02-20'),('2017-02-21','2017-02-22'),('2017-03-17','2017-03-18'),('2017-03-19','2017-03-20'),('2017-03-21','2017-03-22')]
#fo = open('delhi.txt','a')
class CtripSpider(scrapy.Spider):
    name = "ctrip"#1365#1095#1367
    
    def start_requests(self):
        #url = 'http://english.ctrip.com/Hotels/list/HotelJsonResult?'
        #for chk_in, chk_out in get_dates:#, [('12-02-2017', '13-02-2017')]
        for chk_in,chk_out in d:
            request = scrapy.FormRequest(
                url=url,
                formdata={'city':'495','pageno':'0','checkin':chk_in,'checkout':chk_out},#,'isScrolling':'true'},
                method='POST',
                callback=self.parse_data)
            yield request
        #yield Request(url,self.parse_data,method="POST",body=urllib.urlencode(payload))
    def parse_data(self, response):
        # do stuff with data...
        data1=json.loads(response.body)
        #for r in data1['HotelResultModel']:
         #   fo.write(str(r['hotelId'])+"\n")
            #print  (r['hotelName'])
        c = ((data1['ResultCount'])/10)
        print c
        pageno=range(0,c)
        for j in pageno:
            yield scrapy.FormRequest(
                url=url,
                formdata={'city':'495','pageno':str(j)},#,'checkin':'2017-02-17','checkout':'2017-02-18'},#'isScrolling':'true'},
                dont_filter=True,
                method='POST',callback=self.data_second,
                ) 
            
    def data_second(self,response):
        sdata=json.loads(response.body) 
        for r in sdata['HotelResultModel']:
            original_list.append(r['hotelId'])
            [u_list.append(x) for x in original_list if x not in u_list]
        print len(u_list) 

        #for r in sdata['HotelResultModel']:
         #   fo.write(str(r['hotelId'])+"\n")
               #print r['hoelId']fo.write(str(r['hotelId'])+"\n")
            #print  (r['hotelName'])
        #fo.write(str(r['hotelId'])+"\n"+r['hotelUrl']+"\n")
        #print(data)'''
