all_items = []

def explorar_praia():
    praias = [
        {"name": "Praia de Ponta negra",
        "image": "images/praia1.png", 
        "description": ("A Praia de Ponta Negra, em Maricá, é um verdadeiro paraíso carioca, conhecida por suas águas cristalinas, paisagens deslumbrantes e um extenso trecho de areia fina e dourada."),
        "address": "Rua Marilene Rangel da Cruz, 6 - Ponta Negra, Maricá - RJ",
        "gallery": ["images/praia1.png", "images/praia1_1.png", "images/praia1_2.png", "images/praia1_3.png", "images/praia1_4.png"]},

        {"name": "Praia da Barra",
         "image": "images/praia2.png",
         "description": (" Com 9 km de areias finas e águas transparentes, esta praia é perfeita para relaxar e saborear a deliciosa gastronomia local. Ideal para pescarias e banhos tranquilos​"),
         "address": "Av. Litorânea - Zacarias, Maricá - RJ",
         "gallery": ["images/praia2.png","images/praia2_1.png","images/praia2_2.png","images/praia2_3.png","images/praia2_4.png"]},

        {"name": "Praia de Itaipuaçu",
         "image": "images/praia3.png",
         "description": ("Com belas vistas do Pão de Açúcar e da Pedra do Elefante ao fundo, a praia oferece um ambiente natural encantador, ideal para caminhadas e momentos tranquilos ao ar livre."
                         "Atenção a bandeira colocada na praia, pois certos dias o mar fica inacessivel e perigoso !"),
         "address": "Itaipuaçu, Maricá, RJ",
         "gallery": ["images/praia3.png","images/praia3_1.png","images/praia3_2.png","images/praia3_3.png","images/praia3_4.png"]},

        {"name": "Praia do Cordeirinho",
         "image": "images/praia4.png",
         "description": ("A Praia do Corderinho é um destino encantador que combina natureza exuberante com uma atmosfera relaxante, tendo águas claras e mornas perfeitas para relaxar."),
         "address": "Rua Noventa e Um Lot Pr Lagoas, 2 - Cordeirinho, Maricá - RJ",
         "gallery": ["images/praia4.png","images/praia4_1.png","images/praia4_2.png","images/praia4_3.png","images/praia4_4.png"]},

         {"name": "Praia do Recanto",
         "image": "images/praia5.png",
         "description": ("Localizada aos pés do Morro do Elefante, com um píer de pedras que se estende mar adentro, essa praia oferece uma longa faixa de areia e um ambiente rústico,"
                         " complementado por quiosques improvisados nas casas dos moradores."),
         "address": "Rua Dr. Adair Farah Da Mota, 95 - Itaipuaçu, Maricá - RJ",
         "gallery": ["images/praia5.png","images/praia5_1.png","images/praia5_2.png","images/praia5_3.png","images/praia5_4.png"]}
   ]

    global all_items

    all_items.extend(praias)
    return "Praias", praias,r"images\praia_cat.jpg"

def explorar_trilhas():
    trilhas = [
        {"name": "Pedra do Macaco",
         "image": "images/trilha1.png",
         "description": ("Um lugar para quem deseja fazer rapel, escalada ou, simplesmente, aproveitar uma bela vista."
                         " Embora a trilha seja considerada leve, a subida é íngreme e pode exigir o uso de cordas em alguns pontos para ajudar os caminhantes"),
         "address": "São José de Imbassai, Maricá - RJ",
         "gallery": ["images/trilha1.png","images/trilha1_1.png","images/trilha1_2.png","images/trilha1_3.png","images/trilha1_4.png"]},

        {"name":"Pedra do elefante",
         "image": "images/trilha2.png",
         "description": ("Localizada na divisa entre Niterói e Maricá, a trilha é de nível moderado e possui uma vista incrível."
                         " Em dias com uma boa visibilidade, você poderá ver os principais pontos turísticos da cidade do Rio de Janeiro, como a Pedra da Gávea e o Pão de Açúcar!."),
         "address": "Serra da tiririca - Mata Atlântica, Maricá - RJ",
         "gallery": ["images/trilha2.png","images/trilha2_1.png","images/trilha2_2.png","images/trilha2_3.png","images/trilha2_4.png"]},

        {"name":"Gruta do Spar",
         "image": "images/trilha3.png",
         "description": ("Este destino é ideal para trilheiros e amantes da natureza que desejam vivenciar um ambiente natural único."
                         " O percurso, que começa próximo à capela do bairro Spar, culmina em um lago de águas cristalinas, perfeito para um mergulho refrescante após a caminhada"),
         "address": "Grutas do Spar, São Gonçalo - RJ",
         "gallery": ["images/trilha3.png","images/trilha3_1.png","images/trilha3_2.png","images/trilha3_3.png","images/trilha3_4.png"]},

        {"name":"Mirante Do Caju",
        "image": "images/trilha4.png",
        "description": ("Um novo ponto turístico sendo desenvolvido que promete oferecer uma vista panorâmica da cidade e experiências culturais e gastronômicas.​"),
        "address": "Jardim Adalberto Alves, Maricá - RJ",
        "gallery": ["images/trilha4.png","images/trilha4_1.png","images/trilha4_2.png","images/trilha4_3.png","images/trilha4_4.png"]}
       ]
    global all_items

    all_items.extend(trilhas)
    return "Trilhas", trilhas,r"images\trilhas_cat.jpg"

def explorar_parques():
    parque = [
        {"name": "Parque Nanci",
         "image": "images/parque1.png",
         "description": ("Sendo um dos maiores parques de Maricá, o parque possui quadras para esportes, pista de atletismo, campo de futebol, churrasqueiras, um playground e aparelhos de ginástica."
                         " Também possui horta e pomar comunitários que incluem diversas frutas, como jabuticaba, limão e manga"),
         "address": "Rua Sabiá - Itapeba, Maricá - RJ",
         "gallery": ["images/parque1.png","images/parque1_1.png","images/parque1_2.png","images/parque1_3.png","images/parque1_4.png"]},

        {"name": "Lagoa de Araçatiba",
         "image": "images/parque2.png",
         "description": ("Local encantador conhecido por suas águas tranquilas e beleza natural."
                         " Esta lagoa é propícia para atividades como pesca e esportes náuticos, oferecendo um cenário perfeito para quem busca lazer e contato com a natureza."),
         "address": "Rua Álvares de Castro - Eldorado, Maricá - RJ",
         "gallery": ["images/parque2.png","images/parque2_1.png","images/parque2_2.png","images/parque2_3.png","images/parque2_4.png"]},

        {"name": "Parque Linear do Flamengo",
         "image": "images/parque3.png",
         "description": ("O parque oferece diversas instalações esportivas, como skatepark, paredes de escalada, quadras poliesportivas e áreas de convivência."
                         " Todas sao interligadas por ciclovias, promovendo um ambiente propício para a prática de esportes e socialização"),
         "address": "Rua Uirapurús - Flamengo, Maricá - RJ",
         "gallery": ["images/parque3.png","images/parque3_1.png","images/parque3_2.png","images/parque3_3.png","images/parque3_4.png"]},

         {"name": "Praça do Tiradentes",
         "image": "images/parque4.png",
         "description": ("Espaço público tranquilo, rodeado por ruas residenciais e com fácil acesso a serviços próximos, como restaurantes e pousadas."),
         "address": "Rua Quarenta e Um, 1639 - Araçatiba, Maricá - RJ",
         "gallery": ["images/parque4.png","images/parque4_1.png","images/parque4_2.png","images/parque4_3.png","images/parque4_4.png"]},
        ]
    global all_items

    all_items.extend(parque)
    return "Parques", parque,r"images\parque_cat.jpg"


def explorar_cultura():
    cultura = [
        {"name": "Museu Casa Darcy Ribeiro",
         "image": "images/cultura1.png",
         "description": ("O espaço oferece: duas salas de cinema, espaço para gravação de podcast (de uso público mediante agendamento),"
                         " sala de karaokê, palco (com destaque para musica contemporêa como rap e trap, poesia e slam). Se localiza em Cordeirinho."),
         "address": "Rua Cento e Dezenove - Ponta Negra, Maricá - RJ",
         "gallery": ["images/cultura1.png","images/cultura1_1.png","images/cultura1_2.png","images/cultura1_3.png","images/cultura1_4.png"]},

        {"name":"Casa de cultura & Museu Histórico",
         "image": "images/cultura2.png",
         "description": ("Um importante patrimônio histórico da cidade, com mais de 180 anos de história. Antigamente, funcionou como cadeia pública e sede da Prefeitura."
                         " Após uma completa restauração, hoje abriga o Museu Histórico de Maricá"),
         "address": "Rua Álvares de Castro, 154 - Centro, Maricá - RJ",
         "gallery": ["images/cultura2.png","images/cultura2_1.png","images/cultura2_2.png","images/cultura2_3.png","images/cultura2_4.png"]},

        {"name":"Planetário de Maricá",
         "image": "images/cultura3.png",
         "description": ("Destaca-se por ser o primeiro planetário do Brasil movido totalmente por energia solar, com o objetivo de enriquecer a experiência educacional de escolas locais."
                         " Conta com um observatório ao ar livre equipado com telescópio, uma sala de aula com recursos de impressão 3D e robótica, e um espaço coworking para empreendedores"),
         "address": "Jardim Atlântico Central, Maricá - RJ",
         "gallery": ["images/cultura3.png","images/cultura3_1.png","images/cultura3_2.png","images/cultura3_3.png","images/cultura3_4.png"]},

         {"name":"Cine Henfil",
         "image": "images/cultura4.png",
         "description": ("Oferece exibições regulares de filmes voltados tanto para o público infantojuvenil quanto adulto, além de mostras e eventos audiovisuais em colaboração com organizações públicas e civis"),
         "address": "R. Alferes Gomes, 390 - Centro, Maricá - RJ",
         "gallery": ["images/cultura4.png","images/cultura4_1.png","images/cultura4_2.png","images/cultura4_3.png","images/cultura4_4.png"]}
        ]
    global all_items

    all_items.extend(cultura)
    return "Cultura", cultura,r"images\cultura_cat.jpg"

def explorar_restaurantes():
    restaurantes = [
        {"name": "Horus Beer & Food",
         "image": "images/restaurante1.png",
         "description": ("O Horus Beer & Food, em Maricá, é uma excelente opção para amantes de carnes nobres e petiscos variados."
                         " Com um ambiente acolhedor, o restaurante destaca-se pela qualidade de seus pratos, como hambúrgueres artesanais"),
         "address": "Rua Irineu Ferreira Pinto, 20 - Ponta Grossa, Maricá - RJ",
         "gallery": ["images/restaurante1_1.png", "images/restaurante1_2.png", "images/restaurante1_3.png", "images/restaurante1_4.png", "images/restaurante1_5.png"]},

        {"name": "Varandão do Zé Carlos",
         "image": "images/restaurante2.png",
         "description": ("Um restaurante simples com climatização, destacando-se pelo churrasco suculento e frutos do mar frescos."
                         " A qualidade e o serviço atencioso fazem deste lugar um favorito em Maricá"),
         "address": "Rua Athaíde Parreiras, 107 - Centro, Maricá - RJ",
         "gallery": ["images/restaurante2_1.png","images/restaurante2_2.png","images/restaurante2_3.png","images/restaurante2_4.png","images/restaurante2_5.png"]},

        {"name": "Casa Grill",
         "image": "images/restaurante3.png",
         "description": ("localizado no coração de Maricá, ao lado da Igreja Nossa Senhora do Amparo. Recentemente rebatizado de Mistura Grill,"
                         " o Casa Grill busca preservar seu legado enquanto apresenta uma nova atmosfera e cardápio."),
         "address": "Rua Almeida Fagundes, 104 - Centro, Maricá - RJ",
         "gallery": ["images/restaurante3_1.png","images/restaurante3_2.png","images/restaurante3_3.png","images/restaurante3_4.png","images/restaurante3_5.png"]},

         {"name": "Bora Bora",
         "image": "images/restaurante4.png",
         "description": ("Com mais de seis anos de experiência, o restaurante oferece um menu diversificado que combina pratos tradicionais, como bacalhau e picanha, com inovações,"
                         " incluindo Bolinho de Feijoada e Patê de Foie Gras com Geleia de Amora."),
         "address": "Rua Álvares de Castro, 632 - Araçatiba, Maricá - RJ",
         "gallery": ["images/restaurante4_1.png","images/restaurante4_2.png","images/restaurante4_3.png","images/restaurante4_4.png","images/restaurante4_5.png"]}
    ]


    global all_items

    all_items.extend(restaurantes)
    return "Restaurantes", restaurantes,r"images\restaurante_cat.jpg"

def explorar_bares():
    bares = [
        {"name": "Caneca Mofada",
         "image": "images/bar1.png",
         "description": ("bar acolhedor e popular em Maricá, conhecido por sua boa cerveja e atmosfera animada."
                         "Ideal para quem busca diversão noturna com amigos, ele oferece um ótimo atendimento e ambiente descontraído, sendo elogiado pelos visitantes pela qualidade do serviço e a experiência vibrante"),
         "address": "Rua Prof. Cardoso de Menezes, 13 - Itaipuaçu, Maricá - RJ",
         "gallery": ["images/bar1_1.png","images/bar1_2.png","images/bar1_3.png","images/bar1_4.png","images/bar1_5.png"]},

        {"name": "Skull Beer Bar",
         "image": "images/bar2.png",
         "description": ("É conhecido como o bar mais rock n' roll de Itaipuaçu. Oferece um ambiente descontraído, perfeito para apreciar cervejas artesanais e um cardápio de petiscos."
                         " Com um estilo único, é o lugar ideal para quem busca uma noite animada com amigos"),
         "address": "Rua Walter Favilla da Silva, Qd96, Lt22, Loja - Barroco, Maricá - RJ",
         "gallery": ["images/bar2_1.png","images/bar2_2.png","images/bar2_3.png","images/bar2_4.png","images/bar2_5.png"]},

        {"name": "Maltz Beer Garden",
         "image": "images/bar3.png",
         "description": ("Bar histórico funcionando a mais de 50 anos na cidade! Oferece um espaço kids e promoções especiais ideal para famílias e grupos de amigos."
                         " É perfeito para quem busca um ambiente descontraído com música ao vivo, variedade de chopps e deliciosos pratos"),
         "address": "Rua Walter Favilla da Silva 20 Barroco - Itaipuaçu, Maricá - RJ",
         "gallery": ["images/bar3_1.png","images/bar3_2.png","images/bar3_3.png","images/bar3_4.png","images/bar3_5.png"]},

         {"name": "Mahalo Ginkeria",
         "image": "images/bar4.png",
         "description": ("Localizado no centro de Maricá, incluindo apresentações ao vivo e festas temáticas, tornando-se um ponto de encontro popular para os amantes da música e da diversão."),
         "address": "Rua Álvares de Castro, 600 - Centro, Maricá - RJ",
         "gallery": ["images/bar4_1.png","images/bar4_2.png","images/bar4_3.png","images/bar4_4.png","images/bar4_5.png"]},

        {"name": "Imperio do King",
         "image": "images/bar5.png",
         "description": ("Costelaria localizada em Itaipuaçu, Maricá, o menu é conhecido por suas costelas suculentas, preparadas com um tempero especial que remete à comida caseira,"
                         " e oferece pratos inovadores como a costela na mini moranga e uma variedade de bebidas, incluindo drinks exclusivos"),
         "address": "Rua Sen. Macedo Soares, 205 - Eldorado, Maricá - RJ",
         "gallery": ["images/bar5_1.png","images/bar5_2.png","images/bar5_3.png","images/bar5_4.png","images/bar5_5.png"]},
    ]
    global all_items

    all_items.extend(bares)
    return "Bares", bares,r"images\bar_cat.jpg"


def explorar_pousadas():
    pousada = [
        {"name": "Vila da Praia",
         "image": "images/pousada1.png",
         "description": ("A Vila da Praia é uma excelente opção para turistas, oferece um ambiente familiar e várias comodidades que vão tornar a sua estadia ainda mais especial."
                        " Além disso os hóspedes contam com frigobar e ambiente climatizado."),
         "address": "Rua Oscar Niemeyer, 12 - Itaipuaçu, Maricá - RJ",
         "gallery": ["images/pousada1_1.png","images/pousada1_2.png","images/pousada1_3.png","images/pousada1_4.png","images/pousada1_5.png"]},

        {"name": "Pousada Potigua",
         "image": "images/pousada2.png",
         "description": ("Com uma bela vista para o mar e decoração charmosa, é um refugio ideal para relaxar e aproveitar"
                         " A Pousada Potigua está localizada à beira-mar na Praia de Ponta Negra em Maricá."),
         "address": "Rua Cento e Trinta e Seis,Lote 9, Quadra 195, 284 Cordeirinho - Ponta Negra, Maricá - RJ",
         "gallery": ["images/pousada2_1.png","images/pousada2_2.png","images/pousada2_3.png","images/pousada2_4.png","images/pousada2_5.png"]},

        {"name":"Pousada Maricá",
         "image": "images/pousada3.png",
         "description": ("Conforto e qualidade! Com uma localização privilegiada próximo a praias e ao centro da cidade, esta pousada oferece um ambiente rústico e aconchegante,"
                         " tornando-a uma escolha perfeita para quem deseja relaxar em meio à beleza natural da região"),
         "address": "Rua Jerônimo Rodrigues, 1 - Centro, Maricá - RJ",
         "gallery": ["images/pousada3_1.png","images/pousada3_2.png","images/pousada3_3.png","images/pousada3_4.png","images/pousada3_5.png"]},

        {"name":"Pousada do Holandes",
         "image": "images/pousada4.png",
         "description": ("Os hóspedes desfrutam de café da manhã buffet e podem saborear pratos indonésios e italianos no restaurante Cantarel. A pousada conta ainda com piscina, bar e terraço ao sol."),
         "address": "Estrada Serramar de Itaipuaçu, 19 - Numero 600 - Itaipuaçu, Niterói - RJ",
         "gallery": ["images/pousada4_1.png","images/pousada4_2.png","images/pousada4_3.png","images/pousada4_4.png","images/pousada4_5.png"]}
        ]
    global all_items

    all_items.extend(pousada)
    return "Pousadas", pousada,r"images\pousada_cat.jpg"


def explorar_estacionamento():
    estacionamento  = [
        {"name": "Sm Estacionamento",
         "image": "images/estacionamento1.png",
         "description": ("É uma opção conveniente para quem busca estacionamento na região, com acesso fácil a Itaipuaçu."),
         "address": "aaaaaaaaa",
         "gallery": ["images/estacionamento1.png","images/estacionamento1_1.png","images/estacionamento1_2.png"]},

        {"name": "Estacionamento Nossa senhora do Amparo", 
        "image": "images/estacionamento2.png",
        "description": ("Estacionamento rotativo que oferece uma opção prática para quem precisa estacionar na região central da cidade."),
        "address": "Avenida Nossa Senhora do Amparo 53, Maricá - RJ",
        "gallery": ["images/estacionamento2.png","images/estacionamento2_1.png","images/estacionamento2_2.png"]},

        {"name":"Estacionamento MariPark",
         "image": "images/estacionamento3.png",
         "description": ("Estacionamento rotativo localizado no bairro Araçatiba, em Maricá."),
         "address": "Rua Álvares de Castro, 460b - Eldorado, Maricá - RJ",
         "gallery": ["images/estacionamento3.png","images/estacionamento3_1.png","images/estacionamento3_2.png"]},
      ]
    global all_items

    all_items.extend(estacionamento)
    return "Estacionamento ", estacionamento, r"images\estacionamento_cat.jpg"
