from setup import get_calendar_service
import datetime
import time
from datetime import timedelta
from datetimerange import DateTimeRange
from event import SLL
from queue import Event, Queue

def getApiResult(service, calendarID):
  """Hit google calendar freebusy API

   Keyword arguments:
   service -- the API service from setup.py
   calendarID -- the email associated with calendar (ex. myemail@gmail.com)
  """
  # get todays date
  today = datetime.date.today()
  tomorrow = today + timedelta(days=1)

  # convert date into datetime object at start of day, which is 800 UTC
  start = datetime.datetime(today.year, today.month, today.day, 8, 0, 0)  # 8am UTC is 12am PST
  # convert to ISO format then append 'Z' for UTC time
  start_UTC = start.isoformat() + 'Z'

  # 7:59am UTC is 11:59pm PST
  end = datetime.datetime(today.year, today.month, tomorrow.day, 7, 59, 0) #11:59pm PST
  end_UTC = end.isoformat() + 'Z'

  body = {
    "timeMin": start_UTC,
    "timeMax": end_UTC,
    "items": [{"id": calendarID}]
  }
  freebusy_result = service.freebusy().query(body=body).execute()  # returns a dictionary
  
  return freebusy_result

def getBusyList(result, calendarID):
  """Extract list of busy times in a day

   Keyword arguments:
   result -- default formatted result from API
   calendarID -- the email associated with calendar (ex. myemail@gmail.com)
  """
  busy_list = result['calendars'][calendarID]['busy']
  return busy_list


def fill_day(busy_list):
  # day = SLL()
  day = Queue()

  for event in busy_list:
    start = event['start']
    end = event['end']
    day.EnQueue(start, end)
  
  return day



def apiCall(service, calendarID):
  result = getApiResult(service, calendarID)

  busy_list = getBusyList(result, calendarID)

  todays_events = fill_day(busy_list)

  return todays_events

def checkBusy(currTime, events_list):
  # see if current time within range of event @ head
  start = events_list.front.data['start']
  end = events_list.front.data['end']
  # set time range for head event
  time_range = DateTimeRange(start, end)

  if currTime in time_range:
    return True
  else:
    return False

    

# def main():
  # set time range for head event

  # meetings.output_list()

  # while True:
  #   print('top of loop')
  #   # check if any events
  #   if meetings.head == None:
  #     print('sleeping...')
  #     time.sleep(5)
  #     continue
    
  #   now = datetime.datetime.utcnow().isoformat() + 'Z'
  #   end = meetings.head.data['end'] 
    # check if busy
    # if checkBusy(now):
    #   print('Busy')
    # else:
    #   print('Not busy')
    #   # refresh api call

    #   time.sleep(5)
  #     # check if curr time is past end time
  #     if now > end:
  #       print('removing head')
  #       # remove head event
  #       meetings.del_head()

  # meetings.output_list()

# if __name__ == '__main__':
#   main()