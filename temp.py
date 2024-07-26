'''
Registration form Themes ; 
    theme_names = { "Gather" : 1,
                    "Serene" : 2,
                    "Twist" : 3,
                    "Vigor": 4,
                    "Glam" : 5,
                    "Cordial" : 6,
                    "Capital" : 7,
                    "Clean" : 8
                    }

    1. white, F4F4F4, #8FD3D8, #182261, #006AE1 : Ubuntu , Open Sans
    2. white, #F0F5F6, #FC6028, #393C53, #345A5E : Raleway , Roboto
    3. #FEF6F0, white, #F0629C, #572370, #9237A5 : Raleway , Roboto
    4. #ffffff, #fcefed, #ffdf3c, #e65722, #600000 : Oswald , Roboto
    5. #41154f, #352366, #4a5cb5, #dde2e6, #fcefed : Fredoka One, Roboto
    6. #d8e9ef, #fdfaff, #6fd7e6, #0b4f6c, #d50000 : Helvetica , Helvetica
    7. #e5e5e5, white, #0aaa4b, #003636, #007a7c : Old Standard TT , PT Sans
    8. #dde2e6, white, #f7f7f7, #273f69, #041532 : PT Sans, PT Sans

'''
import customtkinter as ctk

def switch_event():
    if switch_var.get() == "on":
        switch_text.set("Switch is On")
    else:
        switch_text.set("Switch is Off")

root = ctk.CTk()
root.geometry("300x150")

switch_var = ctk.StringVar(value="off")
switch_text = ctk.StringVar(value="Switch is Off")

switch = ctk.CTkSwitch(
    master=root,
    textvariable=switch_text,
    variable=switch_var,
    onvalue="on",
    offvalue="off",
    command=switch_event
)
switch.pack(padx=20, pady=10)

root.mainloop()






# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from ttkbootstrap.dialogs import Querybox
# import json

# class ThemeBuilder(ttk.Frame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#         self.master = master
#         self.current_theme = self.master.style.theme.name
#         self.create_widgets()

#     def create_widgets(self):
#         # Theme selection
#         ttk.Label(self, text="Select Theme:").pack(pady=5)
#         themes = self.master.style.theme_names()
#         self.theme_var = ttk.StringVar(value=self.current_theme)
#         theme_menu = ttk.OptionMenu(self, self.theme_var, self.current_theme, *themes, command=self.change_theme)
#         theme_menu.pack(pady=5)

#         # Color customization
#         ttk.Label(self, text="Customize Colors:").pack(pady=5)
#         self.color_buttons = {}
#         for color in ['primary', 'secondary', 'success', 'info', 'warning', 'danger']:
#             btn = ttk.Button(self, text=f"Change {color.capitalize()}", command=lambda c=color: self.change_color(c))
#             btn.pack(pady=2)
#             self.color_buttons[color] = btn

#         # Save and load themes
#         ttk.Button(self, text="Save Current Theme", command=self.save_theme).pack(pady=5)
#         ttk.Button(self, text="Load Theme", command=self.load_theme).pack(pady=5)

#     def change_theme(self, theme_name):
#         self.master.style.theme_use(theme_name)
#         self.current_theme = theme_name

#     def change_color(self, color_name):
#         current_color = self.master.style.colors.get(color_name, '#000000')
#         new_color = Querybox.get_color(parent=self, title=f"Choose {color_name} color", initialcolor=current_color)
#         if new_color:
#             self.master.style.configure(f'{color_name}.TButton', background=new_color)
#             self.color_buttons[color_name].configure(style=f'{color_name}.TButton')

#     def save_theme(self):
#         theme_data = {
#             'theme_name': self.current_theme,
#             'colors': self.master.style.colors
#         }
#         filename = Querybox.get_string(parent=self, title="Save Theme", prompt="Enter filename:")
#         if filename:
#             with open(f"{filename}.json", "w") as f:
#                 json.dump(theme_data, f)

#     def load_theme(self):
#         filename = Querybox.get_file(parent=self, title="Load Theme", filetypes=[("JSON Files", "*.json")])
#         if filename:
#             with open(filename, "r") as f:
#                 theme_data = json.load(f)
#             self.master.style.theme_use(theme_data['theme_name'])
#             for color, value in theme_data['colors'].items():
#                 self.master.style.configure(f'{color}.TButton', background=value)
#                 if color in self.color_buttons:
#                     self.color_buttons[color].configure(style=f'{color}.TButton')

# class App(ttk.Window):
#     def __init__(self):
#         super().__init__(themename="cosmo")  # Set the initial theme here
#         self.title("Theme Builder Example")
#         self.geometry("400x500")
        
#         self.theme_builder = ThemeBuilder(self)
#         self.theme_builder.pack(expand=YES, fill=BOTH, padx=10, pady=10)

#         # Example widgets to showcase theme changes
#         ttk.Button(self, text="Primary Button", style="primary.TButton").pack(pady=5)
#         ttk.Button(self, text="Secondary Button", style="secondary.TButton").pack(pady=5)
#         ttk.Entry(self).pack(pady=5)
#         ttk.Checkbutton(self, text="Check me").pack(pady=5)

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# import customtkinter as ctk
# import json
# from tkinter import colorchooser

# class ThemeCustomizer(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#         self.master = master
        
#         self.theme = {
#             "primary_color": "#4a90e2",
#             "background_color": "#f0f0f0",
#             "text_color": "#333333",
#             "button_color": "#4a90e2",
#             "button_hover_color": "#2980b9"
#         }
        
#         self.create_widgets()
    
#     def create_widgets(self):
#         self.title = ctk.CTkLabel(self, text="Theme Customizer")
#         self.title.pack(pady=10)
        
#         for key in self.theme:
#             frame = ctk.CTkFrame(self)
#             frame.pack(fill="x", padx=10, pady=5)
            
#             label = ctk.CTkLabel(frame, text=key.replace("_", " ").title())
#             label.pack(side="left")
            
#             button = ctk.CTkButton(frame, text="Choose Color", 
#                                    command=lambda k=key: self.choose_color(k))
#             button.pack(side="right")
        
#         self.apply_button = ctk.CTkButton(self, text="Apply Theme", 
#                                           command=self.apply_theme)
#         self.apply_button.pack(pady=10)
        
#         self.save_button = ctk.CTkButton(self, text="Save Theme", 
#                                          command=self.save_theme)
#         self.save_button.pack(pady=5)
        
#         self.load_button = ctk.CTkButton(self, text="Load Theme", 
#                                          command=self.load_theme)
#         self.load_button.pack(pady=5)
    
#     def choose_color(self, key):
#         color = colorchooser.askcolor(title=f"Choose {key.replace('_', ' ').title()}")
#         if color[1]:  # color is a tuple (RGB, hex)
#             self.theme[key] = color[1]
    
#     def apply_theme(self):
#         ctk.set_default_color_theme("blue")  # Reset to default theme
        
#         # Apply custom colors
#         ctk.set_widget_scaling(1)  # Adjust scaling if needed
#         ctk.set_appearance_mode("light" if self.is_light_theme() else "dark")
        
#         # Update colors for specific widget types
#         ctk.CTkLabel.configure(self, text_color=self.theme["text_color"])
#         ctk.CTkButton.configure(self, fg_color=self.theme["button_color"], 
#                                 hover_color=self.theme["button_hover_color"])
        
#         # Apply background color to the main window
#         self.master.configure(fg_color=self.theme["background_color"])
        
#         # You might need to update other widget types and recreate some widgets
#         # for changes to take full effect
    
#     def is_light_theme(self):
#         # Simple check to determine if the theme is light or dark
#         r, g, b = [int(self.theme["background_color"][i:i+2], 16) for i in (1, 3, 5)]
#         return (r*0.299 + g*0.587 + b*0.114) > 186
    
#     def save_theme(self):
#         with open("custom_theme.json", "w") as f:
#             json.dump(self.theme, f)
    
#     def load_theme(self):
#         try:
#             with open("custom_theme.json", "r") as f:
#                 self.theme = json.load(f)
#             self.apply_theme()
#         except FileNotFoundError:
#             print("No saved theme found.")

# # Example usage
# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.title("Theme Customizer Example")
#     root.geometry("400x500")
    
#     theme_customizer = ThemeCustomizer(root)
#     theme_customizer.pack(fill="both", expand=True)
    
#     root.mainloop()