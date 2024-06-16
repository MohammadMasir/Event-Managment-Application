hide_sidebar = True   # Sidebar control variable
def butimg6():
    global hide_sidebar         # Defined global variable
    if hide_sidebar:
        show_sidebar()
    else:
        hide_sidebar

def show_sidebar():
    global hide_sidebar    # Defined global variable
    hide_sidebar = False
    for i in range(-300,0,10):
        sidebar_frame.place(x=i, y=0)
        f3.update()
        f3.after(10)

def hide_sidebar():
    global hide_sidebar
    hide_sidebar = True
    for i in range(0, -300, -10):
        sidebar_frame.place(x=i, y=0)
        f3.update()
        f3.after(10)
