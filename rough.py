# import customtkinter as ctk

# class SidebarApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Sidebar Example")
#         self.geometry("800x600")

#         # Create sidebar frame
#         self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
#         self.sidebar.pack(side="left", fill="y", expand=False)

#         # Create main content area
#         self.main_content = ctk.CTkFrame(self)
#         self.main_content.pack(side="right", fill="both", expand=True)

#         # Create sidebar menu items
#         self.create_sidebar_item("General", ["Option 1", "Option 2"])
#         self.create_sidebar_item("Registration", ["Register", "Unregister"])
#         self.create_sidebar_item("Marketing", ["Campaigns", "Analytics"])
#         self.create_sidebar_item("Email", ["Compose", "Inbox", "Sent"])
#         self.create_sidebar_item("Attendees", ["List", "Groups"])
#         self.create_sidebar_item("Surveys", ["Feedback Surveys", "Responses"])
#         self.create_sidebar_item("Reports", ["Generate", "View"])
#         self.create_sidebar_item("Integrations", ["Connect", "Manage"])

#     def create_sidebar_item(self, label, subitems):
#         frame = ctk.CTkFrame(self.sidebar, corner_radius=0)
#         frame.pack(fill="x", pady=(0, 1))

#         button = ctk.CTkButton(frame, text=f"{label} ▼", anchor="w", command=lambda: self.toggle_subitems(frame, label,subitems))
#         button.pack(fill="x")

#         # Create hidden frame for subitems
#         subframe = ctk.CTkFrame(frame, corner_radius=0)
#         subframe.pack(fill="x")
#         subframe.pack_forget()  # Initially hidden

#         # Create buttons for subitems
#         for item in subitems:
#             sub_button = ctk.CTkButton(subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color=("gray70", "gray30"),text_color="red")
#             sub_button.pack(fill="x", pady=(0, 1))

#     def toggle_subitems(self, parent_frame, label, subitems):
#         button = parent_frame.winfo_children()[0]  # The main button
#         subframe = parent_frame.winfo_children()[1]  # The subframe
        
#         if subframe.winfo_viewable():
#             subframe.pack_forget()
#             button.configure(text=f"{label} ▼") #
#         else:
#             subframe.pack(fill="x", pady=(0, 5))
#             button.configure(text=f"{label} ▲") #button.cget('text').split()[0]

# # ... (rest of the code remains the same)
# if __name__ == "__main__":
#     app = SidebarApp()
#     app.mainloop()

import customtkinter as ctk

class SidebarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sidebar Example")
        self.geometry("800x600")

        # Create sidebar frame
        self.sidebar = ctk.CTkScrollableFrame(self, width=250, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", expand=False)

        # Create main content area
        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(side="right", fill="both", expand=True)

        # Create sidebar menu items
        self.create_sidebar_item("General", ["Option 1", "Option 2"])
        self.create_sidebar_item("Registration", ["Register", "Unregister"])
        self.create_sidebar_item("Marketing", ["Campaigns", "Analytics"])
        self.create_sidebar_item("Email", ["Compose", "Inbox", "Sent"])
        self.create_sidebar_item("Attendees", ["List", "Groups"])
        self.create_sidebar_item("Surveys", ["Feedback Surveys", "Responses"])
        self.create_sidebar_item("Reports", ["Generate", "View"])
        self.create_sidebar_item("Integrations", ["Connect", "Manage"])

    def create_sidebar_item(self, label, subitems):
        frame = ctk.CTkFrame(self.sidebar, corner_radius=0)
        frame.pack(fill="x", pady=(0, 1))

        # Create a sub-frame for the button content
        button_frame = ctk.CTkFrame(frame, corner_radius=0, fg_color="#20807f")
        button_frame.pack(fill="x")

        # Label on the left
        label_widget = ctk.CTkButton(button_frame, text=label, anchor="w", command= lambda : self.toggle_subitems(frame, label, subitems), fg_color="#20807f", text_color="white")
        label_widget.pack(side="left")

        # Arrow on the right
        self.arrow_label = ctk.CTkLabel(button_frame, text="▼", anchor="e")
        self.arrow_label.pack(side="right",padx=(0,5))

        # Make the whole frame clickable
        button_frame.bind("<Button-1>", lambda event: self.toggle_subitems(frame, label, subitems))

        # Create hidden frame for subitems
        subframe = ctk.CTkFrame(frame, corner_radius=20, fg_color="#093838")
        subframe.pack(fill="x")
        subframe.pack_forget()  # Initially hidden

    # Create buttons for subitems
        for item in subitems:
            sub_button = ctk.CTkButton(subframe, text=f"  • {item}", anchor="w", fg_color="transparent", hover_color=("gray70", "gray30"), text_color="white")
            sub_button.pack(fill="x")

    def toggle_subitems(self, parent_frame, label, subitems):
        subframe = parent_frame.winfo_children()[1]  # The subframe
        self.arrow_label = parent_frame.winfo_children()[0].winfo_children()[1]  # The arrow label
        
        if subframe.winfo_viewable():
            subframe.pack_forget()
            self.arrow_label.configure(text="▼")
        else:
            subframe.pack(fill="x")
            self.arrow_label.configure(text="▲")
# ... (rest of the code remains the same)
if __name__ == "__main__":
    app = SidebarApp()
    app.mainloop()