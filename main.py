from kivy.app import App
from kivy.uix.button import Button
# from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class ChineseRestaurantApp(App):
    
    def build(self):
        layout = GridLayout(cols=1)
        
        menu_items = ['Фу-юань', 'Хушу', 'Жяодзи', 'Удон']
        
        for item in menu_items:
            btn = Button(text=item)
            layout.add_widget(btn)
        
        return layout

if __name__ == '__main__':
    ChineseRestaurantApp().run()