# Para executar, primeiro instale a biblioteca necessária:
# No terminal, digite: pip install streamlit

import streamlit as st
from collections import defaultdict

# --- Banco de Dados de Produtos COMPLETO E REVISADO ---
# A primeira descrição na lista de cada produto é a que será exibida na interface.
# As outras servem como palavras-chave para a busca interna.
product_data = {
    # Refrigerantes (Coca-Cola)
    '110255': ['Coca-Cola Lata 220ml', 'coca 220'],
    '110130': ['Coca-Cola Lata 350ml', 'coca lt 350', 'coca lata'],
    '110574': ['Coca-Cola Lata 350ml Pack 6un', 'coca lt p6'],
    '110658': ['Coca-Cola Lata 350ml Pack 12un', 'coca lt p12'],
    '110663': ['Coca-Cola PET 200ml', 'coca 200ml', 'cocacola mini'],
    '110122': ['Coca-Cola PET 600ml', 'coca 600'],
    '110583': ['Coca-Cola Retornável PET 1L', 'coca ls', 'coca 1l retornavel'],
    '110301': ['Coca-Cola PET 1,5L', 'coca 1,5l', 'coca 1.5'],
    '110440': ['Coca-Cola PET 2L', 'coca 2l'],
    '110584': ['Coca-Cola Retornável PET 2L', 'coca 2l retornavel'],
    '110441': ['Coca-Cola PET 2,5L', 'coca 2,5l', 'coca 2.5'],
    '110444': ['Coca-Cola PET 3L', 'coca 3l'],
    '110140': ['Coca-Cola Retornável Vidro 200ml', 'coca rgb 200'],
    '110132': ['Coca-Cola Retornável Vidro 290ml (KS)', 'coca ks'],
    '110112': ['Coca-Cola Bag 18L (Postmix)', 'coca bag 18l'],

    # Refrigerantes (Coca-Cola Zero/Sem Açúcar)
    '110256': ['Coca-Cola Sem Açúcar Lata 220ml', 'coca zero 220'],
    '113130': ['Coca-Cola Sem Açúcar Lata 350ml', 'coca zero lata', 'coca zero lt'],
    '112899': ['Coca-Cola Zero Lata 350ml Pack 12un', 'coca zero lt p12'],
    '110664': ['Coca-Cola Sem Açúcar PET 200ml', 'coca zero 200'],
    '113139': ['Coca-Cola Sem Açúcar PET 600ml', 'coca zero 600'],
    '113127': ['Coca-Cola Sem Açúcar PET 1,5L', 'coca zero 1.5l'],
    '113106': ['Coca-Cola Sem Açúcar PET 2L', 'coca zero 2l'],
    '113123': ['Coca-Cola Sem Açúcar PET 2,5L', 'coca zero 2.5l'],
    '113133': ['Coca-Cola Zero Retornável Vidro 290ml (KS)', 'coca zero ks'],
    '113107': ['Coca-Cola Sem Açúcar Retornável PET 2L', 'coca zero retornavel 2l'],
    '110367': ['Coca-Cola Zero Bag 5L (Postmix)', 'coca zero bag'],
    '110287': ['Coca-Cola Plus Café Lata 220ml', 'coca cafe'],

    # Refrigerantes (Fanta)
    '110330': ['Fanta Laranja Lata 350ml', 'fanta laranja lt'],
    '110600': ['Fanta Laranja PET 200ml', 'fanta laranja 200'],
    '110339': ['Fanta Laranja PET 600ml', 'fanta laranja 600'],
    '110327': ['Fanta Laranja PET 1,5L', 'fanta laranja 1.5l'],
    '110306': ['Fanta Laranja PET 2L', 'fanta laranja 2l'],
    '110333': ['Fanta Laranja Retornável Vidro 290ml (KS)', 'fanta laranja ks'],
    '110318': ['Fanta Laranja Retornável PET 2L', 'fanta laranja retornavel 2l'],
    '110601': ['Fanta Laranja Zero Lata 350ml', 'fanta laranja zero lt'],
    '111006': ['Fanta Laranja Zero PET 2L', 'fanta laranja zero 2l'],
    '110430': ['Fanta Uva Lata 350ml', 'fanta uva lt'],
    '110604': ['Fanta Uva PET 200ml', 'fanta uva 200'],
    '110439': ['Fanta Uva PET 600ml', 'fanta uva 600'],
    '110427': ['Fanta Uva PET 1,5L', 'fanta uva 1.5l'],
    '110406': ['Fanta Uva PET 2L', 'fanta uva 2l'],
    '110433': ['Fanta Uva Retornável Vidro 290ml (KS)', 'fanta uva ks'],
    '110435': ['Fanta Uva Retornável PET 2L', 'fanta uva retornavel 2l'],
    '110344': ['Fanta Guaraná Lata 350ml', 'fanta guarana lt'],
    '110605': ['Fanta Guaraná PET 200ml', 'fanta guarana 200'],
    '110349': ['Fanta Guaraná PET 1,5L', 'fanta guarana 1.5l'],
    '110348': ['Fanta Guaraná PET 2L', 'fanta guarana 2l'],
    '110428': ['Fanta Guaraná Retornável PET 2L', 'fanta guarana retornavel 2l'],
    '110621': ['Fanta Guaraná Zero Lata 350ml', 'fanta guarana zero lt'],
    '110388': ['Fanta Guaraná Zero PET 2L', 'fanta guarana zero 2l'],
    '110670': ['Fanta Caju Lata 350ml', 'fanta caju lt'],
    '110671': ['Fanta Caju PET 2L', 'fanta caju 2l'],
    '112505': ['Fanta Maracujá Lata 350ml', 'fanta maracuja lt'],
    '112506': ['Fanta Maracujá PET 2L', 'fanta maracuja 2l'],
    '112924': ['Fanta Mistério Chucky Punch Lata 350ml', 'fanta misterio'],
    '110310': ['Fanta Laranja Bag 10L (Postmix)', 'fanta laranja bag'],
    '110410': ['Fanta Uva Bag 10L (Postmix)', 'fanta uva bag'],
    '110382': ['Fanta Guaraná Bag 10L (Postmix)', 'fanta guarana bag'],

    # Refrigerantes (Sprite e Schweppes)
    '110549': ['Sprite Lata 350ml', 'sprite lt'],
    '110623': ['Sprite PET 200ml', 'sprite 200'],
    '110551': ['Sprite PET 2L', 'sprite 2l'],
    '110532': ['Sprite Retornável Vidro 290ml (KS)', 'sprite ks'],
    '110626': ['Sprite Sem Açúcar Lata 350ml', 'sprite zero lt'],
    '110506': ['Sprite Sem Açúcar PET 2L', 'sprite zero 2l'],
    '110599': ['Sprite Lemon Fresh PET 510ml', 'sprite lemon fresh 510'],
    '110565': ['Sprite Lemon Fresh PET 1,5L', 'sprite lemon fresh 1.5l'],
    '110510': ['Sprite Sem Açúcar Bag 10L (Postmix)', 'sprite zero bag'],
    '112030': ['Schweppes Citrus Lata 350ml', 'schweppes citrus lt'],
    '112027': ['Schweppes Citrus PET 1,5L', 'schweppes citrus 1.5l'],
    '112033': ['Schweppes Tônica Lata 350ml', 'schweppes tonica lt'],
    '110633': ['Schweppes Tônica Sem Açúcar Lata 350ml', 'schweppes tonica zero lt'],
    '110475': ['Schweppes Tônica Pink Lata 220ml', 'schweppes pink'],

    # Sucos (Ades)
    '110465': ['Ades Laranja TP 200ml', 'ades laranja 200'],
    '110464': ['Ades Maçã TP 200ml', 'ades maca 200'],
    '110466': ['Ades Uva TP 200ml', 'ades uva 200'],
    '110461': ['Ades Abacaxi TP 1L', 'ades abacaxi 1l'],
    '110462': ['Ades Laranja TP 1L', 'ades laranja 1l'],
    '110463': ['Ades Maçã TP 1L', 'ades maca 1l'],
    '110460': ['Ades Uva TP 1L', 'ades uva 1l'],
    '110457': ['Ades Morango TP 1L', 'ades morango 1l'],
    '110458': ['Ades Pêssego TP 1L', 'ades pessego 1l'],

    # Sucos (Del Valle e Kapo)
    '113032': ['Del Valle Kapo Caju 200ml', 'kapo caju'],
    '113042': ['Del Valle Kapo Laranja 200ml', 'kapo laranja'],
    '113056': ['Del Valle Kapo Maçã 200ml', 'kapo maca'],
    '113045': ['Del Valle Kapo Morango 200ml', 'kapo morango'],
    '113046': ['Del Valle Kapo Uva 200ml', 'kapo uva'],
    '112810': ['Del Valle Frut Laranja PET 200ml', 'dv frut laranja 200'],
    '112812': ['Del Valle Frut Uva PET 200ml', 'dv frut uva 200'],
    '112815': ['Del Valle Frut Frutas Cítricas PET 200ml', 'dv frut citricas 200'],
    '112817': ['Del Valle Frut Limão PET 200ml', 'dv frut limao 200'],
    '114585': ['Del Valle Frut Uva PET 450ml', 'dv frut uva 450'],
    '113666': ['Del Valle Frut Laranja PET 1L', 'dv frut laranja 1l'],
    '113670': ['Del Valle Frut Uva PET 1L', 'dv frut uva 1l'],
    '112809': ['Del Valle Frut Laranja PET 1,5L', 'dv frut laranja 1.5l'],
    '114619': ['Del Valle Frut Uva PET 1,5L', 'dv frut uva 1.5l'],
    '112816': ['Del Valle Frut Frutas Cítricas PET 1,5L', 'dv frut citricas 1.5l'],
    '114622': ['Del Valle Frut Limão PET 1,5L', 'dv frut limao 1.5l'],
    '114437': ['Del Valle Néctar Maracujá Lata 290ml', 'dv nectar maracuja lt'],
    '114438': ['Del Valle Néctar Pêssego Lata 290ml', 'dv nectar pessego lt'],
    '114439': ['Del Valle Néctar Uva Lata 290ml', 'dv nectar uva lt'],
    '113726': ['Del Valle Néctar Manga Lata 290ml', 'dv nectar manga lt'],
    '114647': ['Del Valle Néctar Abacaxi TP 1L', 'dv nectar abacaxi 1l'],
    '114645': ['Del Valle Néctar Laranja TP 1L', 'dv nectar laranja 1l'],
    '114646': ['Del Valle Néctar Manga TP 1L', 'dv nectar manga 1l'],
    '114649': ['Del Valle Néctar Maracujá TP 1L', 'dv nectar maracuja 1l'],
    '114648': ['Del Valle Néctar Pêssego TP 1L', 'dv nectar pessego 1l'],
    '114644': ['Del Valle Néctar Uva TP 1L', 'dv nectar uva 1l'],
    '114578': ['Del Valle Néctar Caju Sem Açúcar TP 1L', 'dv nectar caju zero'],
    '114654': ['Del Valle Néctar Pêssego Sem Açúcar TP 1L', 'dv nectar pessego zero'],
    '114653': ['Del Valle Néctar Uva Sem Açúcar TP 1L', 'dv nectar uva zero'],
    '114625': ['Del Valle 100% Suco Laranja TP 1L', 'dv 100 laranja'],
    '114472': ['Del Valle 100% Suco Maçã TP 1L', 'dv 100 maca'],
    '114623': ['Del Valle 100% Suco Uva TP 1L', 'dv 100 uva'],

    # Chás e Matte Leão
    '113688': ['Ice Tea Leão Limão PET 300ml', 'ice tea limao 300'],
    '113687': ['Ice Tea Leão Pêssego PET 300ml', 'ice tea pessego 300'],
    '113530': ['Ice Tea Leão Limão PET 1,5L', 'ice tea limao 1.5l'],
    '113529': ['Ice Tea Leão Pêssego PET 1,5L', 'ice tea pessego 1.5l'],
    '113696': ['Ice Tea Leão Limão Zero PET 300ml', 'ice tea limao zero 300'],
    '113689': ['Ice Tea Leão Pêssego Zero PET 300ml', 'ice tea pessego zero 300'],
    '113686': ['Ice Tea Leão Pêssego Zero PET 1,5L', 'ice tea pessego zero 1.5l'],
    '113740': ['Leão Fuze Ice Tea Limão Zero PET 1,5L', 'fuze zero'],
    '113716': ['Ice Tea Leão Limão com Gás Lata 290ml', 'ice tea limao com gas'],
    '113717': ['Matte Leão Limão com Gás Lata 290ml', 'matte com gas'],
    '113517': ['Matte Leão Natural Copo 300ml', 'matte copo'],
    '113518': ['Matte Leão Limão Copo 300ml', 'matte copo limao'],
    '113519': ['Matte Leão Natural Zero Copo 300ml', 'matte copo zero'],
    '113710': ['Matte Leão Natural PET 300ml', 'matte 300'],
    '113709': ['Matte Leão Limão PET 300ml', 'matte limao 300'],
    '113712': ['Matte Leão Limão Zero PET 300ml', 'matte limao zero 300'],
    '113711': ['Matte Leão Natural Zero PET 300ml', 'matte zero 300'],
    '113697': ['Matte Leão Natural PET 1,5L', 'matte 1.5l'],
    '113699': ['Matte Leão Limão PET 1,5L', 'matte 1.5l limao'],
    '113708': ['Matte Leão Pêssego PET 1,5L', 'matte pessego 1.5l'],
    '113707': ['Matte Leão Limão Zero PET 1,5L', 'matte limao zero 1.5l'],
    '113698': ['Matte Leão Natural Zero PET 1,5L', 'matte zero 1.5l'],
    '112800': ['Leão Guaraná PET 300ml', 'guarana leao'],

    # Água e CO2
    '113322': ['Água Crystal sem Gás Copo 310ml', 'agua copo s/gas'],
    '113323': ['Água Crystal sem Gás PET 350ml', 'agua 350 s/gas'],
    '113324': ['Água Crystal com Gás PET 350ml', 'agua 350 c/gas'],
    '113325': ['Água Crystal sem Gás PET 500ml', 'agua 500 s/gas'],
    '113326': ['Água Crystal com Gás PET 500ml', 'agua 500 c/gas'],
    '113328': ['Água Crystal sem Gás PET 1,5L', 'agua 1.5l s/gas'],
    '113327': ['Água Crystal com Gás PET 1,5L', 'agua 1.5l c/gas'],
    '112824': ['Crystal Saborizada Maçã PET 510ml', 'crystal maca'],
    '112822': ['Crystal Saborizada Maracujá PET 510ml', 'crystal maracuja'],
    '6549': ['Cilindro CO2 6kg', 'co2 6kg'],
    '115101': ['CO2 6kg (Recarga)', 'recarga co2'],

    # Energéticos e Isotônicos
    '112666': ['Monster Energy Green Lata 473ml', 'monster verde'],
    '112646': ['Monster Energy Zero Sugar Lata 473ml', 'monster green zero'],
    '112669': ['Monster Ultra (Branco) Lata 473ml', 'monster branco'],
    '112676': ['Monster Mango Loco Lata 473ml', 'monster mango loco'],
    '112582': ['Monster Khaotic Lata 473ml', 'monster khaotic'],
    '112689': ['Monster Pacific Punch Lata 473ml', 'monster pacific punch'],
    '112584': ['Monster Pipeline Punch Lata 473ml', 'monster pipeline punch'],
    '112677': ['Monster Ultra Violet Lata 473ml', 'monster roxo'],
    '112580': ['Monster Ultra Watermelon Lata 473ml', 'monster watermelon'],
    '112806': ['Monster Ultra Fiesta Mango Lata 473ml', 'monster fiesta mango'],
    '112585': ['Monster Ultra Peachy Keen Lata 473ml', 'monster peachy keen'],
    '112675': ['Monster Absolutely Zero Lata 473ml', 'monster zero preto'],
    '112682': ['Reign Lemon HDZ Lata 473ml', 'reign lemon'],
    '112683': ['Reign Melon Mania Lata 473ml', 'reign melon'],
    '113245': ['Powerade Mountain Blast (Azul) PET 500ml', 'powerade azul'],
    '113246': ['Powerade Uva PET 500ml', 'powerade uva'],
    '113247': ['Powerade Laranja PET 500ml', 'powerade laranja'],
    '113248': ['Powerade Limão PET 500ml', 'powerade limao'],
    '113249': ['Powerade Frutas Tropicais PET 500ml', 'powerade tropical'],
    '113250': ['Powerade Tangerina PET 500ml', 'powerade tangerina'],
    '112900': ['Powerade Maçã Verde PET 500ml', 'powerade maca verde'],

    # Cervejas
    '112758': ['Estrella Galicia Lata 350ml', 'estrella galicia lt 350'],
    '112759': ['Estrella Galicia Lata 473ml', 'estrella galicia lt 473'],
    '112773': ['Estrella Galicia Long Neck 355ml', 'estrella galicia ln'],
    '112755': ['Estrella Galicia Garrafa 600ml', 'estrella galicia 600'],
    '112764': ['Estrella Galicia 0.0% Álcool Lata 330ml', 'estrella galicia zero'],
    '112774': ['1906 Reserva Especial Long Neck 355ml', 'cerveja 1906'],
    '112911': ['Cerpa Export Long Neck 350ml', 'cerpa export'],
    '112801': ['Tijuca Puro Malte Lata 350ml', 'tijuca lata'],
    '112877': ['Therezópolis Gold Lata 350ml', 'therezopolis gold lt 350'],
    '112820': ['Therezópolis Gold Lata 473ml', 'therezopolis gold lt 473'], # Código duplicado na lista original, unificado aqui
    '112878': ['Therezópolis Gold Lata 473ml (Alternativo)', 'therezopolis gold lt 473 alt'], # Código duplicado na lista original, unificado aqui
    '112754': ['Therezópolis Gold Long Neck 355ml', 'therezopolis gold ln'],
    '112873': ['Therezópolis Gold Garrafa 500ml', 'therezopolis gold 500'],
    '112771': ['Therezópolis Gold Garrafa 600ml', 'therezopolis gold 600'],
    '112859': ['Therezópolis Bock Garrafa 500ml', 'therezopolis bock'],
    '112832': ['Therezópolis Dunkel Garrafa 500ml', 'therezopolis dunkel'],
    '112834': ['Therezópolis IPA Garrafa 500ml', 'therezopolis ipa'],
    '112833': ['Therezópolis Weissbier Garrafa 500ml', 'therezopolis weiss'],
    '112807': ['Therezópolis Session IPA Long Neck 355ml', 'therezopolis session ipa ln'],
    '112799': ['Therezópolis Session IPA Lata 350ml', 'therezopolis session ipa lt'],

    # Destilados, Vinhos e Prontos para Beber
    '110491': ['Absolut & Sprite Lata 269ml', 'absolut sprite'],
    '112557': ['Jack Daniel\'s & Coca-Cola Lata 269ml', 'jack cola'],
    '112841': ['Aperol Garrafa 750ml', 'aperol'],
    '112875': ['Campari Garrafa 748ml', 'campari 748'],
    '112876': ['Campari Garrafa 998ml', 'campari 1l', 'campari'],
    '112845': ['Bulldog Gin Garrafa 750ml', 'bulldog'],
    '112882': ['SKYY Vodka Garrafa 750ml', 'skyy'],
    '112884': ['Dreher Garrafa 900ml', 'dreher'],
    '112879': ['Old Eight Whisky Garrafa 900ml', 'old eight'],
    '112843': ['Drury\'s Gin Garrafa 900ml', 'drurys'],
    '112838': ['Cynar Garrafa 900ml', 'cynar'],
    '112837': ['Sagatiba Pura Garrafa 700ml', 'sagatiba'],
    '112881': ['Sagatiba Maiara & Maraisa Garrafa 700ml', 'sagatiba maiara'],
    '112852': ['Sagatiba Rabo de Galo Garrafa 700ml', 'sagatiba rabo de galo'],
    '112798': ['Cinzano Pro Spritz Garrafa 750ml', 'cinzano spritz'],
    '112848': ['Cinzano Vermouth Rosso Garrafa 1L', 'cinzano rosso'],
    '112892': ['Cinzano 1757 Garrafa 1L', 'cinzano 1757'],
    '112840': ['Liebfraumilch Vinho Branco Garrafa 750ml', 'vinho alemao'],
    '110480': ['Schweppes Gin Tônica Garrafa 250ml', 'schweppes gt garrafa'],
    '110482': ['Schweppes Spritz Garrafa 250ml', 'schweppes spritz garrafa'],
    '110484': ['Schweppes Vodka & Citrus Garrafa 250ml', 'schweppes vodka garrafa'],
    '110476': ['Schweppes Mixed Gin Tônica Lata 269ml', 'schweppes gt lata'],
    '110477': ['Schweppes Mixed Gin Tônica Pink Lata 269ml', 'schweppes gt pink lata'],
    '110478': ['Schweppes Mixed Spritz Lata 269ml', 'schweppes spritz lata'],
    '110479': ['Schweppes Mixed Vodka & Citrus Lata 269ml', 'schweppes vodka lata'],
    
    # Doces
    '115820': ['Fruittella Mastigável Morango', 'fruittella morango'],
    '112808': ['Fruittella Swirl Caramelo', 'fruittella caramelo'],
    '115822': ['Fruittella Swirl Morango', 'fruittella swirl morango'],
    '115807': ['Mentos Frutas', 'mentos frutas'],
    '115808': ['Mentos Mint', 'mentos menta'],
    '115823': ['Mentos Rainbow', 'mentos rainbow'],
    '115828': ['Mentos Fanta Laranja', 'mentos fanta'],
    '115819': ['Mentos Spearmint', 'mentos spearmint'],
    '115830': ['Mentos Pure Fruit', 'mentos pure fruit'],
    '115838': ['Mentos Cool White Blue Raspberry', 'mentos cool blue'],
    '115839': ['Mentos Cool White Peppermint', 'mentos cool peppermint'],
    '115824': ['Mentos Pure Fresh Mint', 'mentos pf mint'],
    '115826': ['Mentos Pure Fresh Wintergreen', 'mentos pf wintergreen'],
    '115817': ['Mentos Pure Fresh Mint (Display)', 'mentos pure fresh mint display'],
    '115811': ['Mentos Pure Fresh Mint Garrafa', 'mentos pure fresh mint garrafa'],
    '115812': ['Mentos Pure Fresh Wintergreen Garrafa', 'mentos pure fresh wintergreen garrafa'],
    '115816': ['Mentos UP2U Garrafa', 'mentos up2u'],
}


# --- Preparação dos Dados para a Interface ---
description_to_code_map = {aliases[0]: code for code, aliases in product_data.items()}
product_display_list = sorted(description_to_code_map.keys())

# --- Lógica dos Botões ---
def add_product_to_order():
    """Função para adicionar produto ao clicar no botão."""
    selected_product = st.session_state.get("selected_product")
    quantity = st.session_state.get("quantity", 1)
    
    if selected_product:
        product_code = description_to_code_map[selected_product]
        st.session_state.order[product_code] += quantity
        st.toast(f"Adicionado: {quantity}x {selected_product}", icon="✅")
        # Limpa o selectbox para a próxima seleção (opcional)
        st.session_state.selected_product = None
    else:
        st.toast("Selecione um produto para adicionar.", icon="⚠️")

# --- Inicialização do Estado da Aplicação ---
if 'order' not in st.session_state:
    st.session_state.order = defaultdict(int)
if 'final_output' not in st.session_state:
    st.session_state.final_output = ""

# --- Interface Gráfica (GUI) ---
st.set_page_config(page_title="Sistema de Pedidos", layout="centered")

# Título e linha vermelha estética
st.title("Sistema de Automação de Pedidos")
st.markdown("<hr style='height:5px; border:none; color:#F40009; background-color:#F40009;' />", unsafe_allow_html=True)

# --- Seção 1: Dados do Cliente ---
with st.container(border=True):
    st.subheader("1. Dados do Cliente")
    col1, col2 = st.columns(2)
    with col1:
        client_code = st.text_input("Código do Cliente", key="client_code")
    with col2:
        client_name = st.text_input("Nome do Cliente", key="client_name")

# --- Seção 2: Adicionar Produtos ---
with st.container(border=True):
    st.subheader("2. Adicionar Produtos")
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_product = st.selectbox(
            "Selecione o Produto", 
            options=product_display_list, 
            index=None, 
            placeholder="Digite para buscar...",
            key="selected_product"
        )
    with col2:
        quantity = st.number_input("Quantidade", min_value=1, step=1, key="quantity")
    
    st.button("Adicionar Produto ao Pedido", on_click=add_product_to_order, use_container_width=True)

# --- Seção 3: Resumo do Pedido ---
with st.container(border=True):
    st.subheader("3. Resumo do Pedido")
    
    if not st.session_state.order:
        st.info("Nenhum item no pedido ainda.")
    else:
        for code, qty in st.session_state.order.items():
            desc = next((aliases[0] for c, aliases in product_data.items() if c == code), f"Produto Cód: {code}")
            st.markdown(f"- **{qty}x** {desc} `(Cód: {code})`")

# --- Seção 4: Ações e Finalização ---
st.markdown("---")
st.subheader("Ações Finais")
col1, col2 = st.columns(2)

with col1:
    if st.button("Limpar Pedido Atual", use_container_width=True):
        st.session_state.order = defaultdict(int)
        st.session_state.final_output = ""
        st.rerun()

with col2:
    if st.button("✅ Finalizar e Gerar Pedido", use_container_width=True, type="primary"):
        if not st.session_state.client_code or not st.session_state.client_name:
            st.error("ERRO: Preencha o Código e o Nome do Cliente antes de finalizar!")
        elif not st.session_state.order:
            st.error("ERRO: O pedido está vazio!")
        else:
            final_output_list = [f"{st.session_state.client_code.strip()} {st.session_state.client_name.strip()}"]
            for code, qty in sorted(st.session_state.order.items()):
                final_output_list.append(f"{code} {qty}")
            
            st.session_state.final_output = "\n".join(final_output_list)
            st.success("Pedido finalizado com sucesso! Veja o resultado abaixo.")
            st.balloons()

# Exibe o resultado final se ele existir
if st.session_state.final_output:
    st.subheader("Resultado Final (Pronto para Copiar)")
    st.code(st.session_state.final_output, language="text")