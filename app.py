import streamlit as st

# Configurações da página
st.set_page_config(page_title="DGCE Manutenção Industrial", layout="centered")

# Logo da empresa (substitua pelo caminho ou URL da sua logo)
st.image("https://link-da-sua-logo.png", use_column_width=True)

# Título
st.title("Plataforma DGCE Manutenção Industrial")

st.write("Selecione abaixo o aplicativo que deseja acessar:")

# Botões retangulares com links
col1, col2 = st.columns(2)

with col1:
    if st.button("App 1 - Monitoramento"):
        st.markdown("[Abrir App 1](https://seu-app1.streamlit.app)", unsafe_allow_html=True)

    if st.button("App 2 - Relatórios"):
        st.markdown("[Abrir App 2](https://seu-app2.streamlit.app)", unsafe_allow_html=True)

with col2:
    if st.button("App 3 - Controle de Estoque"):
        st.markdown("[Abrir App 3](https://seu-app3.streamlit.app)", unsafe_allow_html=True)

    if st.button("App 4 - Gestão de Ordens"):
        st.markdown("[Abrir App 4](https://seu-app4.streamlit.app)", unsafe_allow_html=True)

# Rodapé
st.write("---")
st.write("© 2026 DGCE Manutenção Industrial")
