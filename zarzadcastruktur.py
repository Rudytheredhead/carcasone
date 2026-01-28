import struktura
import Kafelek
import nazwy
import gracz
naz = nazwy.nazwy()
class Menedzer_Struktur:
    def __init__(self):
        self.struktury = [] # tab na wszystkie aktywne strukuty
        self.next_id =1
        self.mapa = {} # mapa elementow (x,y,kierunek) -> struktura
    def nowa_strukura(self,typ):
            s = struktura.Struktura(typ,self.next_id)
            self.struktury.append(s)
            self.next_id+=1
            return s
    def usun_strukture(self,strukt):
         if strukt in self.struktury:
              self.struktury.remove(strukt)
    def polozenie_kafelka(self,kafelek,gracze):
         x_grid, y_grid = kafelek.grid_x, kafelek.grid_y
         for idx, segment in enumerate(kafelek.polaczenia):
                typ = segment["typ"]
                strony_segmentu = segment["poloczenia"]
                znalezione_strukury =set() #set zeby nie bylo powtorzen
                for strona in strony_segmentu:
                    sasiad_stuktura = self.znajdz_sasiada(x_grid,y_grid, strona)
                    if sasiad_stuktura and sasiad_stuktura.typ == typ:
                            znalezione_strukury.add(sasiad_stuktura)
                            
                lista_strukur = list(znalezione_strukury)
                
                aktywna_struktura = None
                nowi_gracze = []
                nowe_pionki =[]
                if len(lista_strukur) == 0:
                      aktywna_struktura = self.nowa_strukura(typ)
                else:
                      
                      aktywna_struktura = lista_strukur[0]
                      if lista_strukur[0].zajeta is not False:
                            nowi_gracze.extend(lista_strukur[0].zajeta)
                            nowe_pionki.extend(lista_strukur[0].pionki)
                      for do_scalenia in lista_strukur[1:]:
                            aktywna_struktura.scal(do_scalenia)
                            self.aktualizuj_ref(do_scalenia, aktywna_struktura)
                            if do_scalenia.zajeta is not False:
                                  nowi_gracze.extend(do_scalenia.zajeta)
                                  nowe_pionki.extend(do_scalenia.zajeta)

                            self.usun_strukture(do_scalenia)
                aktywna_struktura.dodaj_element(x_grid,y_grid,idx,segment)
                if nowi_gracze != []:
                      aktywna_struktura.zajeta = nowi_gracze
                      aktywna_struktura.pionki = nowe_pionki
                for strona in strony_segmentu:
                      self.mapa[(x_grid,y_grid,strona)] = aktywna_struktura
                self.sprawdz_czy_zamknieta(aktywna_struktura)
                

    def znajdz_sasiada(self, x,y,strona):
        
        dx,dy =0,0
        przeciwna = " "
        if strona == naz.N: dx, dy, przeciwna = 0, 1, naz.S
        elif strona == naz.S: dx, dy, przeciwna = 0, -1, naz.N
        elif strona == naz.E: dx, dy, przeciwna = 1, 0, naz.W
        elif strona == naz.W: dx, dy, przeciwna = -1, 0, naz.E

        klucz = (x+dx, y+dy, przeciwna)
        
        return self.mapa.get(klucz)
    def aktualizuj_ref(self, do_scalenia,aktywna):
          for klucz, struktura in self.mapa.items():
                if struktura == do_scalenia:
                      self.mapa[klucz] = aktywna
    def sprawdz_czy_zamknieta(self,struktura):
            zamknieta = True
            tarcze = 0
            katedra = False
            karczma = False
            
            liczba_elemtentow = set()
            for (x,y,id,segment) in struktura.elementy:
                liczba_elemtentow.add((x,y,id))
                if segment["typ"] == naz.DROGA and segment["karczma"]:
                      karczma = True
                elif segment["typ"] == naz.MIASTO:
                      if segment["katedra"]:katedra = True
                      if segment["tarcza"]:tarcze+=1
                for kierunek in segment["poloczenia"]:
                      sasiad = self.znajdz_sasiada(x,y,kierunek)
                      if sasiad is None:
                            zamknieta = False
            struktura.czy_zamknieta = zamknieta
            mnoznik = 1
            if struktura.typ == naz.MIASTO:
                if struktura.czy_zamknieta:
                    mnoznik = 2
                    if katedra:
                          mnoznik =3
                if not struktura.czy_zamknieta and katedra:
                      mnoznik = 0
            elif struktura.typ == naz.DROGA:
                    if struktura.czy_zamknieta and karczma:
                        mnoznik = 2
                    if not struktura.czy_zamknieta and karczma:
                          mnoznik = 0
            punkty = (len(liczba_elemtentow)+tarcze)*mnoznik
            struktura.punkty = punkty
            
    def zajecie_struktury(self,x_grid,y_grid,kierunek,gracz=None,pionek = None):
          self.mapa[(x_grid,y_grid,kierunek)].zajeta= [gracz] #jak powstanie klasa gracz zmian na gracz.kolor
          self.mapa[(x_grid,y_grid,kierunek)].pionki = pionek
            
                    
                        
                    

                      

                
                    
                
                
