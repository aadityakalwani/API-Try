import webbrowser


webbrowser.open("https://www.youtube.com")


def new_tab():
    webbrowser.open("https://www.google.com")


on = str(input("Press x to open a new tab: "))

if on.lower() == "x":
    new_tab()
