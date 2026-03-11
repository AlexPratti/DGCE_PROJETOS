import streamlit as st

# Configurações da página
st.set_page_config(page_title="DGCE Manutenção Industrial", layout="wide")

# CSS customizado
st.markdown("""
    <style>
    .stApp {
        background-color: black;
    }
    .button-row {
        display: flex;
        justify-content: flex-start; /* alinhado à esquerda */
        flex-wrap: nowrap; /* todos em uma linha */
        margin-top: 10px;
        margin-bottom: 60px; /* espaçamento extra abaixo dos botões */
    }
    .app-button {
        display: inline-block;
        width: 220px;
        padding: 12px;
        margin-right: 10px;
        font-size: 15px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        background-color: #d3d3d3;
        color: black;
        border-radius: 6px;
        border: 1px solid black;
        cursor: pointer;
        transition: transform 0.2s ease, opacity 0.3s ease;
    }
    .app-button:hover {
        opacity: 0.85;
        transform: scale(1.05);
    }
    .subtitle {
        text-align: left;
        color: gray;
        margin-top: 5px;
    }
    .footer {
        text-align: left;
        color: gray;
        margin-top: 20px; /* espaçamento menor, pois já demos respiro nos botões */
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h2 style='text-align: left; color: white;'>⚡ DGCE - Manutenção Industrial</h2>", unsafe_allow_html=True)

# Texto de instrução
st.markdown("<p class='subtitle'>Selecione abaixo o aplicativo que deseja acessar:</p>", unsafe_allow_html=True)

# Botões em linha com espaçamento extra abaixo
st.markdown("""
<div class='button-row'>
    <a class="app-button" href="https://c-lculobancocapacitores-tne9epqsrh64gtwaakzyax.streamlit.app/" target="_blank">Cálculo Banco de Capacitores</a>
    <a class="app-button" href="https://short-circuit-calc-e5u5dmgap2uqfdtbkc3d4e.streamlit.app/" target="_blank">Cálculo de Curto-Circuito</a>
    <a class="app-button" href="https://calculadoraenergiaincidente-yqufhgaxaqr5uedwzbca93.streamlit.app/" target="_blank">Cálculo Arc Flash</a>
    <a class="app-button" href="https://sistemael-trico-whsavdbi3zt3jxzmegbhfr.streamlit.app/" target="_blank">Sistema Elétrico</a>
</div>
""", unsafe_allow_html=True)

# Rodapé
st.markdown("<p class='footer'>© 2026 DGCE Manutenção Industrial</p>", unsafe_allow_html=True)
