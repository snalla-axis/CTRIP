# import datetime
# now = datetime.date.today()
# now_day_1 = now

# dates = {}

# for n_week in range(1):
#     dates[n_week] = [(now_day_1 + datetime.timedelta(days=d)).strftime("%y-%m-%d") for d in range(7)]
#     dates[n_week]=	[(now_day_1 + datetime.timedelta(mdasy[today.month])).]

# # print dates
# from calendar import mdays
# from datetime import datetime, timedelta

# today = datetime.now()
# next_month_of_today = today + timedelta(mdays[today.month])
# print next_month_of_today
import datetime
from dateutil import relativedelta
def date():
	nextmonth = []
	thismonth=[]
	thismonth = [datetime.date.today()+datetime.timedelta(days=d) for d in range(8)]
	nextmonth = [datetime.date.today()+datetime.timedelta(days=d) + relativedelta.relativedelta(months=1) for d in range(8)]
	#print type(str(nextmonth[0]))
	#print type(str(thismonth[0]))
		#c=[]
		#c = [tuple(zip(thismonth,thismonth[d] for d in range(1,7)))]
	d = [tuple(t for t in zip(thismonth[::1], thismonth[1::1]))]
	d.append(tuple(t for t in zip(nextmonth[::1], nextmonth[1::1])))
	res=[k for i in d for k in i]
	#print d
	return res

