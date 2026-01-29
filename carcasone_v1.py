#https://wikicarpedia.com/car/Base_game
import arcade
import arcade.gui
import Kafelek
import numpy as np
import nazwy 
import gracz
import zarzadcastruktur

import copy #do usuniecia
naz = nazwy.nazwy()
fazy = nazwy.fazy()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"
meneger = zarzadcastruktur.Menedzer_Struktur()

wszystkie_kafelki = {
    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek1.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek1.png", 'miasto', 'droga', 'pole', 'droga',
    poloczenia=[{"typ": naz.DROGA, "poloczenia":[naz.E, naz.W], "karczma" :False},
                {"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False}],),
    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek2.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek2.png", 'miasto', 'miasto', 'miasto', 'miasto',
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N,naz.W,naz.S,naz.E], "tarcza" :True, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek3.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek3.png",  naz.MIASTO, naz.POLE, naz.POLE,  naz.POLE,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek4.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek4.png",  naz.POLE, naz.MIASTO, naz.POLE,  naz.MIASTO,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.E, naz.W], "tarcza" :True, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek5.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek5.png",  naz.POLE, naz.MIASTO, naz.POLE,  naz.MIASTO,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.E, naz.W], "tarcza" :False, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek6.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek6.png",  naz.MIASTO, naz.POLE,  naz.MIASTO, naz.POLE,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False},
                {"typ": naz.MIASTO, "poloczenia":[naz.S], "tarcza" :False, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek7.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek7.png",  naz.MIASTO, naz.POLE,  naz.POLE, naz.MIASTO,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False},
                {"typ": naz.MIASTO, "poloczenia":[naz.W], "tarcza" :False, "katedra" : False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek8.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek8.png",  naz.MIASTO, naz.DROGA,  naz.DROGA, naz.POLE,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False},
                {"typ": naz.DROGA, "poloczenia":[naz.E,naz.S], "karczma":False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek9.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek9.png",  naz.MIASTO, naz.POLE,  naz.DROGA, naz.DROGA,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False},
                {"typ": naz.DROGA, "poloczenia":[naz.W,naz.S], "karczma":False}],),

    r"E:\__priv\python\__pv\carcasonne\kafelki\kafeleka01.png": Kafelek.Kafelek(r"E:\__priv\python\__pv\carcasonne\kafelki\kafeleka01.png",  naz.MIASTO, naz.DROGA,  naz.DROGA, naz.DROGA,
    poloczenia=[{"typ": naz.MIASTO, "poloczenia":[naz.N], "tarcza" :False, "katedra" : False},
                {"typ": naz.DROGA, "poloczenia":[naz.W], "karczma":False},
                {"typ": naz.DROGA, "poloczenia":[naz.E], "karczma":False},
                {"typ": naz.DROGA, "poloczenia":[naz.S], "karczma":False},
                {"typ": naz.KLASZTOR, "poloczenia":[naz.CENTER]}],),                                                          
}
pula = [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek1.png"]*3
pula.extend([ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek2.png"])
pula.extend ( [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek3.png"]*5)
pula.extend( [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek4.png"]*2)
pula.extend( [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek5.png"]*1)
pula.extend( [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek6.png"]*3)
pula.extend([ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek7.png"]*2)
pula.extend( [r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek8.png"]*3)
pula.extend( [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek9.png"]*3)
test = [ r"E:\__priv\python\__pv\carcasonne\kafelki\kafeleka01.png"]*4






#do testowania, usun potem
del pula
pula = copy.deepcopy(test)

##


liczba_graczy =2
gracze = []

gracze.append(gracz.Gracz("bialy", "pierwszy"))
gracze.append(gracz.Gracz("niebieski", "drugi"))
#gracze.append(gracz.Gracz("czarny", "rudy"))



class GameView(arcade.View):
 
    def __init__(self):
        super().__init__()
        self.camera = None
        self.rozmiar_kafelka = 100
        self.poczatek_gry = True
        self.ui_poczatek = arcade.gui.UIManager()
        self.ulozenie_poczatku = arcade.gui.UIGridLayout(
            column_count=2, row_count=3, horizontal_spacing=0, vertical_spacing=20
        )
#do dorobienia ui poczatku gry - wpisywanie nazw uzytkwnikow i wybor kolorow

        self.ui_glowne = arcade.gui.UIManager()
        
        self.ulozenie_glowne = arcade.gui.UIGridLayout(
            column_count=2, row_count=liczba_graczy, horizontal_spacing=0, vertical_spacing=20
        )
        styl = arcade.gui.UIFlatButton.UIStyle(
                font_size=12,
                font_name="Arial",
                font_color=arcade.color.BLACK,
                bg=arcade.color.BLUE_GRAY,
                border=arcade.color.BLACK,
                border_width=1,
            )
        styl2 = arcade.gui.UIFlatButton.UIStyle(
                font_size=12,
                font_name="Arial",
                font_color=arcade.color.BLACK,
                bg=arcade.color.BLUE_GRAY,
                border=arcade.color.RED,
                border_width=3,
            )
        self.styl_pasywny = {
            "press": styl,
            "normal": styl,
            "hover": styl,
            "disabled": styl,
        }
        self.styl_aktywny  = {
            "press": styl2,
            "normal": styl2,
            "hover": styl2,
            "disabled": styl2,
        }
        self.tabela_ui_graczy =[]
       
        for i in range (liczba_graczy):
            
            tekst = f"l.pionkow: {gracze[i].pionki}\nPunkty: {gracze[i].punkty}"
            
            gracz_ =arcade.gui.UIFlatButton(text=gracze[i].id+"\n" + gracze[i].kolor, width=100, height=70, multiline=True,style=self.styl_pasywny)
            info = arcade.gui.UIFlatButton(text=tekst, width=150, height=70, multiline=True,style=self.styl_pasywny)
            self.tabela_ui_graczy.append([gracz_,info])

            
            self.ulozenie_glowne.add(gracz_,column=0, row=i)
            self.ulozenie_glowne.add(info,column=1, row=i)
        self.tabela_ui_graczy[0][0].style = self.styl_aktywny
        self.tabela_ui_graczy[0][1].style = self.styl_aktywny


        self.anchor_glowny = self.ui_glowne.add(arcade.gui.UIAnchorLayout())
        self.anchor_glowny.add(
                    anchor_x="left",
                    anchor_y="center_y",
                    align_y= -20,
                    child=self.ulozenie_glowne,
                )
        self.ui_glowne.enable()

        

        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()

   
        obrot_wskazowki = arcade.gui.UIFlatButton(text="obrot ->", width=100)
        obrot_przeciwnie = arcade.gui.UIFlatButton(text="<- obrot", width=100)
        self.pomin_kafelek = arcade.gui.UIFlatButton(text="pomin", width=100)

        czy_pominac_ture  = arcade.gui.UIFlatButton(text="nie kladz pionka", width=100)
        self.widget_wylosowany = None
        
        self.ulozenie = arcade.gui.UIGridLayout(
            column_count=2, row_count=1, horizontal_spacing=20, vertical_spacing=20
        )
        self.ulozenie.add(obrot_wskazowki, column=1, row=0)
        self.ulozenie.add(obrot_przeciwnie, column=0, row=0)



        @obrot_wskazowki.event("on_click")
        def obrot_wsk(event):
            self.sprite_wylosowany.angle += 90
            self.wylosowany_kafelek.obrot()

        @obrot_przeciwnie.event("on_click")
        def obrot_niewsk(event):
            
            self.sprite_wylosowany.angle += -90
            self.wylosowany_kafelek.obrot(wskazowki_zegara=False)
        @self.pomin_kafelek.event("on_click")
        def pomin(event):
            self.losuj_nowy_kafelek()
            self.nastepny_gracz()
        self.anchor = self.ui_manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(
                    anchor_x="center_x",
                    anchor_y="top",
                    align_y= -20,
                    child=self.ulozenie,
                )
        self.anchor.add(anchor_x="right",anchor_y="top",align_x=-10,align_y=-10, child= self.pomin_kafelek)
        
             
        self.ui_kladzenia_pionka = arcade.gui.UIManager()
        self.ui_kladzenia_pionka.enable()
        self.ulozenie2 = arcade.gui.UIGridLayout(
            column_count=1, row_count=1, horizontal_spacing=20, vertical_spacing=20
        )
        
        czy_pominac_ture  = arcade.gui.UIFlatButton(text="nie kladz pionka", width=200)
        self.ulozenie2.add(czy_pominac_ture,column=0,row=0)
        @czy_pominac_ture.event("on_click")
        def pomin(event):
            self.faza = fazy.KAFELEK
            self.ui_kladzenia_pionka.disable()
            self.nastepny_gracz()

        self.anchor2 =self.ui_kladzenia_pionka.add(arcade.gui.UIAnchorLayout())
        self.anchor2.add(
                    anchor_x="center_x",
                    anchor_y="top",
                    align_y= -20,
                    child=self.ulozenie2,
                )

        
        self.background_color = arcade.color.AMAZON
        self.czy_ruch_kamery = False
        self.nowa_pozycja_kamerery = (0, 0)
        self.polozone_kafelki = {}
        self.czy_losowac_nowy = True
        self.faza = fazy.KAFELEK
        self.swierzo_postawiony_kafelek = None
        self.aktywny_gracz = 0

        # If you have sprite lists, you should create them here,
        # and set them to None
    def setup(self):
        self.camera = arcade.Camera2D()
        self.tile_list = arcade.SpriteList()
        self.lista_pionkow = arcade.SpriteList()
        self.testowy_kafelek = None
        self.x_myszki , self.y_myszki = 0,0
        self.koniec_gry = False

        

  
        

        start = wszystkie_kafelki[r"E:\__priv\python\__pv\carcasonne\kafelki\kafelek1.png"]
        self.poloz_kafelek_na_siatce(start, 8, 5)
        
        # center_x/y to współrzędne w pikselach, nie w siatce logicznej!
        

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.window.use()
        self.ui_glowne.draw()
        self.camera.use()
        if self.koniec_gry:
            pass
        elif self.faza == fazy.KAFELEK:
            self.camera.use() # Aktywuje kamerę (wszystko poniżej rysuje się względem kamery)
            self.tile_list.draw()
            self.lista_pionkow.draw()
            
            
            self.window.use()
            self.ui_manager.enable()
            self.ui_manager.draw()
        elif self.faza == fazy.PIONEK:
            self.camera.use() # Aktywuje kamerę (wszystko poniżej rysuje się względem kamery)
            self.tile_list.draw()
            self.lista_pionkow.draw()
            self.swierzo_postawiony_kafelek.rysuj_hotspoty(meneger)
            self.window.use()
            self.ui_kladzenia_pionka.enable()
            self.ui_kladzenia_pionka.draw()
        self.camera.use()

        

        # Call draw() on all your sprite lists below
    def point_to_grid(self, x_screen, y_screen):
        world_x, world_y, _ = self.camera.unproject((x_screen, y_screen))
        x_grid = round(world_x / self.rozmiar_kafelka)
        y_grid = round(world_y / self.rozmiar_kafelka)
        return x_grid, y_grid

    def on_update(self, delta_time):
        if len(pula)==0 and self.faza == fazy.KAFELEK:
            self.koniec_gry = True
        if self.faza ==fazy.PIONEK:
            if not self.sprawdz_mozliwosc_polozenia_pionka(self.swierzo_postawiony_kafelek) or gracze[self.aktywny_gracz].pionki ==0:
                self.faza = fazy.KAFELEK
                self.nastepny_gracz()
        if self.czy_losowac_nowy:
            self.losuj_nowy_kafelek()
        if self.faza == fazy.KAFELEK:
            x_grid, y_grid = self.point_to_grid(self.x_myszki,self.y_myszki)
            gridy = self.get_sasiednie_gridy(x_grid, y_grid)
            if self.polozone_kafelki.get((x_grid,y_grid)):
                pass
            elif gridy ==[] or gridy is None:
                    
                    if self.testowy_kafelek is not None:
                        try:
                            self.tile_list.remove(self.testowy_kafelek)
                        except:pass
                        self.testowy_kafelek = None
            elif self.testowy_kafelek != self.wylosowany_kafelek.do_sprite(x_grid*100,y_grid*100):
                if self.testowy_kafelek is not None:
                    try:self.tile_list.remove(self.testowy_kafelek)
                    except:pass
               
                self.testowy_kafelek = self.wylosowany_kafelek.do_sprite(x_grid*100,y_grid*100)
                
                self.testowy_kafelek.alpha = 100
                
                self.tile_list.append(self.testowy_kafelek)
                gridy = []
        

    def on_key_press(self, key, key_modifiers):
        

        if self.faza == fazy.KAFELEK:
            if key == 100 or key ==65363:
                self.sprite_wylosowany.angle += 90
                self.wylosowany_kafelek.obrot()
            elif key == 97 or key == 65361:
                self.sprite_wylosowany.angle += -90
                self.wylosowany_kafelek.obrot(False)



           

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        
        #x_grid, y_grid = self.point_to_grid(x,y)
        self.x_myszki,self.y_myszki = x,y
        if self.czy_ruch_kamery:
            old_x, old_y = self.camera.position
            self.camera.position = (old_x - delta_x, old_y - delta_y)

      
        

    def on_mouse_press(self, x, y, button, key_modifiers):
        
        
        x_grid, y_grid = self.point_to_grid(x,y)
        world_x, world_y, _ = self.camera.unproject((x, y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.czy_ruch_kamery = True
            #self.nowa_pozycja_kamerery = (x, y)
        if button == arcade.MOUSE_BUTTON_LEFT:
            try:
                self.tile_list.remove(self.testowy_kafelek)
            except:
                pass
            
            if self.faza == fazy.KAFELEK:
                world_x, world_y, _ = self.camera.unproject((x, y))
                trafione_kafelki = arcade.get_sprites_at_point((world_x, world_y), self.tile_list)
                if len(trafione_kafelki) > 0:
                    
                    klikniety_sprite = trafione_kafelki[0]
                    if klikniety_sprite!= self.testowy_kafelek:
                        klikniety_sprite.color = arcade.color.RED
                else:
                    
                    
                    gridy = self.get_sasiednie_gridy(x_grid, y_grid)
                   
                    if gridy ==[] or gridy is None:
                        pass
                    else:
                        czy_mozna = True
                        for grid in gridy:
                            test = self.wylosowany_kafelek.poloz_kafelek(x_grid,y_grid)
                            if self.polozone_kafelki[grid].czy_mozna_polaczyc(test):
                                pass
                            else:
                                czy_mozna = False
                                break
                            del test
                        




                        if czy_mozna:           
                           
                            self.poloz_kafelek_na_siatce(self.wylosowany_kafelek, x_grid, y_grid)
                            self.losuj_nowy_kafelek()
                            
                            
                            
                            self.faza = fazy.PIONEK
                        gridy=[]
            elif self.faza == fazy.PIONEK:
              

                    pionek,kierunek = (self.swierzo_postawiony_kafelek.czy_nacisnieto_hotspot(world_x,world_y,czy_polozyc_pionek = gracze[self.aktywny_gracz].kolor, meneger= meneger))
                    
                    if pionek is not None:
                        if meneger.mapa[(x_grid,y_grid,kierunek)].zajeta is False:
                            sprite = pionek.do_sprite()
                            meneger.zajecie_struktury(x_grid,y_grid,kierunek,gracz = gracze[self.aktywny_gracz],pionek = [pionek])
                            self.lista_pionkow.append(sprite)
                            
                            
                            gracze[self.aktywny_gracz].pionki+= -1
                            self.faza = fazy.KAFELEK
                            self.nastepny_gracz()
    def losuj_nowy_kafelek(self):
        if len(pula)>0:
            idx = np.random.randint(0,len(pula))
            sciezka = pula.pop(idx)
            if self.widget_wylosowany:
                self.anchor.remove(self.widget_wylosowany)
            

            self.wylosowany_kafelek = wszystkie_kafelki[sciezka].poloz_kafelek(0,0)
            self.sprite_wylosowany = self.wylosowany_kafelek.do_sprite(0,0)
            self.widget_wylosowany = arcade.gui.UISpriteWidget(sprite=self.sprite_wylosowany)
            self.anchor.add(
                        anchor_x="center_x",
                        anchor_y="top",
                        align_y= -100,
                        child=self.widget_wylosowany,
                    )
            self.czy_losowac_nowy = False
        else:
            self.wylosowany_kafelek = None
            
            
            
    def sprawdz_mozliwosc_polozenia_pionka(self,kafelek):
        x_grid,y_grid = kafelek.grid_x, kafelek.grid_y
        kierunki = [naz.S,naz.W,naz.E,naz.N]
        for kierunek in kierunki:
            test = meneger.mapa.get((x_grid,y_grid,kierunek))
            if test is not None:
                if not test.zajeta:
                    return True
        return False 


      


    def on_mouse_release(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.czy_ruch_kamery = False
        if button == arcade.MOUSE_BUTTON_LEFT:
            for sprite in self.tile_list:
                if sprite != self.testowy_kafelek:
                    sprite.color = arcade.color.WHITE

    def poloz_kafelek_na_siatce(self, kaf, grid_x, grid_y):
        kafelek = kaf.poloz_kafelek(grid_x, grid_y)
        self.swierzo_postawiony_kafelek =kafelek
        meneger.polozenie_kafelka(kafelek,gracze)
       
        
        center_x = grid_x * self.rozmiar_kafelka 
        center_y = grid_y * self.rozmiar_kafelka 
        sprite = kafelek.do_sprite(center_x, center_y)
        
        self.tile_list.append(sprite)
        self.polozone_kafelki[(grid_x, grid_y)] = kafelek
    def get_sasiednie_gridy(self,x_grid,y_grid):
        tab =[]
        try: 
            test = self.polozone_kafelki[(x_grid+1,y_grid)]
            
        except:
            pass
        else:
            tab.append((x_grid+1,y_grid))
    

        try: 
            test = self.polozone_kafelki[(x_grid-1,y_grid)]
            
        except:
            pass
        else:
            tab.append((x_grid-1,y_grid))
        try: 
            test = self.polozone_kafelki[(x_grid,y_grid+1)]
            
        except:
            pass
        else:
            tab.append((x_grid,y_grid+1))
        try: 
            test = self.polozone_kafelki[(x_grid,y_grid-1)]
            
        except:
            pass
        else:
            tab.append((x_grid,y_grid-1))



        if tab ==[]:
            return None
        else:
            return tab





        
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        ZOOM_SPEED = 0.1
        if scroll_y > 0:
            # Kółko w górę -> Przybliżamy
            self.camera.zoom += ZOOM_SPEED
            
            
        elif scroll_y < 0:
            # Kółko w dół -> Oddalamy
            self.camera.zoom -= ZOOM_SPEED
            

        # Zabezpieczenie: Nie pozwól na zoom mniejszy niż 0.1 (odwrócony świat)
        if self.camera.zoom < 0.1:
            self.camera.zoom = 0.1
    def nastepny_gracz(self):
        self.aktywny_gracz +=1
        if self.aktywny_gracz == len(gracze):
            self.aktywny_gracz =0
        


        czy_zamkniete = True
        for segment in self.swierzo_postawiony_kafelek.polaczenia:
            x, y = self.swierzo_postawiony_kafelek.grid_x,self.swierzo_postawiony_kafelek.grid_y
            kierunek = segment["poloczenia"][0]
            strukt = meneger.mapa.get((x,y,kierunek))
            if strukt.czy_zamknieta and strukt.zajeta is not False:
                strukt.dodaj_punkty(gracze)
                for gracz in strukt.zajeta:
                    
                    gracz.pionki+= 1
                for pionek in strukt.pionki:
                    
                    self.lista_pionkow.remove(pionek.sprite)

        self.ui_kladzenia_pionka.disable()
        for idx,tab in enumerate(self.tabela_ui_graczy):
            
            
            tab[1].text = f"l.pionkow: {gracze[idx].pionki}\nPunkty: {gracze[idx].punkty}"
            if idx == self.aktywny_gracz:
                
                tab[0].style = self.styl_aktywny
                tab[1].style = self.styl_aktywny
            else:
                tab[0].style = self.styl_pasywny
                tab[1].style = self.styl_pasywny
        self.ui_glowne.trigger_render() 
       
            
            


            





def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(1000, 1000, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()




main()
for struktura in meneger.struktury:
    struktura.dodaj_punkty(gracze)
for gracz in gracze:
    print(gracz.id, " ",gracz.punkty)