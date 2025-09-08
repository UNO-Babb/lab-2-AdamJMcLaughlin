#FutureTime.py
#Name:
#Date:
#Assignment:

print("Adam McLaughlin\n09/04/2025\nFutureTime")
print()
# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  startHour = int(input("Enter starting hour (0-23)"))
  startMinute = int(input("Enter starting minute (0-59)"))
  moreMins = 500

  totalMinutes = startMinute + moreMins
  futureMins = (currentMinute + moreMins ) % 60
  extraHour = (currentMinute + moreMins ) // 60
  futureHour = (startHour + extraHour) % 24

  print(extraHour)

  print(futureMins)
  #Calculate the time after the user-supplied time has passed.
 

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"{futureHour:02d}:{futureMins:02d}")

if __name__ == '__main__':
  main()

