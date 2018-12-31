'''Edward Yaroslavsky eyarosla 11/15/18
I pledge my honor that I have abided by the Stevens Honor System.

Lab 11'''

class QuadraticEquation(object):
    def __init__(self,a,b,c):
        '''Constructor that assigns float values to the properties'''
        self.__a = float(a)
        if self.__a == 0.0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__b = float(b)
        self.__c = float(c)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c
        
    def discriminant(self):
        '''Finds the discriminant in the quadratic formula'''
        return self.__b**2 - (4 * self.__a * self.__c)

    def root1(self):
        '''Finds the first root from the quadratic formula'''
        if self.discriminant() < 0:
            return None
        else:
            numerator = (-1*self.__b)+(self.discriminant())**(.5)
            denominator = 2 * self.__a
            return numerator / denominator

    def root2(self):
        '''Finds the second root from the quadratic formula'''
        if self.discriminant() < 0:
            return None
        else:
            numerator = (-1*self.__b)-(self.discriminant())**(.5)
            denominator = 2 * self.__a
            return numerator / denominator

    def __str__(self):
        '''Outputs the quadratic equation as a string'''
        if self.__a < 0:
            a = '-x^2'
        elif self.__a == 1:
            a = 'x^2'
        else:
            a = str(self.__a) + 'x^2'

        if self.__b == -1:
            b = ' - ' + 'x'
        elif self.__b < 0:
            b = ' - ' + str(self.__b * -1) + 'x'
        elif self.__b == 0:
            b = ''
        elif self.__b == 1:
            b = ' + x'
        else:
            b = ' + ' + str(self.__b) + 'x'

        if self.__c < 0:
            c = ' - ' + str(self.__c * -1)
        elif self.__c == 0:
            c = ''
        else:
            c = ' + ' + str(self.__c)

        return a + b + c + ' = 0'
            
