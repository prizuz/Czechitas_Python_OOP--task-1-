import math

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

locality = Locality("Praha", 2)
loc1 = Locality("Manětín", 0.8)
loc2 = Locality("Brno", 3)

class Property:
    def __init__(self, locality):
        self.locality = locality

# zadání: atribut "locality" = lokalita, kde se pozemek nachází, je objektem třídy Locality
property1 = Property(locality)

class Estate(Property): 
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
# metoda, která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo
# daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku * koeficient obce
        if self.estate_type == "land":
            coefficient = 0.85
        if self.estate_type == "building_site":
            coefficient = 9
        if self.estate_type == "forrest":
            coefficient = 0.35

        tax = self.area * coefficient * self.locality.coefficient 
        return math.ceil(tax)

    def __str__(self):
        return f'Pozemek ({self.estate_type}), lokalita {locality.name} (koeficient {locality.coefficient}), plocha {self.area} metrů čtverečních, daň {my_tax} Kč.'

estate1 = Estate(locality, "forrest", 500)
my_tax = estate1.calculate_tax()
print(estate1) 

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        tax = self.area * self.locality.coefficient * 15
        if self.commercial == True:
            tax = tax * 2
        return math.ceil(tax)

    def __str__(self):
        return f'Nemovitost: lokalita {locality.name} (koeficient {locality.coefficient}), plocha {self.area} metrů čtverečních, daň {my_tax} Kč.'

# zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8
residence1 = Estate(loc1, "land", 900)
my_tax = residence1.calculate_tax()
print(residence1)

# dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8
residence2 = Residence(loc1, 120, False)
my_tax = residence2.calculate_tax()
print(residence2)

# kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3
residence3 = Residence(loc2, 90, True)
my_tax = residence3.calculate_tax()
print(residence3)


