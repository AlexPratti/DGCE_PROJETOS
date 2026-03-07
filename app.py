import streamlit as st

# Configurações da página
st.set_page_config(page_title="DGCE Manutenção Industrial", layout="centered")

# Logo direto do GitHub
st.image(
    "https://raw.githubusercontent.com/AlexPratti/DGCE_PROJETOS/refs/heads/main/LOGO_ESCURA_DGCE.png",
    use_column_width=True
)

# Título
st.title("Plataforma DGCE Manutenção Industrial")
st.write("Selecione abaixo o aplicativo que deseja acessar:")

# CSS customizado para estilizar os botões com cores diferentes
st.markdown("""
    <style>
    .app-button {
        display: inline-block;
        width: 280px;
        padding: 15px;
        margin: 10px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: opacity 0.3s ease;
        color: white;
    }
    .app-button:hover {
        opacity: 0.85;
    }
    .capacitores { background-color: #2E8B57; }   /* verde */
    .arcflash { background-color: #B22222; }      /* vermelho */
    .curtocircuito { background-color: #1E90FF; } /* azul */
    .sistema { background-color: #8B008B; }       /* roxo */
    </style>
""", unsafe_allow_html=True)

# Layout em duas colunas
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a class="app-button capacitores" href="https://c-lculobancocapacitores-tne9epqsrh64gtwaakzyax.streamlit.app/" target="_blank">Cálculo Banco de Capacitores</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button arcflash" href="https://calculo-arc-flash-hb8eujmejx23kk2skfn9nr.streamlit.app/" target="_blank">Cálculo Arc Flash</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a class="app-button curtocircuito" href="https://short-circuit-calc-e5u5dmgap2uqfdtbkc3d4e.streamlit.app/" target="_blank">Cálculo de Curto-Circuito</a>', unsafe_allow_html=True)
    st.markdown('<a class="app-button sistema" href="https://sistemael-trico-whsavdbi3zt3jxzmegbhfr.streamlit.app/" target="_blank">Sistema Elétrico</a>', unsafe_allow_html=True)

# Rodapé
st.write("---")
st.write("© 2026 DGCE Manutenção Industrial")
