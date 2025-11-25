import streamlit as st
import pandas as pd
import json
import os

# CONFIG
st.set_page_config(page_title="CinePython", page_icon="")

ARQUIVO = "catalogo.json"

# --- FUNÇÕES PARA SALVAR / CARREGAR ---
def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(st.session_state['catalogo'], f, indent=4, ensure_ascii=False)

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            st.session_state['catalogo'] = json.load(f)
    else:
        st.session_state['catalogo'] = []


# --- TELA DE LOGIN ---
def login_page():
    st.title(" Login - CinePython")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "123":
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("❌ Usuário ou senha incorretos!")


# --- INICIAR LOGIN ---
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login_page()
    st.stop()


# --- CARREGA DADOS QUANDO O USUÁRIO LOGA ---
if "catalogo" not in st.session_state:
    carregar_dados()

# --- INTERFACE PRINCIPAL ---
st.title(" CinePython: Gerenciador de Filmes")
st.write("Gerencie seus filmes e séries favoritos de forma visual!")

# MENU LATERAL
st.sidebar.header("Adicionar Novo Título")
nome = st.sidebar.text_input("Nome do Filme/Série")
genero = st.sidebar.selectbox("Gênero", ["Ação", "Comédia", "Drama", "Sci-Fi", "Terror", "Outro"])
ano = st.sidebar.number_input("Ano de Lançamento", min_value=1900, max_value=2025)
nota = st.sidebar.slider("Sua Nota", 0.0, 10.0, 5.0)

if st.sidebar.button("Cadastrar Filme"):
    if nome:
        novo_filme = {"Nome": nome, "Gênero": genero, "Ano": ano, "Nota": nota}
        st.session_state['catalogo'].append(novo_filme)
        salvar_dados()
        st.sidebar.success(f"✅ {nome} adicionado!")
    else:
        st.sidebar.error("❌ O nome é obrigatório!")


# BOTÃO LOGOUT
if st.sidebar.button("Sair do Sistema"):
    st.session_state["logado"] = False
    st.rerun()


# LISTAGEM PRINCIPAL
st.header("Meus filmes Assistidos")

if len(st.session_state['catalogo']) > 0:
    df = pd.DataFrame(st.session_state['catalogo'])
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)
    col1.metric("Total Assistido", len(df))
    col2.metric("Média de Notas", f"{df['Nota'].mean():.1f}")

    if st.button("Limpar Lista Completa"):
        st.session_state['catalogo'] = []
        salvar_dados()
        st.rerun()
else:
    st.info("Nenhum filme cadastrado ainda. Use a barra lateral! ")