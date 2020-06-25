from datetime import datetime

"""_—Returns the current day (Sunday, for example)2_part_of_day(self)—Returns “morning” if the current hour is before 12 P.M.,“afternoon” if the current hour is 12 P.M. or later but before 5 P.M., and “eve-ning” from 5 P.M. onward3greet(self, store)—Given the name of a store, store, and the output of theprevious two methods, prints a message of the formHi, welcome to <store>!How’s your <day> <part of day> going?Here’s a coupon for 20% off!The _day and _part_of_day methods can be signified as private (named with a lead-ing  underscore)  because  the  only  functionality  the  Greeter  class  needs  to  expose  isgreet. This helps encapsulate the internals of the Greeter class so that its only publicconcern is performing the greeting itself.TIPYou  can  use  datetime.datetime.now()  to  get  the  current  datetimeobject, using the .hour attribute for the time of day and .strftime('%A') toget the current day of the week.How did it go? Your solution should look something like the following example."""


class Greetings:
    def __init__(self):
        self.name = None

    def _day(self):
        return datetime.now().strftime('%A')

    def _part_of_day(self):
        hour = datetime.now().hour
        if hour < 12:
            part_of_day = 'morning'
        elif 12 <= hour < 17:
            part_of_day = 'afternoon'
        else:
            part_of_day = 'evening'
            return part_of_day
        return

    def greet(self, store):
        print(
            f"Hi, welcome to {store} \n!How’s your {self._day()} {self._part_of_day()} going? \nHere’s a coupon for "
            f"20 % off!")
