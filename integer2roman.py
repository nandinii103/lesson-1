class Integer2Roman:
    def __init__(self):
        self.roman_map = [
            (500 ,'D' ) , (50 , 'L') , (5 , 'V') , (100 , ' C')
            (10 , 'X') , (1000 , 'M')
        ]
        def convert(self , num):
            roman_numeral = ""
    for value,symbol in self.roman_map:
        while num >= value:
            roman_value += symbol
            num -= value
            

    