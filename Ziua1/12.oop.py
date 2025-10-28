
## CLASA este un sablon
## este scrisa cu litera mare la inceput
class Student:
    """ ACEASTA ESTE DOCUMENTATIA PT CLASA STUDENT
    """
    ## __init__ -> este o functie magica (toate cele care au "__")
    def __init__(self, nume, varsta):
        """ACEASA E DOCUMENTATIA PT __INIT__"""
        self.varsta = varsta
        self.nume = nume

    ## functia de conversie la string
    def __str__(self):
        return f"Studentul pe nume {self.nume} are varsta {self.varsta} ani "


## Folosire obiect
obiect = Student("Florin", 23)
print(obiect)

obiect = Student("Mihaela", 21)
print(obiect)

print(Student.__doc__)

help(Student)