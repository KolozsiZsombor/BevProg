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

    def __str__(self):
        return self._nev + f" Egy szuperhős, akinkek a szuperereje {str(self._szuperero)}"
    
    def __eq__(self, masik_hos):
        return self._nev == masik_hos._nev and self._szuperero == masik_hos._szuperero

    def __add__(self, masik_hos):
        if isinstance(masik_hos, Szuperhos):
            uj_szuperero = self._szuperero + masik_hos._szuperero
            uj_szuperhos = Szuperhos("Megahős", uj_szuperero)
            return uj_szuperhos

hos1 = Szuperhos("Thor",70)
hos2 = Szuperhos("Hulk",80)
hos3 = Szuperhos("Pikachu",80085)
hos4 = hos1 + hos2
hos5 = 6 + 2

print(hos1)

print(hos5 == hos2)
print(hos4)
