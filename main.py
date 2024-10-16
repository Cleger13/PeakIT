#import flet as ft


# # Список меню
# menu_items = [
#     {"name": "Куриный суп", "price": 200},
#     {"name": "Утия с овощами", "price": 350},
#     {"name": "Лапша с морепродуктами", "price": 400},
#     {"name": "Чай зеленый", "price": 100},
# ]

# class RestaurantApp(ft.UserControl):
#     def build(self):
#         self.order_list = ft.ListView()

#         # Создаем карточки для каждого элемента меню
#         menu_cards = []
#         for item in menu_items:
#             card = ft.Card(
#                 content=ft.Row([
#                     ft.Column([
#                         ft.Text(item["name"], size=20, weight="bold"),
#                         ft.Text(f"{item['price']} ₽", color=ft.colors.GREEN_600)
#                     ], alignment=ft.MainAxisAlignment.START),
#                     ft.ElevatedButton("Добавить", on_click=self.add_to_order(item))
#                 ]),
#                 padding=10,
#                 margin=5
#             )
#             menu_cards.append(card)

#         # Возвращаем основной интерфейс
#         return ft.Column(
#             [
#                 ft.Text("Меню ресторана", size=24, weight="bold"),
#                 ft.Column(menu_cards),
#                 ft.Text("Ваш заказ:", size=24, weight="bold"),
#                 self.order_list,
#                 ft.ElevatedButton("Оформить заказ", on_click=self.place_order),
#             ],
#             alignment=ft.MainAxisAlignment.START,
#         )

#     def add_to_order(self, item):
#         # Функция добавления заказа
#         def handler(e):
#             self.order_list.add(ft.Text(f"{item['name']} - {item['price']} ₽", size=16))
#         return handler

#     def place_order(self, e):
#         # Функция подтверждения заказа
#         order_summary = "\n".join([order.value for order in self.order_list.controls])
#         if order_summary:
#             ft.snack_bar.SnackBar(
#                 content=ft.Text("Ваш заказ оформлен:\n" + order_summary),
#                 open=True
#             ).show()
#         else:
#             ft.snack_bar.SnackBar(
#                 content=ft.Text("Ваш заказ пуст!"),
#                 open=True
#             ).show()

# def main(page):
#     page.title = "Китайский Ресторан"
#     page.vertical_alignment = ft.MainAxisAlignment.START
#     page.add(RestaurantApp())

# ft.app(target=main)


import flet as ft 
import time

def main(page: ft.Page):
    page.title = "Registration Form"
    page.window_width = 400
    page.window_height = 450
    
    username = ft.TextField(label = "Usrname", width = 300)
    email = ft.TextField(label = "Email", width = 300)
    
    password = ft.TetField(label = "Password", password = True, width = 270)
    password_eye = ft.IconButton(icon = ft.icons.VISIBILITY_OFF,
                                 on_click = lambda e: toggle_password_visibility(password, password_eye))
    confirm_password = ft.TetField(label = "Confirm Password", password = True, width = 270)
    confirm_password_eye = ft.IconButton(icon = ft.icons.VISIBILITY_OFF,
                                 on_click = lambda e: toggle_password_visibility(confirm_password,
                                                                                 confirm_password_eye))
    
    def toggle_password_visibility(field, eye_button):
        if field.password:
            field.password = False
            eye_button.icon = ft.icons.VISIBILITY
        else:
            field.password = True
            eye_button.icon = ft.icons.VISIBILITY_OFF
        page.update()

    def register(e):
        loading_text = ft.Text("Processing data...", size = 18)
        progress_bar = ft.ProgressBar(width = 300)
        page.add(ft.Column([loading_text, progress_bar], alignment = ft.MainAxisAlignment.CENTER))
        page.update()
        
        time.sleep(2)
        
        page.controls.pop()
        page.update()
        
        if password.value != confirm_password.value:
            def close_dialog(e):
                page.dialog.open = False
                page.update()
            
            page.dialog = ft.AlertDialog(
                title = ft.Text("Error"),
                content = ft.Text("Passwords do not match!"),
                actions = [ft.TextButton("OK", on_click = close_dialog)],
            )
            
            page.dialog.open = True
            page.update()
            
        else:
            def close_dialog(e):
                page.dialog.open = False
                page.update()
            
            page.dialog = ft.AlertDialog(
                title = ft.Text("Success"),
                content = ft.Text("Registration successful!"),
                actions = [ft.TextButton("OK", on_click = close_dialog)],
            )
            
            page.dialog.open = True
            page.update()
    
    register_button = ft.ElevatedButton("Register", on_click = register)
    
    page.add(
        ft.Column([
            ft.Text("Regitration Form", size = 24, weight = ft.FontWeight.BOLD),
            username,
            email,
            ft.Row([password, password_eye], alignment = ft.MainAxistAlignment.START),
            ft.Row([confirm_password, confirm_password_eye], alignment = ft.MainAxistAlignment.START),
            register_button,
        ],
            alignment = ft.MainAxistAlignment.CENTER,
            horizontal_aligment = ft.CrossAxisAlignment.START)
    )

ft.app(target = main )