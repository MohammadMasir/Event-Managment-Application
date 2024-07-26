import customtkinter as ctk
import requests
from tkinter import StringVar, Listbox, END
import threading
import queue

class LocationSearch(ctk.CTkFrame):
    def __init__(self, main, parent_frame):
        super().__init__(parent_frame)
        self.main = main
        self.parent = parent_frame

        self.entry_widget()
        self.suggestion_queue = queue.Queue()
        self.after(100, self.check_suggestion_queue)

    def entry_widget(self):
        self.entry_var = StringVar()
        self.entry_var.trace_add("write", self.debounce_update_suggestions)
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, width=400)
        self.entry.pack()

        self.sc_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.sc_frame.pack(fill="x")
        self.sc_frame.pack_forget()

        self.entry.bind("<FocusIn>", self.show_suggestions)

        self.listbox = Listbox(self.sc_frame)
        self.listbox.pack(fill="both", expand=True)

        self.debounce_timer = None
        self.cache = {}

    def show_suggestions(self, event):
        self.sc_frame.pack(fill="x", expand=True, pady=20, padx=20)

    def debounce_update_suggestions(self, *args):
        if self.debounce_timer is not None:
            self.after_cancel(self.debounce_timer)
        self.debounce_timer = self.after(300, self.update_suggestions)

    def update_suggestions(self):
        query = self.entry_var.get()
        if query:
            if query in self.cache:
                self.display_suggestions(self.cache[query])
            else:
                threading.Thread(target=self.fetch_suggestions, args=(query,), daemon=True).start()
        else:
            self.listbox.delete(0, END)

    def fetch_suggestions(self, query):
        suggestions = get_autocomplete_suggestions(query)
        self.cache[query] = suggestions
        self.suggestion_queue.put(suggestions)

    def check_suggestion_queue(self):
        try:
            suggestions = self.suggestion_queue.get_nowait()
            self.display_suggestions(suggestions)
        except queue.Empty:
            pass
        finally:
            self.after(100, self.check_suggestion_queue)

    def display_suggestions(self, suggestions):
        self.listbox.delete(0, END)
        for suggestion in suggestions:
            self.listbox.insert(END, suggestion)
        if suggestions:
            self.sc_frame.pack(fill="x", expand=True, pady=20, padx=20)
        else:
            self.sc_frame.pack_forget()

    def get_selected_venue(self):
        return self.entry_var.get()

def get_autocomplete_suggestions(query):
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q": query,
                "format": "json",
                "addressdetails": 1,
                "limit": 20,
            },
            headers={
                "User-Agent": "Event_management"  # Replace with your app name and email
            }
        )
        result = response.json()
        suggestions = [place['display_name'] for place in result]
        return suggestions
    except Exception as e:
        print(f"An error occurred: {e}")
        return []