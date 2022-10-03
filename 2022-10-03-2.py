class Szuperhos:
    def __init__(self, nev, szuperero = 50):
        self._nev = nev
        self._szuperero = szuperero 
        # print("--Szuperhős létrehozva--")

    @property
    def szuperero(self):
        return self._szuperero

    @szuperero.setter
    def szuperero(self, ertek):
        self._szuperero = ertek

    

hos1 = Szuperhos("Thor",70)

hos1.szuperero = 13

print(hos1.szuperero)