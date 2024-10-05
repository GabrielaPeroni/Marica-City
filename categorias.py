all_items = []

def explorar_praia():
    praias = [
        {"name": "Praia 1", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil.", "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia 2", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png"]},
        {"name": "Praia 3", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.", "gallery": ["images/praia2.png","images/praia2_1.png"]}
    ]

    global all_items

    all_items.extend(praias)
    return "Praias", praias

def explorar_bares():
    bares = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(bares)
    return "Bares", bares


def explorar_restaurantes():
    restaurantes = [
        {"name": "Restaurante 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Restaurante 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(restaurantes)
    return "Restaurantes", restaurantes

def explorar_trilhas():
    trilhas = [
        {"name": "Trilha 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Trilha 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(trilhas)
    return "Trilhas", trilhas

def explorar_cultura():
    cultura = [
        {"name": "Cultura 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Cultura 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(cultura)
    return "Cultura", cultura


def explorar_lagoas():
    lagoas = [
        {"name": "Lagoas 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Lagoas 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(lagoas)
    return "Lagoas", lagoas


def explorar_boates():
    boates = [
        {"name": "Boate 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Boate 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(boates)
    return "Boates", boates


def explorar_hoteis_e_pousados():
    hoteis_e_pousados = [
        {"name": "Pousada 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Pousada 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(hoteis_e_pousados)
    return "Hoteis/ Pousadas", hoteis_e_pousados


def explorar_estacionamento():
    estacionamento  = [
        {"name": "Estacionamento 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.", "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Estacionamento 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.", "gallery": ["images/bar2.png","images/bar2_1.png"]},
    ]
    global all_items

    all_items.extend(estacionamento )
    return "Estacionamento ", estacionamento 
