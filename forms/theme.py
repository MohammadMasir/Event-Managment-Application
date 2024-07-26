import customtkinter as ctk 
from PIL import Image
import tkinter as tk 
import json

class ThemeDesigner():
    def __init__(self, parent_frame, form, number):
        super().__init__()
        self.form = form
        self.parent = parent_frame
        self.apply = None
        self.no = number

    def back(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        self.Theme_structure()

    def theme_change(self, colors):
        primary_text_color = colors[-2]
        secondary_text_color = colors[-1]
        bg = colors[0]
        entry_bg = colors[1]

        upper_text = primary_text_color
        frame_color = primary_text_color
        border_color = primary_text_color
        lower_text = secondary_text_color
        background = bg
        entries_fg = entry_bg

        # Save the current theme configuration
        self.current_theme = {
            "primary_text_color": primary_text_color,
            "secondary_text_color": secondary_text_color,
            "background": bg,
            "entry_background": entry_bg,
            "frame_color": frame_color,
            "border_color": border_color
        }

        if self.no == 1:
            self.form.main_scrollable_frame.configure(fg_color=entries_fg)
            self.form.blue_frame.configure(fg_color=frame_color)
            self.form.upper_frame.configure(fg_color=background)
            self.form.lower_frame.configure(fg_color=background)
            self.form.demeven.configure(text_color=upper_text)
            self.form.date.configure(text_color=upper_text)
            self.form.venue.configure(text_color=upper_text)
            self.form.time.configure(text_color=lower_text)
            self.form.location.configure(text_color=lower_text)
            self.form.personal.configure(text_color=lower_text)
            self.form.mandatory.configure(text_color=upper_text)
            self.form.first_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.last_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.email_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.mobile_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.company_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.title_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.cancel.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.next.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)
        elif self.no == 2:
            self.form.main_scrollable_frame.configure(fg_color=entries_fg)
            self.form.blue_frame.configure(fg_color=frame_color)
            self.form.demeven.configure(text_color=upper_text)
            self.form.date.configure(text_color=upper_text)
            self.form.venue.configure(text_color=upper_text)
            self.form.time.configure(text_color=lower_text)
            self.form.location.configure(text_color=lower_text)
            self.form.slider.configure(progress_color=upper_text)
            self.form.personal.configure(text_color=lower_text)
            self.form.mandatory.configure(text_color=upper_text)
            self.form.email.configure(text_color=upper_text)
            self.form.name.configure(text_color=upper_text)
            self.form.edit_button.configure(text_color=lower_text)
            self.form.company.configure(text_color=upper_text)
            self.form.company_name.configure(text_color=upper_text)
            self.form.title.configure(text_color=upper_text)
            self.form.title_name.configure(text_color=upper_text)
            self.form.questions.configure(text_color=lower_text)
            self.form.agenda.configure(text_color=lower_text)
            self.form.item_button.configure(text_color=lower_text)
            self.form.addmission_item.configure(text_color=lower_text)
            self.form.previous.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.cancel.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.submit.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)

        elif self.no == 3:
            self.form.main_scrollable_frame.configure(fg_color=entries_fg)
            self.form.blue_frame.configure(fg_color=frame_color)
            self.form.demeven.configure(text_color=upper_text)
            self.form.logout_button.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)
            self.form.date.configure(text_color=upper_text)
            self.form.venue.configure(text_color=upper_text)
            self.form.time.configure(text_color=lower_text)
            self.form.location.configure(text_color=lower_text)
            self.form.registerr.configure(text_color=lower_text)
            self.form.confirmation_number_label.configure(text_color=upper_text)
            self.form.confirmation_number_value.configure(text_color=lower_text)
            self.form.receive_email_label.configure(text_color=lower_text)
            self.form.add_to_calendar_b.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.see_you_in_label.configure(text_color=upper_text)
            self.form.modify_registration_button.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)
            self.form.cancel_registration_button.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)

        elif self.no == 4:
            self.form.main_scrollable_frame.configure(fg_color=entries_fg)
            self.form.blue_frame.configure(fg_color=frame_color)
            self.form.demeven.configure(text_color=upper_text)
            self.form.date.configure(text_color=upper_text)
            self.form.venue.configure(text_color=upper_text)
            self.form.time.configure(text_color=lower_text)
            self.form.location.configure(text_color=lower_text)
            self.form.sorry_label.configure(text_color=lower_text)
            self.form.mandatory_filling.configure(text_color=upper_text)
            self.form.first_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.last_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.email_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.mobile_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.company_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.title_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.reason_label.configure(text_color=lower_text)
            self.form.reason_input_box.configure(fg_color=entries_fg, border_color=border_color)
            self.form.cancel_button.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.submit_button.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)

        elif self.no == 5:
            self.form.main_scrollable_frame.configure(fg_color=entries_fg)
            self.form.blue_frame.configure(fg_color=frame_color)
            self.form.demeven.configure(text_color=upper_text)
            self.form.date.configure(text_color=upper_text)
            self.form.venue.configure(text_color=upper_text)
            self.form.time.configure(text_color=lower_text)
            self.form.location.configure(text_color=lower_text)
            self.form.sorry_label.configure(text_color=lower_text)
            self.form.mandatory_filling.configure(text_color=upper_text)
            self.form.first_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.last_name_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.email_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.mobile_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.company_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.title_entry.configure(fg_color=entries_fg, border_color=border_color)
            self.form.reason_label.configure(text_color=lower_text)
            self.form.reason_input_box.configure(fg_color=entries_fg, border_color=border_color)
            self.form.cancel_button.configure(fg_color=background, border_color=lower_text, text_color=lower_text)
            self.form.submit_button.configure(fg_color=lower_text, border_color=lower_text, text_color=entries_fg)

    def theme_color_palette(self, theme_name, color_names, font):
        ctk.CTkLabel(self.parent, text=theme_name, font=ctk.CTkFont(size=15, family="Segoue UI", weight="bold")).pack(anchor="nw", pady=(10,0),padx=(15,0))
        theme_frame = tk.Frame(self.parent, borderwidth=3, relief="raised", bg="#FDFDFD")
        theme_frame.pack(fill="x", padx=20, pady=10)

        color_frame = ctk.CTkFrame(theme_frame, fg_color=color_names[0], height=40)
        color_frame.pack(fill="both")

        options_frame = ctk.CTkFrame(theme_frame, fg_color="transparent")
        options_frame.pack(fill="both")

        apply = ctk.CTkButton(theme_frame, text="Apply", fg_color="khaki", border_color="wheat", text_color="black", 
                            command=lambda c=color_names: self.theme_change(c), hover_color="palegoldenrod")
        apply.pack(anchor="center", pady=5)

        colors_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        colors_frame.pack(anchor="center")

        for colors in color_names:
            ctk.CTkButton(colors_frame, text="", fg_color=colors, border_width=2, border_color="#D9DCDE", width=20, height=20).pack(side="left", padx=(5,0), pady=(5,0))

    def change_theme_command(self):
        for widget in self.parent.winfo_children():
            widget.pack_forget()
        top_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        top_frame.pack(fill="x", expand=True)
        ctk.CTkLabel(top_frame, text="Standard Themes", font=ctk.CTkFont(size=25, family="Segoue UI", weight="bold")).pack(side="left",anchor="nw", pady=(10,0))

        imag = ctk.CTkImage(dark_image= Image.open(r"pics\back.png"), size=(15,15))
        back_butt = ctk.CTkButton(top_frame, text="", image=imag, fg_color="#F0F0F0", command=self.back, width=60,height=20)
        back_butt.pack(side="right",anchor="ne", pady=(10,0), padx=(0,5))

        line = self.common_line()
        line.pack(pady=10)
        self.theme_color_palette("Gather", ["white", "white smoke", "#8FD3D8", "#182261", "#006AE1"], "Open Sans")
        self.theme_color_palette("Serene", ["white", "#F0F5F6", "#FC6028", "#393C53", "#345A5E"], "Roboto")
        self.theme_color_palette("Twist", ["#FEF6F0", "white", "#F0629C", "#572370", "#9237A5"], "Roboto")
        self.theme_color_palette("Vigor", ["white", "#fcefed", "#ffdf3c", "#e65722", "#600000"], "Roboto")
        self.theme_color_palette("Glam", ["#41154f", "#352366", "#4a5cb5", "#dde2e6", "#fcefed"], "Roboto")
        self.theme_color_palette("Cordial", ["#d8e9ef", "#fdfaff", "#6fd7e6", "#0b4f6c", "#d50000"], "Helvetica")
        self.theme_color_palette("Capital", ["#e5e5e5", "white", "#0aaa4b", "#003636", "#007a7c"], "PT Sans")
        self.theme_color_palette("Clean", ["#dde2e6", "white", "#f7f7f7", "#273f69", "#041532"], "PT Sans")

    def add_image_command(self):
        pass

    def edit_image_command(self):
        pass
    
    def finished_command(self):
        pass


    def save_theme(self):
        if not self.current_theme:
            print("No theme has been applied yet.")
            return

        theme_name = ctk.CTkInputDialog(title="Save Theme", text="Enter a name for this theme:").get_input()
        if not theme_name:
            print("Theme name is required.")
            return

        theme_data = {
            "form_type" : self.form_type,
            "name": theme_name,
            "colors": self.current_theme
        }

        try:
            with open("saved_themes.json", "r") as f:
                saved_themes = json.load(f)
        except FileNotFoundError:
            saved_themes = []

        saved_themes.append(theme_data)

        with open("saved_themes.json", "w") as f:
            json.dump(saved_themes, f, indent=2)

        print(f"Theme '{theme_name}' has been saved successfully.")

    def load_saved_themes(self):
        try:
            with open("saved_themes.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def show_saved_themes(self):
        saved_themes = self.load_saved_themes()
        if not saved_themes:
            print("No saved themes found.")
            return

        themes_window = ctk.CTkToplevel(self.parent)
        themes_window.title("Saved Themes")

        for theme in saved_themes:
            theme_frame = ctk.CTkFrame(themes_window)
            theme_frame.pack(pady=10, padx=10, fill="x")

            ctk.CTkLabel(theme_frame, text=theme["name"]).pack(side="left", padx=10)
            
            apply_button = ctk.CTkButton(
                theme_frame, 
                text="Apply", 
                command=lambda t=theme["colors"]: self.apply_saved_theme(t)
            )
            apply_button.pack(side="right", padx=10)

    def apply_saved_theme(self, theme_colors):
        colors = [
            theme_colors["background"],
            theme_colors["entry_background"],
            theme_colors["frame_color"],
            theme_colors["primary_text_color"],
            theme_colors["secondary_text_color"]
        ]
        self.theme_change(colors)

    def common_line(self):
        canvas = tk.Canvas(self.parent,height = 1,bg = "lightgray",relief = tk.SUNKEN)
        return canvas

    def back_reg(self):
        self.form.main_scrollable_frame.pack_forget()
        self.parent.pack_forget()

        self.form.register_page.registration_proccess()

    def Theme_structure(self):
        top_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        top_frame.pack(fill="x", expand=True, ipady=10)
        self.theme = ctk.CTkLabel(top_frame,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 25,weight = "bold"))
        self.theme.pack(side="left", padx=(120,0))

        imag = ctk.CTkImage(dark_image= Image.open(r"pics\close.png"), size=(15,15))
        back_butt = ctk.CTkButton(top_frame, text="", image=imag, fg_color="#F0F0F0", command=self.back_reg, width=40,height=20)
        back_butt.pack(side="right",anchor="ne", padx=(0,5), pady=(20,0))

        self.line1 = self.common_line()
        self.line1.pack()

        frame1 = ctk.CTkFrame(self.parent, fg_color="transparent")
        frame1.pack(fill="x", expand=True)

        self.quick_setup = ctk.CTkLabel(frame1,text = "Quick Setup",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.quick_setup.pack(anchor="nw", padx=10)

        label_frame = ctk.CTkFrame(frame1, fg_color="transparent")
        label_frame.pack(fill="x")

        self.visual_theme = ctk.CTkLabel(label_frame,text = "Create a visual theme for your website and",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.visual_theme.pack(anchor="nw", padx=10) #registration pages.

        ctk.CTkLabel(label_frame, text="registration pages.", text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal")).pack(side="top",anchor="nw", padx=10)

        self.theme_button_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.theme_button_frame.pack(pady=20, fill="x")

        self.change_theme = ctk.CTkLabel(self.theme_button_frame,text = "Theme",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.change_theme.pack(side="left", padx=(10,0))

        self.change_theme_button = ctk.CTkButton(self.theme_button_frame,text = "Change Theme",height = 30,width = 110,corner_radius = 12,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.change_theme_command)
        self.change_theme_button.pack(side="right", padx=(0,10))

        self.line2 = self.common_line()
        self.line2.pack()

        frame2 = ctk.CTkFrame(self.parent, fg_color="transparent")
        frame2.pack(fill="x", expand=True)

        self.logo = ctk.CTkLabel(frame2,text = "Logo",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.logo.grid(row = 6,column = 0,sticky = "nw",padx = (10,0))

        self.logo_image_label = ctk.CTkLabel(frame2,text = "Logo Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.logo_image_label.grid(row = 7,column = 0,sticky = "nw",padx = (10,0),pady = (10,0))

        self.rectangle_frame = ctk.CTkFrame(frame2,height = 100,width = 270,border_width = 1,fg_color = "#ffffff",border_color = "lightgray")
        self.rectangle_frame.grid(row = 8,column = 0,sticky = "nw",padx = (10,0),pady = (0,20))

        self.add_image = ctk.CTkImage(dark_image = Image.open(r"pics\gallery.png"),size = (20,20))
        self.add_image_button = ctk.CTkButton(self.rectangle_frame,image = self.add_image,text = "",height = 10,width = 20,fg_color = "#ffffff",hover_color = "lightgray",command = self.add_image_command)
        self.add_image_button.place(x = 120,y = 30)

        self.add_image_label = ctk.CTkLabel(self.rectangle_frame,text = "Add Image",text_color = "#11A2E3",fg_color = "#ffffff")
        self.add_image_label.place(x = 110, y = 57)

        self.line3 = self.common_line()
        self.line3.pack()

        frame3 = ctk.CTkFrame(self.parent, fg_color="transparent")
        frame3.pack(fill="x", expand=True)

        self.header_background =  ctk.CTkLabel(frame3,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 20,weight = "bold"))
        self.header_background.grid(row = 10,column = 0,sticky = "nw",padx = (10,0))

        self.header_background_image =  ctk.CTkLabel(frame3,text = "Header Background Image",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "normal"))
        self.header_background_image.grid(row = 11,column = 0,sticky = "nw,",padx = (10,0),pady = (10,0))

        self.header_background_frame = ctk.CTkFrame(frame3,height = 200,width = 270,border_width = 1,fg_color = "#000000",border_color = "lightgray")
        self.header_background_frame.grid(row = 12,column = 0,sticky = "nw",padx = (10,0),pady = 0)

        self.edit_image = ctk.CTkButton(frame3,text = "Edit Image",height = 30,width = 250,corner_radius = 5,border_width = 1,border_color = "#11A2E3",text_color = "#11A2E3",fg_color = "#ffffff",hover_color = "blue",command = self.edit_image_command)
        self.edit_image.grid(row = 13,column = 0,padx = 40,pady = (5,10))

        self.line4 = self.common_line()
        self.line4.pack()

        frame4 = ctk.CTkFrame(self.parent, fg_color="transparent")
        frame4.pack(fill="x", expand=True)

        self.colors = ctk.CTkLabel(frame4,text = "Save & Generate URL",text_color = "#000000",font = ctk.CTkFont(size = 15,weight = "bold"))
        self.colors.grid(row = 15,column = 0,sticky = "nw",padx = (10,0))

        self.save_button = ctk.CTkButton(frame4, text="Save Theme", command=self.save_theme)
        self.save_button.grid(row=16, column=0, padx=40, pady=(10,5))

        self.show_saved_button = ctk.CTkButton(frame4, text="Show Saved Themes", command=self.show_saved_themes)
        self.show_saved_button.grid(row=17, column=0, padx=40, pady=5)

        self.finished = ctk.CTkButton(frame4, text="SAVE", height=30, width=250, corner_radius=5, border_width=1, border_color="#11A2E3", text_color="#11A2E3", fg_color="#ffffff", hover_color="blue", command=self.finished_command)
        self.finished.grid(row=18, column=0, padx=40, pady=(5,20))

        if self.no == 1:
            self.form_type = 1
        elif self.no == 2:
            self.form_type = 2
        elif self.no == 3:
            self.form_type = 3
        elif self.no == 4:
            self.form_type = 4
        elif self.no == 5:
            self.form_type = 5