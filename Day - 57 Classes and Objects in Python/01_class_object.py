class Person:
    name = "Hridoy"
    occupation = "Software Devloper"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}" )

a = Person()
b = Person()
c = Person()
a.name = "Shuvo"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"


# print(a.name, a.occupation)
a.info()
b.info()
c.info()