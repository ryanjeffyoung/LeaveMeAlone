from setup import get_calendar_service
from freebusy import getApiResult, getBusyList, fill_day,checkBusy, apiCall
from event import SLL
from datetimerange import DateTimeRange
import datetime
import time

# set calId to use
calId = 'ryan.jeffery.young@gmail.com'
# create google API service
service = get_calendar_service()
# todays_events = apiCall(service, calId) # this is resetting the head every cycle, endless loop
# todays_events.output_list()

while True:
    now = datetime.datetime.utcnow().isoformat() + 'Z'

    result = getApiResult(service, calId)
    events_list = getBusyList(result, calId)
    
    for event in events_list:
        start = event['start']
        end = event['end']

        time_range = DateTimeRange(start, end)

        if now in time_range:
            print('busy')
        else:
            print('sleeping')
    # sleep for 1 min refresh
    time.sleep(60)
    
