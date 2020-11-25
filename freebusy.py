import datetime
from datetime import timedelta   
from setup import get_calendar_service

def main():
    service = get_calendar_service()

    calId = 'ryan.jeffery.young@gmail.com'

    # call APi
    now = datetime.datetime.utcnow().isoformat() + 'Z' # z for UTC time
    tmr = datetime.datetime.utcnow() + timedelta(days=2)
    tmr_utc = tmr.isoformat() + 'Z'

    body = {
           "timeMin": now,
           "timeMax": tmr_utc,
           "timeZone": "PST",
           "items": [{"id": calId}]
       }
    
    freebusy_result = service.freebusy().query(body=body).execute()

    freebusy = freebusy_result[u'calendars']

    busyList = freebusy[calId]['busy']


    busy_cal = {}
    for cal_name in freebusy:
      busy_cal.update(freebusy[cal_name])

    print((busyList[0])['start'])


if __name__ == '__main__':
    main()


    