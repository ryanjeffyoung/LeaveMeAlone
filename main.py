from setup import Setup
from freebusy import getApiResult, getBusyList
from event import SLL
from datetimerange import DateTimeRange
import datetime
import time
import i2c_lcd_driver
import pytz
from pytz import timezone
# init lcd screen
mylcd = i2c_lcd_driver.lcd()
mylcd.lcd_clear()
# set calId to use
calId = 'ryan.jeffery.young@gmail.com'
# create google API service
service = Setup()
while True:
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    result = getApiResult(service, calId)
    events_list = getBusyList(result, calId)
    if len(events_list) == 0:
        # mylcd.lcd_display_string('Not busy', 1)
        # mylcd.lcd_display_string('Please knock :)', 2)
        print('not busy')
    for event in events_list:
        start = event['start']
        end = event['end']
        pst = timezone('US/Pacific')
        end_dt = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%Sz')
        end_dt_utc = pytz.UTC.localize(end_dt)
        end_local = end_dt_utc.astimezone(pst)
        end_formatted = end_local.strftime('%I:%M %p')                                                           
        time_range = DateTimeRange(start, end)
        if now in time_range:
            mylcd.lcd_display_string("BUSY Until", 1)
            mylcd.lcd_display_string(end_formatted, 2)
            # print('busy until', end_formatted)
        else:
            mylcd.lcd_display_string('Not busy', 1)
            mylcd.lcd_display_string('Please knock :)', 2)
            # print('not busy')
    # sleep for 1 min refresh
    time.sleep(60)
    
