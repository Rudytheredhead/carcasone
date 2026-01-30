#mozliwosc dla bokow: miasto, droga, pole

import nazwy
import copy
import arcade
import pionek
import numpy as np
naz = nazwy.nazwy()
def obrot_kierunku(kierunek, wskazowki = True):
    if kierunek == naz.CENTER:
        return naz.CENTER
    if wskazowki:
        if kierunek == naz.N:
            return naz.E
        if kierunek == naz.E:
            return naz.S
        if kierunek == naz.S:
            return naz.W
        if kierunek == naz.W:
            return naz.N
    else:
        if kierunek == naz.N:
            return naz.W
        if kierunek == naz.W:
            return naz.S
        if kierunek == naz.S:
            return naz.E
        if kierunek == naz.E:
            return naz.N

naz = nazwy.nazwy()


testowe_poloczenie = [
    {"typ":naz.MIASTO, "poloczenia":[naz.N], "tarcza":False, "katedra":False},
    {"typ": naz.DROGA, "poloczenia":[naz.E, naz.W], "karczma" : False}
  ]

testowe_poloczenie2 = [
    {"typ": naz.DROGA, "poloczenia":[naz.E, naz.W], "karczma" : False},
    {"typ": naz.MIASTO, "poloczenia":[naz.N], "karczma" : False},
    {"typ":naz.POLE, "poloczenia":[naz.WG,naz.EG], "miasto":[naz.N]},
    {"typ":naz.POLE, "poloczenia":[naz.WD,naz.SL,naz.SP,naz.ED],"miasto":False}

]
class Kafelek:
    def __init__(self, image_path, n, e, s, w,czy_klasztor=False,czy_katedra=False, czy_karczma=False, grid_x=None, grid_y=None,kat = 0,poloczenia = None):
        self.image_path = image_path
        self.rozmiar_kafelka = 100
        self.boki = {'N': n, 'E': e, 'S': s, 'W': w}
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.czy_klasztor = czy_klasztor
        self.czy_katedra = czy_katedra
        self.czy_karczma = czy_karczma
        self.kat = kat
        self.polaczenia = poloczenia
        
        

    def obrot(self, wskazowki_zegara=True):
        if not wskazowki_zegara:
            n = self.boki['N']
            e = self.boki['E']
            s = self.boki['S']
            w = self.boki['W']
            self.boki['N'] = e
            self.boki['E'] = s
            self.boki['S'] = w
            self.boki['W'] = n
            self.kat += -90


        else:
            n = self.boki['N']
            e = self.boki['E']
            s = self.boki['S']
            w = self.boki['W']
            self.boki['N'] = w
            self.boki['E'] = n
            self.boki['S'] = e
            self.boki['W'] = s
            self.kat += +90
        
        for poloczenie in self.polaczenia:
                
                for idx in range(len(poloczenie["poloczenia"])):
                    poloczenie["poloczenia"][idx] = obrot_kierunku(poloczenie["poloczenia"][idx],wskazowki=wskazowki_zegara)
        
    def poloz_kafelek(self, grid_x, grid_y):
        nowe_polaczenia = copy.deepcopy(self.polaczenia)
        
        return Kafelek(self.image_path, self.boki['N'], self.boki['E'], self.boki['S'], self.boki['W'], self.czy_klasztor, self.czy_katedra, self.czy_karczma, grid_x, grid_y,kat =self.kat, poloczenia=nowe_polaczenia)
    def do_sprite(self, center_x, center_y):
        sprite = arcade.Sprite(self.image_path, scale=1, center_x=center_x, center_y=center_y)
        sprite.width = self.rozmiar_kafelka
        sprite.height = self.rozmiar_kafelka
        sprite.angle =self.kat
        
        return sprite
    def get_sasiadujaca_strona(self,grid_x,grid_y):
        if grid_x == self.grid_x and grid_y == self.grid_y + 1:
            return 'N'
        elif grid_x == self.grid_x + 1 and grid_y == self.grid_y:
            return 'E'
        elif grid_x == self.grid_x and grid_y == self.grid_y - 1:
            return 'S'
        elif grid_x == self.grid_x - 1 and grid_y == self.grid_y:
            return 'W'
        else:
            return None
    def czy_mozna_polaczyc(self,inny_kafelek):
         
        moja_strona = self.get_sasiadujaca_strona(inny_kafelek.grid_x, inny_kafelek.grid_y)
        moj_bok = self.boki[moja_strona]
        if not moja_strona:
            return False
        if  moja_strona == 'N':
            inny_bok = inny_kafelek.boki['S']
        if  moja_strona== 'S':
            inny_bok = inny_kafelek.boki['N']
        if  moja_strona== 'E':
            inny_bok = inny_kafelek.boki['W']
        if  moja_strona == 'W':
            inny_bok = inny_kafelek.boki['E']
        
        
        return moj_bok == inny_bok
    def get_hotspoty(self,meneger):
        hotspoty = []
        hotspot =None
        for idx,segment in enumerate(self.polaczenia):
            
            hotspot = {"typ":segment["typ"], "polozenie":[], "kierunek":[]}
            czy_zajete = False
            
            for idx,poloczenie in enumerate(segment["poloczenia"]):
                if meneger.mapa.get((self.grid_x,self.grid_y, poloczenie)).zajeta is not False:
                    continue
                hotspot = {"typ":segment["typ"], "polozenie":[], "kierunek":[]}        
                
                
                hotspot['polozenie'].append(self.kierunek_na_przesuniecie(poloczenie))
                hotspot['kierunek'].append(poloczenie)
                if hotspot is not None:
                    hotspoty.append(hotspot)
            del hotspot
        if hotspoty ==[]:
            return False
        return hotspoty
    def kierunek_na_przesuniecie(self, kierunek):
        dx, dy =0,0
        if kierunek == naz.N:dy = 40
        if kierunek == naz.S:dy = -40
        if kierunek == naz.E:dx = 40
        if kierunek == naz.W:dx = -40
        if kierunek == naz.CENTER: dx,dy =0,0
        return (dx,dy)
    def rysuj_hotspoty(self,meneger):
        x_kafelka, y_kafelka = self.grid_x, self.grid_y
        x_kafelka, y_kafelka = x_kafelka*100, y_kafelka*100
        
        tablica = self.get_hotspoty(meneger)
        
        if  not tablica:
            return
        for hotspoty in tablica:
            for hotspot in hotspoty["polozenie"]:
                
            
                dx,dy = hotspot
                arcade.draw_circle_filled(x_kafelka+dx, y_kafelka+dy, 5, arcade.color.BLACK_OLIVE)
    def czy_nacisnieto_hotspot(self,mouse_x,mouse_y,czy_polozyc_pionek= None,meneger = None):
        sprite,kierunek = None,None
        x_kafelka, y_kafelka = self.grid_x, self.grid_y
        x_kafelka, y_kafelka = x_kafelka*100, y_kafelka*100
        
        tablica = self.get_hotspoty(meneger)
       
        if not tablica:
            return None,None
        
        
        for hotspoty in tablica:
            for idx,hotspot in enumerate(hotspoty["polozenie"]):
                dx,dy = hotspot
                x, y = x_kafelka+dx, y_kafelka+dy
                odleglosc_x,odleglosc_y = mouse_x - x,mouse_y-y
                odleglosc = np.sqrt(odleglosc_y**2 + odleglosc_x**2)
                
                if odleglosc<=10:
                    
                    kierunek=  hotspoty["kierunek"][idx]
                    if czy_polozyc_pionek:
                        if kierunek == naz.E :kat = 90
                        elif kierunek == naz.W: kat= -90
                        else: kat = 0
                        pion = pionek.Pionek(kolor = czy_polozyc_pionek,kat = kat)#kolor gracza
                        pion.x , pion.y = x,y
        
        if kierunek is None:
            return None,None
        if czy_polozyc_pionek:
            return pion,kierunek
        else:
            return kierunek

                


