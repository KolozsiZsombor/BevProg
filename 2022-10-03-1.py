class Szuperhos:
    def __init__(self, nev, szuperero = 50):
        self._nev = nev
        self._szuperero = szuperero 
        # print("--Szuperhős létrehozva--")

    def get_szuperero(self):
            return self._szuperero

    def set_szuperero(self, ertek):
            self.szuperero = ertek

hos1 = Szuperhos("Thor",70)

hos1.set_szuperero(455)

print(hos1.get_szuperero())