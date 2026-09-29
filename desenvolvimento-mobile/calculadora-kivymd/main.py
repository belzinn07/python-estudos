from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        layout_principal = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.label = Label(text="0", color=self.theme_cls.primary_color)
        botao1 = Button(text="1", on_press=self.clicou_numero, font_size=24)
        botao2 = Button(text="2", on_press=self.clicou_numero, font_size=24)
        botao3 = Button(text="3", on_press=self.clicou_numero, font_size=24)
        botao4 = Button(text="4", on_press=self.clicou_numero, font_size=24)
        botao5 = Button(text="5", on_press=self.clicou_numero, font_size=24)
        botao6 = Button(text="6", on_press=self.clicou_numero, font_size=24)
        botao7 = Button(text="7", on_press=self.clicou_numero, font_size=24)
        botao8 = Button(text="8", on_press=self.clicou_numero, font_size=24)
        botao9 = Button(text="9", on_press=self.clicou_numero, font_size=24)
        botao0 = Button(text="0", on_press=self.clicou_numero, font_size=24)
        botao_soma = Button(text="+", on_press=self.clicou_numero, font_size=24,background_color=(0, 0, 0, 0.5), color= (0,0,1,1))  
        botao_subtracao = Button(text="-", on_press=self.clicou_numero, font_size=24,background_color=(0, 0, 0, 0.5), color= (0,0,1,1))
        botao_multiplicao = Button(text="x", on_press=self.clicou_numero, font_size=24,background_color=(0, 0, 0, 0.5), color= (0,0,1,1))
        botao_divisao = Button(text="÷", on_press=self.clicou_numero, font_size=24,background_color=(0, 0, 0, 0.5), color= (0,0,1,1))
        botao_resultado = Button(text="=", on_press=self.clicou_numero, font_size=24, background_color=(0, 0, 1, 1))
        layout_principal.add_widget(self.label)
        
        layout_primeira_linha = BoxLayout(orientation="horizontal", spacing=10)
        layout_primeira_linha.add_widget(botao7)
        layout_primeira_linha.add_widget(botao8)
        layout_primeira_linha.add_widget(botao9)
        layout_primeira_linha.add_widget(botao_multiplicao)
        layout_principal.add_widget(layout_primeira_linha)
        
        layout_segunda_linha = BoxLayout(orientation="horizontal", spacing=10)
        layout_segunda_linha.add_widget(botao4)
        layout_segunda_linha.add_widget(botao5)
        layout_segunda_linha.add_widget(botao6)
        layout_segunda_linha.add_widget(botao_divisao)
        layout_principal.add_widget(layout_segunda_linha)

        layout_terceira_linha = BoxLayout(orientation="horizontal", spacing=10)     
        layout_terceira_linha.add_widget(botao1)
        layout_terceira_linha.add_widget(botao2)
        layout_terceira_linha.add_widget(botao3)
        layout_terceira_linha.add_widget(botao_soma)
        layout_principal.add_widget(layout_terceira_linha)

        layout_quarta_linha = BoxLayout(orientation="horizontal", spacing=10)
        layout_quarta_linha.add_widget(botao_resultado)
        layout_quarta_linha.add_widget(botao0)
        layout_quarta_linha.add_widget(botao_subtracao)
        layout_principal.add_widget(layout_quarta_linha)

        return layout_principal

    def clicou_numero(self, instance):
        self.label.text = instance.text

if __name__ == "__main__":
    CalculadoraApp().run()

