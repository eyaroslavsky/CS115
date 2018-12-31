'''
Created on 11/23/18
@author: Edward Yaroslavsky eyarosla
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''Changes the object to represent one calendar day after the
        date it originally represented.'''
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.isLeapYear():
            if self.month == 2 and self.day == 29:
                self.month = 3
                self.day = 1
            elif self.month == 2 and self.day == 28:
                self.day = 29
            elif self.day == DAYS_IN_MONTH[self.month]:
                self.month += 1
                self.day = 1
            else:
                self.day += 1
        elif self.day == DAYS_IN_MONTH[self.month]:
            self.month += 1
            self.day = 1
        else:
            self.day += 1

    def yesterday(self):
        '''Changes the object to represent one calendar day before the
        date it originally represented.'''
        if self.month == 1 and self.day == 1:
            self.month = 12
            self.day = 31
            self.year -= 1
        elif self.isLeapYear():
            if self.month == 3 and self.day == 1:
                self.month = 2
                self.day = 29
            elif self.day == 1:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
            else:
                self.day -= 1
        elif self.day == 1:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1

    def addNDays(self, N):
        '''Changes the calling object so that it
        represents N calendar days after the date it originally represented.'''
        for x in range(0,N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''Changes the calling object so that it
        represents N calendar days before the date it originally represented.'''
        for x in range(0,N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''Returns True if the calling object is a calendar date before the input
        named d2'''
        if d2.year < self.year:
            return False
        elif d2.year > self.year:
            return True
        else:
            if d2.month < self.month:
                return False
            elif d2.month > self.month:
                return True
            else:
                if d2.day < self.day:
                    return False
                elif d2.day > self.day:
                    return True
                else:
                    return False

    def isAfter(self, d2):
        ''''Returns True if the calling object is a calendar date after the input
        named d2'''
        if self.isBefore(d2) or self.equals(d2):
            return False
        return True

    def diff(self, d2):
        '''Returns an integer representing the number of days between self and d2'''
        selfCopy = self.copy()
        d2Copy = d2.copy()
        count = 0
        
        if selfCopy.isBefore(d2Copy):
            while selfCopy.isBefore(d2Copy):
                selfCopy.tomorrow()
                count -= 1
        elif selfCopy.isAfter(d2Copy):
            while selfCopy.isAfter(d2Copy):
                selfCopy.yesterday()
                count += 1
        return count

    def dow(self):
        '''Returns a string that indicates the day of the week of the object'''
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        d = Date(11,9,2011) #Wednesday
        diff = self.diff(d)
        if diff < 0:
            return days[2-(abs(diff)%7)]
        return days[2+(diff%7)]
        
