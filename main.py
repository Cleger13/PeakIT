import flet as ft 
import time

def main(page: ft.Page):
    page.title = "Registration Form"
    page.window_width = 400
    page.window_height = 450
    
    username = ft.TextField(label = "Usrname", width = 300)
    email = ft.TextField(label = "Email", width = 300)
    
    password = ft.TextField(label = "Password", password = True, width = 270)
    password_eye = ft.IconButton(icon = ft.icons.VISIBILITY_OFF,
                                 on_click = lambda e: toggle_password_visibility(password, password_eye))
    confirm_password = ft.TextField(label = "Confirm Password", password = True, width = 270)
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
            ft.Text("Registration Form", size = 24, weight = ft.FontWeight.BOLD),
            username,
            email,
            ft.Row([password, password_eye], alignment = ft.MainAxisAlignment.START),
            ft.Row([confirm_password, confirm_password_eye], alignment = ft.MainAxisAlignment.START),
            register_button,
        ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.START)
    )

ft.app(target = main)