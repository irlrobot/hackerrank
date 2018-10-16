class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print('You are young.')
            return
        if self.age >= 13 and self.age < 18:
            print('You are a teenager.')
            return
        print('You are old.')

    def yearPasses(self):
        self.age += 1