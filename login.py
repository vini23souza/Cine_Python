import streamlit as st
import pandas as pd
import os
from PIL import Image
import json

# ---------------- CONFIG ----------------
st.set_page_config(page_title="CinePython", page_icon="", layout="wide")

# CSS ESTILO NETFLIX
st.markdown("""
    <style>
        body {
            background-color: #0d0d0d;
            color: white;
        }
        .movie-card {
            background-color: #1a1a1a;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(255,255,255,0.1);
            transition: 0.2s ease-in-out;
        }
        .movie-card:hover {
            transform: scale(1.05);
            box-shadow: 0px 4px 20px rgba(255,0,0,0.4);
        }
        img {
            border-radius: 10px;
        }
        .header-title {
            font-size: 40px;
            font-weight: 700;
            color: #e50914;
        }
    </style>
""", unsafe_allow_html=True)

# GARANTIR PASTA DE IMAGENS
if not os.path.exists("capas"):
    os.makedirs("capas")

# ---------------- BANCO DE DADOS ----------------
def carregar_dados():
    if os.path.exists("database.json"):
        with open("database.json", "r") as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open("database.json", "w") as f:
        json.dump(dados, f, indent=4)

catalogo = carregar_dados()

# ---------------- TÍTULO ----------------
st.markdown("<h1 class='header-title'>🎬 CinePython</h1>", unsafe_allow_html=True)
st.write("Seu catálogo de filmes em estilo Netflix!")

# ---------------- SIDEBAR – CADASTRO ----------------
st.sidebar.header("Adicionar Filme")

nome = st.sidebar.text_input("Nome do Filme")
genero = st.sidebar.selectbox("Gênero", ["Ação", "Comédia", "Drama", "Sci-Fi", "Terror", "Romance", "Outro"])
ano = st.sidebar.number_input("Ano", 1900, 2025)
nota = st.sidebar.slider("Nota", 0.0, 10.0, 5.0)
capa = st.sidebar.file_uploader("Capa do Filme", type=["jpg", "png", "jpeg"])

if st.sidebar.button("Cadastrar Filme"):
    if nome:
        caminho_capa = ""
        if capa:
            caminho_capa = f"capas/{nome.replace(' ', '_')}.png"
            img = Image.open(capa)
            img.save(caminho_capa)

        filme = {
            "Nome": nome,
            "Gênero": genero,
            "Ano": ano,
            "Nota": nota,
            "Capa": caminho_capa
        }

        catalogo.append(filme)
        salvar_dados(catalogo)
        st.sidebar.success("Filme adicionado!")
        st.rerun()
    else:
        st.sidebar.error("O nome é obrigatório!")

# ---------------- LISTAGEM ----------------
st.header("📚 Meu Catálogo")

if len(catalogo) == 0:
    st.info("Nenhum filme cadastrado ainda. Use o menu ao lado!")
else:
    cols = st.columns(4)
    i = 0

    for filme in catalogo:
        with cols[i]:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

            if filme["Capa"] and os.path.exists(filme["Capa"]):
                st.image(filme["Capa"], width=180)
            else:
                st.write("Sem capa")

            st.markdown(f"### {filme['Nome']}")
            st.write(f"🎭 {filme['Gênero']}")
            st.write(f"📅 {filme['Ano']}")
            st.write(f"⭐ {filme['Nota']}")

            st.markdown("</div>", unsafe_allow_html=True)

        i += 1
        if i == 4:
            cols = st.columns(4)
            i = 0

# ---------------- APAGAR TUDO ----------------
if st.button("🗑️ Apagar Catálogo Completo"):
    catalogo = []
    salvar_dados(catalogo)
    st.rerun()