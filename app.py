import streamlit as st

# Configurações da página
st.set_page_config(page_title="DGCE Manutenção Industrial", layout="wide")

# Barra superior com logo à esquerda e título à direita
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(
        "https://raw.githubusercontent.com/AlexPratti/DGCE_PROJETOS/refs/heads/main/LOGO_ESCURA_DGCE.png",
        width=80
    )
with col_title:
    st.markdown("<h2 style='text-align: right; color: white;'>DGCE - Manutenção Industrial</h2>", unsafe_allow_html=True)

# CSS customizado para fundo escuro e botões cinza
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .app-button {
        display: inline-block;
        width: 280px;
        padding: 15px;
        margin: 10px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        background-color: #d3d3d3; /* cinza */
        color: black; /* letras pretas */
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: opacity 0.3s ease;
    }
    .app-button:hover {
        opacity: 0.85;
    }
    </style>
""", unsafe_allow_html=True)

st.write("Selecione abaixo o aplicativo que deseja acessar:")

# Layout em duas colunas para os botões
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a class="app-button" href="https://c-lculobancocapacitores-tne9epqsrh64gtwaakzyax.streamlit.app/" target="_blank">Cálculo Banco de Capacitores</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button" href="https://calculo-arc-flash-hb8eujmejx23kk2skfn9nr.streamlit.app/" target="_blank">Cálculo Arc Flash</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a class="app-button" href="https://short-circuit-calc-e5u5dmgap2uqfdtbkc3d4e.streamlit.app/" target="_blank">Cálculo de Curto-Circuito</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button" href="https://sistemael-trico-whsavdbi3zt3jxzmegbhfr.streamlit.app/" target="_blank">Sistema Elétrico</a>', unsafe_allow_html=True)

# Rodapé
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 DGCE Manutenção Industrial</p>", unsafe_allow_html=True)
