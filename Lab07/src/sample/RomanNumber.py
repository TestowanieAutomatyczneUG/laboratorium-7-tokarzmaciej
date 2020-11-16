class Roman():
    def roman(self, romanNumber):
        if type(romanNumber) != int:
            raise Exception("You take bad type")
        romanNumberTuple = (('M', 1000),
                            ('CM', 900),
                            ('D', 500),
                            ('CD', 400),
                            ('C', 100),
                            ('XC', 90),
                            ('L', 50),
                            ('XL', 40),
                            ('X', 10),
                            ('IX', 9),
                            ('V', 5),
                            ('IV', 4),
                            ('I', 1))
        arabNumber = ""
        for numeral, integer in romanNumberTuple:
            while romanNumber >= integer:
                arabNumber += numeral
                romanNumber -= integer
        return arabNumber
