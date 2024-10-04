import customtkinter as ctk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk

# Função para alternar entre modo claro e escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        ctk.set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

# Função para limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para a tela "Inicio"
def show_home():
    clear_frame(main_frame)
    home_label = ctk.CTkLabel(master=main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)

# Função para exibir a galeria e descrição de cada item dentro das categorias
def show_gallery(place):
    clear_frame(main_frame)
    
    # Frame da galeria
    gallery_frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
    gallery_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    back_button = ctk.CTkButton(master=gallery_frame, text="Voltar", command=show_explore_menu, fg_color="red")
    back_button.pack(pady=10, anchor="w")
    
    # Carregar imagem principal
    try:
        img = Image.open(place["image"])
        img = img.resize((400, 300))
        image = ImageTk.PhotoImage(img)
        main_image_label = ctk.CTkLabel(master=gallery_frame, image=image, text="")
        main_image_label.image = image  # Manter referência
        main_image_label.pack(pady=10)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")
    
    label_name = ctk.CTkLabel(master=gallery_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=10)
    
    label_description = ctk.CTkLabel(master=gallery_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=10)
    
    # Galeria de imagens adicionais
    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = Canvas(gallery_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)
        scrollbar = Scrollbar(gallery_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")
        
        gallery_container = ctk.CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")
        
        for image_path in gallery_images:
            try:
                img = Image.open(image_path)
                img = img.resize((120, 90))
                image = ImageTk.PhotoImage(img)
                gallery_label = ctk.CTkButton(master=gallery_container, image=image, text="", 
                                              command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")
        
        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))

# Funções individuais de exploração

def explorar_praia():
    # Definindo os detalhes específicos das praias
    praias = [
        {"name": "Praia do Francês", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil.", "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia de Copacabana", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.", "gallery": ["images/praia2_1.png"]},
    ]
    # Retorna o nome do botão e os itens
    return "Praias", praias

def explorar_bares():
    # Definindo os detalhes específicos dos bares
    bares = [
        {"name": "Bar do Zé", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Botequim do João", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2_1.png"]},
    ]
    # Retorna o nome do botão e os itens
    return "Bares", bares

# Adicione outras funções como explorar_trilhas, explorar_cultura etc.

# Função para exibir o menu de categorias (Explorar)
def show_explore_menu():
    clear_frame(main_frame)
    
    # Lista de funções para explorar
    explore_options = [explorar_praia, explorar_bares]
    
    for option_func in explore_options:
        button_name, content = option_func()  # Obtém o nome do botão e os itens
        button = ctk.CTkButton(master=main_frame, text=button_name, command=lambda c=content: show_content(c), fg_color="red")
        button.pack(pady=10, padx=20)

# Função para exibir o conteúdo de uma categoria
def show_content(items):
    clear_frame(main_frame)
    
    for item in items:
        frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")
        
        try:
            img = Image.open(item["image"])
            img = img.resize((120, 90))
            image = ImageTk.PhotoImage(img)
            label_image = ctk.CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {item['image']} - {e}")
        
        label_name = ctk.CTkLabel(master=frame, text=item["name"], font=("Arial", 16))
        label_name.pack(anchor="w")
        
        label_description = ctk.CTkLabel(master=frame, text=item["description"], wraplength=400)
        label_description.pack(anchor="w")
        
        button_details = ctk.CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(p), fg_color="red")
        button_details.pack(anchor="e", pady=10)

# Função para o menu de "Opções"
def show_options_menu():
    clear_frame(main_frame)
    global theme_button
    theme_button = ctk.CTkButton(master=main_frame, text="Modo Claro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)

# Função para atualizar a imagem principal na galeria
def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((400, 300))
        image = ImageTk.PhotoImage(img)
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")

# Configuração da janela principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Opções de Lazer")

# Cabeçalho
header = ctk.CTkFrame(app, fg_color="red")
header.pack(side="top", fill="x")
header_label = ctk.CTkLabel(header, text="MARICA CITY", text_color="white", font=("Arial", 20, "bold"))
header_label.pack(pady=10)

# Menu lateral com as opções Inicio, Explorar, e Opções
menu_frame = ctk.CTkFrame(master=app, fg_color="gray")
menu_frame.pack(side="left", fill="y", padx=20, pady=20)

menu_buttons = [
    {"text": "Inicio", "command": show_home},
    {"text": "Explorar", "command": show_explore_menu},
    {"text": "Opções", "command": show_options_menu},
]

for btn in menu_buttons:
    ctk.CTkButton(master=menu_frame, text=btn["text"], command=btn["command"], fg_color="red").pack(pady=10, padx=10)

# Frame principal onde o conteúdo será mostrado
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Inicializa com a tela de início
dark_mode = True
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

show_home() 
app.mainloop()
