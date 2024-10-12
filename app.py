from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkScrollableFrame, set_appearance_mode
from PIL import Image
from galeria import show_content, show_gallery, update_main_image, clear_frame
from categorias import (explorar_praia, explorar_bares, explorar_restaurantes, 
                        explorar_trilhas, explorar_cultura, explorar_lagoas, 
                        explorar_boates, explorar_hoteis_e_pousados, explorar_estacionamento)


# Configurar modo claro/ escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

    transparent_windows = [header, menu_frame, search_frame]

    for component in transparent_windows:
        component.configure(fg_color=app.cget("bg"))

# Lógica da Pesquisa
def search_action(query):
    all_items = (explorar_praia()[1] + explorar_bares()[1] + explorar_restaurantes()[1] 
                 + explorar_trilhas()[1] + explorar_cultura()[1] + explorar_lagoas()[1] 
                 + explorar_boates()[1] + explorar_hoteis_e_pousados()[1] + explorar_estacionamento()[1])

    # Filtrar os itens apenas se a query não estiver vazia
    if query.strip():
        filtered_items = [item for item in all_items if query.lower() in item["name"].lower()]
    else:
        filtered_items = []

    global normal_frame

    if normal_frame is not None:
        normal_frame.destroy()
        normal_frame = None
        
    show_content(main_frame, filtered_items, app)


# Carrega os ícones diretamente da pasta "icons"
def load_icons():
    icons = {
        "home": CTkImage(Image.open("icons/home.png"), size=(25, 25)),
        "explorar": CTkImage(Image.open("icons/explorar.png"), size=(25, 25)),
        "favoritos": CTkImage(Image.open("icons/favorito.png"), size=(25, 25)),
        "opcoes": CTkImage(Image.open("icons/opcoes.png"), size=(25, 25))
    }
    return icons

def show_gallery_callback(place):
    show_gallery(main_frame, place)

# Menu 'Inicio'
def show_home():
    global normal_frame
    clear_frame(main_frame)
    main_frame._parent_canvas.yview_moveto(0.0)

    if normal_frame is None:
        normal_frame = CTkFrame(master=app)
        normal_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

    clear_frame(normal_frame)

    home_label = CTkLabel(master=normal_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)

# Menu 'Explorar'
def show_explore_menu():
    global normal_frame

    if normal_frame is not None:
        normal_frame.destroy()
        normal_frame = None

    clear_frame(main_frame)

    explore_options = [explorar_praia, explorar_bares, explorar_restaurantes, explorar_trilhas,
                       explorar_cultura, explorar_lagoas, explorar_boates,
                       explorar_hoteis_e_pousados, explorar_estacionamento]

    for option_func in explore_options:
        button_name, content, img_path = option_func()

        pil_image = Image.open(img_path)
        resized_image = pil_image.resize((550, 100), Image.BICUBIC)

        ct_image = CTkImage(resized_image, size=(550, 100))

        button = CTkButton(master=main_frame, text=button_name, command=lambda c=content: show_content(main_frame, c,  app),
                               text_color="red", font=("Arial", 16, "bold"), fg_color="transparent", width=550,
                               height=100, image=ct_image, compound="top")
        button.pack(pady=5, padx=5, anchor="center", fill="x")

# Menu 'favoritos'
def show_favorites_menu():
    from favoritos import favorite_states
    global normal_frame

    if normal_frame is not None:
        normal_frame.destroy()
        normal_frame = None

    clear_frame(main_frame)
    main_frame._parent_canvas.yview_moveto(0.0)

    favoritos_label = CTkLabel(master=main_frame, text="Favoritos", font=("Arial", 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            for category in [explorar_praia(), explorar_bares(), explorar_restaurantes(), explorar_trilhas(), explorar_cultura()
                             , explorar_lagoas(), explorar_boates(), explorar_hoteis_e_pousados(), explorar_estacionamento()]:
                for item in category[1]:
                    if item["name"] == item_name:
                        favorite_items.append(item)

    show_content(main_frame, favorite_items,  app)

# Menu 'Opções'
def show_options_menu():
    global normal_frame
    clear_frame(main_frame)

    if normal_frame is None:
        normal_frame = CTkFrame(master=app)
        normal_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

    clear_frame(normal_frame)

    global theme_button
    theme_button = CTkButton(master=normal_frame, text="Modo Escuro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)

#################### APLICATIVO ####################
app = CTk()
app.geometry("1200x700")
app.title("Marica City")
app.resizable(width=False, height=False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Nome MARICA CITY
header = CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = CTkLabel(header, text="MARICA CITY", text_color="red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)

# Botao de pesquisa
search_frame = CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="w", padx=(10, 0))

search_entry = CTkEntry(search_frame, width=350)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()), fg_color="red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

# Frame principal
main_frame = CTkScrollableFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

normal_frame = None

menu_frame = CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

# Botoes da esquerda / MENU
icon = load_icons()
menu_buttons = [
    {"text": "   Inicio   ", "command": show_home, "icon": icon["home"]},
    {"text": " Explorar", "command": show_explore_menu, "icon": icon["explorar"]},
    {"text": "Favoritos", "command": show_favorites_menu, "icon": icon["favoritos"]},
    {"text": " Opções  ", "command": show_options_menu, "icon": icon["opcoes"]}
]

for index, btn in enumerate(menu_buttons):
    CTkButton(
        master=menu_frame,
        text=btn["text"],
        command=btn["command"],
        image=btn["icon"],
        compound="left",
        fg_color="red",
        width=150,
        height=40
    ).grid(row=index, column=0, pady=10, padx=10)

# Tema inicial
dark_mode = False
set_appearance_mode("light")

show_home()
app.mainloop()
