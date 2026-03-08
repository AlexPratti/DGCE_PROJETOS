import streamlit as st

# Configurações da página
st.set_page_config(page_title="DGCE Manutenção Industrial", layout="wide")

# Título com símbolo de raio ⚡ à esquerda
st.markdown("<h2 style='text-align: left; color: white;'>⚡ DGCE - Manutenção Industrial</h2>", unsafe_allow_html=True)

# CSS customizado para fundo preto e botões cinza com borda preta fina
st.markdown("""
    <style>
    .stApp {
        background-color: black;
    }
    .app-button {
        display: inline-block;
        width: 220px;
        padding: 12px;
        margin: 5px; /* espaçamento reduzido */
        font-size: 15px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        background-color: #d3d3d3; /* cinza */
        color: black; /* letras pretas */
        border-radius: 6px;
        border: 1px solid black; /* borda preta fina */
        cursor: pointer;
        transition: opacity 0.3s ease;
    }
    .app-button:hover {
        opacity: 0.85;
    }
    </style>
""", unsafe_allow_html=True)

st.write("Selecione abaixo o aplicativo que deseja acessar:")

# Layout em duas colunas bem próximas
col1, col2 = st.columns([1,1], gap="small")

with col1:
    st.markdown('<a class="app-button" href="https://c-lculobancocapacitores-tne9epqsrh64gtwaakzyax.streamlit.app/" target="_blank">Cálculo Banco de Capacitores</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button" href="https://calculo-arc-flash-hb8eujmejx23kk2skfn9nr.streamlit.app/" target="_blank">Cálculo Arc Flash</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a class="app-button" href="https://short-circuit-calc-e5u5dmgap2uqfdtbkc3d4e.streamlit.app/" target="_blank">Cálculo de Curto-Circuito</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button" href="https://sistemael-trico-whsavdbi3zt3jxzmegbhfr.streamlit.app/" target="_blank">Sistema Elétrico</a>', unsafe_allow_html=True)

# Rodapé
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 DGCE Manutenção Industrial</p>", unsafe_allow_html=True)
