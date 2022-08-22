from subprocess import run
from sys import exit

from requests import get

try:
    try:
        import PySimpleGUI as sg
    except:
        run(["pip", "install", "PySimpleGUI"])
        import PySimpleGUI as sg
    try:
        from bs4 import BeautifulSoup
    except:
        run(["pip", "install", "beautifulsoup4"])
        from bs4 import BeautifulSoup
    try:
        import html5lib
    except:
        run(["pip", "install", "html5lib"])
        import html5lib
except:
    from tkinter import messagebox

    messagebox.showerror(
        "Missing dependency", "Python3-pip may not be installed on your system."
    )
    exit("pip is not installed.")



def validate(url):
    page = "https://gavinisumanth.github.io/"
    if url[0 : len(page)] == "https://gavinisumanth.github.io/":
        for i in url[len(page) : -1]:
            if i.lower() not in "abcdefghijklmnopqrstuvwxyz":
                return False

        return True



custom_theme = {
    "BACKGROUND": "#003566",
    "TEXT": "#fef9ef",
    "INPUT": "#fef9ef",
    "TEXT_INPUT": "#001219",
    "SCROLL": "#17c3b2",
    "BUTTON": ("white", "#00afb9"),
    "PROGRESS": ("#01826B", "#D0D0D0"),
    "BORDER": 0,
    "SLIDER_DEPTH": 0,
    "PROGRESS_DEPTH": 0,
}
sg.theme_add_new("dark", custom_theme)
sg.theme("dark")

layout = [
    [sg.Text("Enter the site address", key="text")],
    [
        sg.Text("URL"),
        sg.Push(),
        sg.Text(":"),
        sg.InputText(key="url", enable_events=True),
    ],
    [sg.Button("Get"), sg.Push(), sg.Button("Quit")],
]

window = sg.Window(
    "Window Title",
    layout,
    no_titlebar=False,
    resizable=False,
    text_justification="left",
)
urls = []
while True:
    event, url_dict = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        window.close()
        break
    elif event == "Get":
        if validate(url_dict["url"]):
            urls.append(url_dict["url"])
            window["url"].update("")
            sg.popup_notify(
                "Press Quit to start download",
                display_duration_in_ms=800,
                fade_in_duration=30,
            )
            window["text"].update("Enter another URL:")
        else:
            window["text"].update("Entered URL is invalid.Enter another URL:")

print(f"Entered URL list:{urls}")
for url in urls:
    try:
        x = get(url)
    except:
        print("Network Error")
    else:
        soup = BeautifulSoup(x.content, "html5lib")
        table = soup.find("p", attrs={"id": "content"})
        with open("temp.html", "w") as file:
            file.write(str(table))
        name = url[len("https://gavinisumanth.github.io/") : len(".html")] + ".azw3"
        run(["ebook-convert", "temp.html", name])
