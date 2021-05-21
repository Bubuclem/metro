import datetime
from django.utils import timezone

# Timer
class TimeEntry(object):
    def __init__(self, start_time,end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days = self.total_time.days
        self.seconds = self.total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
    
    def serialize(self):
        return {
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.days,
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds
        }

    def microseconds(self):
        return self.total_time.microseconds

def get_time():
    return timezone.now()

def start_timer():
    time = get_time()
    return time

def stop_timer(start):
    end = get_time()
    time = TimeEntry(start,end)
    return time.microseconds()

# Print
class Print_value(object):
    def __init__(self):
        self.messages = []

    def add_message(self,*messages):
        for message in messages:
            self.messages.append(message)