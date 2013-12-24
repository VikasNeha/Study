"""
Retrieves trend data for a given item_id
"""

from getpass import getpass
from pyzabbix import ZabbixAPI
from datetime import datetime
from datetime import date
import time
import csv

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://zabbix.example.com'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
zapi.login('user', 'xxxxxxxxx')

#name = raw_input('What is your first name? ')
#print 'Your name is, %s' % name.capitalize()

from time import strptime


def get_date():
    while True:
        date = raw_input("Please enter a date in YYYYMMDD format: ")
        try:
            parsed = strptime(date, "%Y%m%d")
        except ValueError as e:
            print "Could not parse date: {0}".format(e)
        else:
            return parsed[:3]

year, month, day = get_date()
today = get_date()
print today

graphids=[5128, 6999, 5106]
for graphid in graphids:
    items = zapi.item.get(graphids=[graphid],
    output='shorten', webitems=1)
    itemids = []
    for item in items:
        itemid = item['itemid']
        itemids.append(itemid)
        print item['itemid']

    f = open('test_' + str(graphid) + '-' + str(today) + '.csv', 'wb+')
    writer = csv.writer(f)
    writer.writerow(str(today))
    writer.writerow(itemids)
    #sys.stdout = f
    averages=[]

    # Create a time range
    time_till = time.mktime(datetime.now().timetuple())
    time_from = time_till - 60 * 60 * 24  # 24 hours

    for itemid in itemids:

        print itemid
        # Query item's trend data
        history = zapi.history.get(itemids=[itemid],
            time_from=time_from,
            time_till=time_till,
            output='extend',
            limit='5000',
            )


        # If nothing was found, try getting it from history
        if not len(history):
            print "zero length"
            history = zapi.history.get(itemids=[itemid],
                time_from=time_from,
                time_till=time_till,
                output='extend',
                limit='5000',
                history=0,
                )

        latencies=[]
        sumLatencies=0
        # Print out mean value for itemid
        for point in history:
            #print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
            #.strftime("%x %X"), point['value']))
            latency = point['value'].split()[-1]
            latencies.append(latency)
            sumLatencies+=float(latency)

        if len(latencies) == 0:
            average = sumLatencies
        else:
            average = sumLatencies / len(latencies)
        print average
        averages.append("%.3f" % average)
    for average in averages:
        print average

    writer.writerow(averages)

    f.close()
