from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkScrollableFrame, CTkOptionMenu, set_appearance_mode
from PIL import Image
from categorias import * 
from galeria import show_content, show_gallery, update_main_image, clear_frame, light_color, light_colorh, dark_color, dark_colorh, title_font, font


options = [explorar_praia, explorar_trilhas, explorar_parques,  
            explorar_cultura ,explorar_restaurantes, explorar_bares, 
            explorar_pousadas, explorar_estacionamento]

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
    all_items = (explorar_praia()[1] + explorar_trilhas()[1] + explorar_parques()[1] 
                 + explorar_cultura()[1] + explorar_restaurantes()[1] + explorar_bares()[1] 
                 + explorar_pousadas()[1] + explorar_estacionamento()[1])

    filtered_items = [item for item in all_items if query.lower() in item["name"].lower()]

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
        "mapa": CTkImage(Image.open("icons/mapa.png"), size=(28, 28)),
        "favoritos": CTkImage(Image.open("icons/favorito.png"), size=(25, 25)),
        "opcoes": CTkImage(Image.open("icons/opcoes.png"), size=(25, 25))
    }
    return icons

def show_gallery_callback(place):
    show_gallery(main_frame, place)

# Lógica do "mapa"
def atualizar_imagem(item_selecionado):
    map_imagem.configure(image=None)
    selected_item = next((item for item in all_items if item["name"] == item_selecionado), None)

    try:
        print(f"Carregando a imagem do mapa {selected_item['map']}...")  
        img = Image.open(selected_item["map"])
        img = img.resize((600, 600), Image.BICUBIC)
        imagem = CTkImage(img, size=(600, 600))

        map_imagem.configure(image=imagem)
        map_imagem.image = imagem
    except Exception as e:
        print(f"Erro ao carregar a imagem do mapa: {selected_item['map']} - {e}")

# Menu 'Inicio'
def show_home():
    global normal_frame
    clear_frame(main_frame)

    if normal_frame is None:
        normal_frame = CTkFrame(master=app)
        normal_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

    clear_frame(normal_frame)

    home_label = CTkLabel(master=normal_frame, text="Bem-vindo à Maricá City!", font=(font, 18, "bold"))
    home_label.pack(pady=20)

# Menu 'Mapa'
def show_mapa():
    global normal_frame
    clear_frame(main_frame)
    all_items.clear()

    if normal_frame is None:
        normal_frame = CTkFrame(master=app)
        normal_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

    clear_frame(normal_frame)

    for func in options:
        func()

    nomes_itens = [item["name"] for item in all_items]
    nomes_itens.sort()
    
    map_menu = CTkOptionMenu(normal_frame, values=nomes_itens, command=atualizar_imagem, width= 200, height= 30, dropdown_fg_color= ("light gray", "gray"), corner_radius= 4,
                             button_color = (light_colorh, dark_colorh), hover= False, fg_color=(light_color, dark_color), anchor= "center", text_color= "white")
    map_menu.pack(side="left", anchor="nw", pady=(40,0),padx=(50,0))

    global map_imagem
    map_imagem = CTkLabel(normal_frame, text="", anchor= "e")
    map_imagem.pack(side="right", fill="both", expand=True, pady=(10,60), padx=(10,50))


# Menu 'Explorar'
def show_explore_menu():
    global normal_frame

    if normal_frame is not None:
        normal_frame.destroy()
        normal_frame = None

    clear_frame(main_frame)

    for option_func in options:
        button_name, content, img_path = option_func()
        
        pil_image = Image.open(img_path)
        resized_image = pil_image.resize((550, 100), Image.BICUBIC)
        ct_image = CTkImage(resized_image, size=(550, 100))

        button = CTkButton(master=main_frame, text="▮ "+ button_name + (" "*90), command=lambda c=content: show_content(main_frame, c,  app),
                               text_color= ("brown", "white"), hover_color =("#c1c1c1", "gray22"), font=(title_font, 18, "bold"), fg_color="transparent",
                                width=550, height=150, image=ct_image, compound="top", anchor= "w")
        
        button.pack(pady=(10, 0), padx=5, anchor="center")


# Menu 'favoritos'
def show_favorites_menu():
    from favoritos import favorite_states
    global normal_frame

    if normal_frame is not None:
        normal_frame.destroy()
        normal_frame = None

    clear_frame(main_frame)
    main_frame._parent_canvas.yview_moveto(0.0)

    favoritos_label = CTkLabel(master=main_frame, text="Favoritos", font=(font, 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            for category in [explorar_praia(), explorar_trilhas(), explorar_parques(), explorar_cultura(), explorar_restaurantes(),
                             explorar_bares(), explorar_pousadas(), explorar_estacionamento()]:
                for item in category[1]:
                    if item["name"] == item_name:
                        favorite_items.append(item)

    show_content(main_frame, favorite_items, app)

# Menu 'Opções'
def show_options_menu():
    global normal_frame
    clear_frame(main_frame)

    if normal_frame is None:
        normal_frame = CTkFrame(master=app)
        normal_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

    clear_frame(normal_frame)

    global theme_button
    theme_button = CTkButton(master=normal_frame, text="Modo Escuro", font=(font, 13), command=toggle_theme, fg_color=(light_color, dark_color),
                              hover_color=(light_colorh, dark_colorh), width= 180)
    theme_button.pack(pady=10, padx=20)

#################### APLICATIVO ####################
app = CTk()
app.geometry("1200x800")
app.title("Marica City")

app.iconbitmap("icons/bus.ico")
app.resizable(width=False, height=False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Nome MARICA CITY
header = CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = CTkLabel(header, text="MARICA CITY", text_color= (light_color, "#2133FF"), font=(title_font, 22, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)

# Botao de pesquisa
search_frame = CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="w", padx=(10, 0))

search_entry = CTkEntry(search_frame, width=350)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = CTkButton(search_frame, text="Pesquisar", font=(title_font, 13), command=lambda: search_action(search_entry.get().lower()),
                           fg_color=(light_color, dark_color), hover_color = (light_colorh, dark_colorh), width=100)
search_button.grid(row=0, column=1, padx=(4, 0), pady=10)

# Frame principal
main_frame = CTkScrollableFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

normal_frame = None

menu_frame = CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

# Botoes da esquerda / MENU
icon = load_icons()
menu_buttons = [
    {"text": "Inicio      ", "command": show_home, "icon": icon["home"]},
    {"text": " Explorar", "command": show_explore_menu, "icon": icon["explorar"]},
    {"text": "Mapa     ", "command": show_mapa, "icon": icon["mapa"]},
    {"text": "Favoritos", "command": show_favorites_menu, "icon": icon["favoritos"]},
    {"text": "Opções   ", "command": show_options_menu, "icon": icon["opcoes"]}
]

for index, btn in enumerate(menu_buttons):
    CTkButton(
        master=menu_frame,
        text=btn["text"],
        command=btn["command"],
        image=btn["icon"],
        compound="left",
        font = (font, 13),
        fg_color=(light_color, dark_color),
        hover_color=(light_colorh, dark_colorh),
        width=150,
        height=40
    ).grid(row=index, column=0, pady=10, padx=10)

# Tema inicial
dark_mode = False

show_home()
app.mainloop()
