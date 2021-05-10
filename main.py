__author__ = "ppowicz"
__copyright__ = "Copyright 2021, ppowicz"
__credits__ = ["Vulcan-API"]

__license__ = "GPL"
__version__ = "1.0.0"

"""

 ###### ###### #####  ######
 #      #    # #    # #
 #      #    # #    # #####
 #      #    # #    # #
 ###### ###### #####  ######

"""

import asyncio, datetime, random

from vulcan import Account
from vulcan import Keystore
from vulcan import Vulcan

maxLines = 75
maxRows = 100

def getKeystore():
  f = open("keystore.json")
  return Keystore.load(f)

def getAccount():
  f = open("account.json")
  return Account.load(f)

async def main():
  client = Vulcan(getKeystore(), getAccount())
  client.set_logging_level(0)

  startDate = datetime.date(2020, 9, 1)
  endDate = datetime.date(2021, 5, 10)

  await client.select_student()

  lessons = await client.data.get_lessons(date_from=startDate, date_to=endDate)

  mathLessonsArray = []

  async for lesson in lessons:
    if (lesson.subject.name == "Matematyka"):
      mathLessonsArray.append(str(lesson.date.date))

  for date in mathLessonsArray:
    f = open("notes/" + "matematyka " + date + ".txt", "w", encoding="utf-8")

    for i in range(random.randint(0, maxLines)):
      for i in range(random.randint(0, maxRows)):
        f.write(chr(random.randint(0, 255)))
      f.write("\n")

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())