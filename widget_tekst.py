import arcade.gui

class RamkaInfo(arcade.gui.UIWidget):
    def __init__(self, text, width=200, height=100, bg_color=arcade.color.ALMOND, border_color=arcade.color.BROWN):
        # 1. Inicjalizacja widgetu
        super().__init__(width=width, height=height)
        self.bg_color = bg_color
        self.border_color = border_color
        
        # 2. Rozbijamy tekst na linie
        linie = text.split("\n")
        
        # 3. Tworzymy pionową listę (UIBoxLayout) dla linii tekstu
        # align="center" tutaj dotyczy ułożenia dzieci wewnątrz boxa w poziomie
        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=5, align="center")
        
        for linia in linie:
            label = arcade.gui.UILabel(
                text=linia,
                width=width,     # Szerokość etykiety taka jak ramki
                font_size=12,
                text_color=arcade.color.BLACK,
                font_name="Kenney Future",
                align="center"   # Wyśrodkowanie tekstu wewnątrz samej etykiety
            )
            v_box.add(label)

        # 4. Tworzymy wewnętrzny AnchorLayout, który posłuży do wycentrowania boxa w ramce
        self.layout = arcade.gui.UIAnchorLayout(width=width, height=height)
        
        # --- KLUCZOWA POPRAWKA ---
        # Dodajemy v_box do layoutu wyraźnie wskazując, że ma być na środku (center)
        self.layout.add(child=v_box, anchor_x="center_x", anchor_y="center_y")
        
        # 5. Dodajemy layout do widgetu
        self.add(self.layout)

    def on_draw(self):
        # Rysujemy tło
        arcade.draw_xywh_rectangle_filled(
            self._x, self._y, self._width, self._height, self.bg_color
        )
        # Rysujemy ramkę
        arcade.draw_xywh_rectangle_outline(
            self._x, self._y, self._width, self._height, 
            self.border_color, border_width=3
        )
        # Rysujemy dzieci (czyli tekst)
        super().on_draw()