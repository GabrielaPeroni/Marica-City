from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkImage, CTkCanvas, CTkScrollbar, set_appearance_mode
from categorias import explorar_praia, explorar_bares, explorar_restaurantes, explorar_trilhas, explorar_cultura, explorar_lagoas, explorar_boates, explorar_hoteis_e_pousados, explorar_estacionamento
from favoritos import toggle_favorite, on_enter, on_leave
from PIL import Image

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

# Limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Carrega os ícones diretamente da pasta "icons"
def load_icons():
    icons = {
        "home": CTkImage(Image.open("icons/home.png"), size=(25, 25)),
        "explorar": CTkImage(Image.open("icons/explorar.png"), size=(25, 25)),
        "favoritos": CTkImage(Image.open("icons/favorito.png"), size=(25, 25)),
        "opcoes": CTkImage(Image.open("icons/opcoes.png"), size=(25, 25))
    }
    return icons

# Lógica da Pesquisa
def search_action(query):
    all_items = explorar_praia()[1] + explorar_bares()[1] + explorar_restaurantes()[1] 
    + explorar_trilhas()[1]+ explorar_cultura()[1] + explorar_lagoas()[1]+ explorar_boates()[1] 
    + explorar_hoteis_e_pousados()[1]+ explorar_estacionamento()[1]

    # Filtrar os itens
    filtered_items = [item for item in all_items if query in item["name"].lower()]
    show_content(filtered_items)

def show_content(items):
    from favoritos import favorite_states
    clear_frame(main_frame)

    if not items:
        no_result_label = CTkLabel(master=main_frame, text="Nenhum resultado encontrado.", font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = CTkFrame(master=main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
            print(f"Carregando a imagem: {item['image']}")  # Linha de depuração
            img = Image.open(item["image"])
            image = CTkImage(img, size=(120,90))

            label_image = CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {item['image']} - {e}")

        label_name = CTkLabel(master=frame, text=item["name"], font=("Arial", 16))
        label_name.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        label_description = CTkLabel(master=frame, text=item["description"], wraplength=400)
        label_description.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        # Criação do botão favorito
        favorite_button = CTkButton(master=frame, text="", image=CTkImage(Image.open("icons/favorito.png"), size=(30, 30)), 
                                          width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        # Adicionando a função para o botão favorito
        favorite_button.bind("<Button-1>", lambda event, btn=favorite_button, item_name=item["name"]: toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>", lambda event, btn=favorite_button, item_name=item["name"]: on_leave(btn, item_name))

        # Inicializa o estado do favorito
        initial_icon = "icons/favorito_active.png" if favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=CTkImage(Image.open(initial_icon),size=(20, 20)))
        
        button_details = CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(p), fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")

def show_gallery(place):
    clear_frame(main_frame)

    back_button = CTkButton(master=main_frame, text="Voltar", command=show_explore_menu, fg_color="red")
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    # Carregar a imagem principal
    try:
        img = Image.open(place["image"])
        image = CTkImage(img, size=(400,300))
        
        main_image_label = CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image  # Manter a referência da imagem
        main_image_label.pack(pady=(15, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    # Nome do lugar
    label_name = CTkLabel(master=main_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=(10, 5))

    # Descrição do lugar
    label_description = CTkLabel(master=main_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=(5, 10))

    # Galeria de imagens adicionais
    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = CTkCanvas(main_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)

        scrollbar = CTkScrollbar(main_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")

        gallery_container = CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                image = CTkImage(img, size=(120,90))
                gallery_label = CTkButton(master=gallery_container, image=image, text="", 
                                              command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image  # Manter a referência da imagem
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))

def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((400, 300))
        image = CTkImage(img)
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")

# Menu 'Inicio'
def show_home():
    clear_frame(main_frame)
    home_label = CTkLabel(master=main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)

# Menu 'Explorar'
def show_explore_menu():
    clear_frame(main_frame)
    explore_options = [explorar_praia, explorar_bares, explorar_restaurantes, explorar_trilhas, explorar_cultura
                       , explorar_lagoas, explorar_boates, explorar_hoteis_e_pousados, explorar_estacionamento]

    for option_func in explore_options:
        button_name, content = option_func()
        button = CTkButton(master=main_frame, text=button_name, command=lambda c=content: show_content(c), fg_color="red")
        button.pack(pady=10, padx=20, side= "top", anchor= "w")

# Menu 'favoritos'
def show_favorites_menu():
    from favoritos import favorite_states
    clear_frame(main_frame)
    favoritos_label = CTkLabel(master=main_frame, text="Favoritos", font=("Arial", 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            for category in [explorar_praia(), explorar_bares(),explorar_restaurantes(), explorar_trilhas(), explorar_cultura()
                             , explorar_lagoas(), explorar_boates(), explorar_hoteis_e_pousados(), explorar_estacionamento()]:
                for item in category[1]:
                    if item["name"] == item_name:
                        favorite_items.append(item)

    show_content(favorite_items)

# Menu 'Opções'
def show_options_menu():
    clear_frame(main_frame)
    global theme_button
    theme_button = CTkButton(master=main_frame, text="Modo Escuro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)

#################### APLICATIVO ####################
app = CTk()
app.geometry("800x600")
app.title("Marica City")
app.resizable(width= False, height= False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Nome MARICA CITY
header = CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = CTkLabel(header, text="MARICA CITY", text_color= "red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)

# Botao de pesquisa
search_frame = CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()), fg_color= "red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

# Frame principal
main_frame = CTkFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

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
