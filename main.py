import webbrowser


website_name = str(input("Enter the website you want to open: "))


def new_tab():
    webbrowser.open(f"https://www.{website_name}.com")


new_tab()
