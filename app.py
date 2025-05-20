import streamlit as st
import pandas as pd
import os

# Nome do arquivo CSV
ARQUIVO_CSV = 'veiculos.csv'

# Carregar dados existentes ou criar estrutura
def carregar_dados():
    if os.path.exists(ARQUIVO_CSV):
        return pd.read_csv(ARQUIVO_CSV)
    else:
        return pd.DataFrame(columns=["Marca", "Modelo", "Ano", "Placa"])

# Salvar novo dado no CSV
def salvar_veiculo(dados):
    dados.to_csv(ARQUIVO_CSV, index=False)

# Interface do Streamlit
st.set_page_config(page_title="Cadastro de Veículos", layout="centered")
st.title("🚗 Cadastro de Veículos")

# Carrega os dados existentes
dados = carregar_dados()

with st.form("formulario_veiculo"):
    st.subheader("Adicionar novo veículo")
    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    ano = st.text_input("Ano")
    placa = st.text_input("Placa").upper()
    
    enviado = st.form_submit_button("Cadastrar")

    if enviado:
        if not marca or not modelo or not ano or not placa:
            st.warning("Por favor, preencha todos os campos.")
        else:
            novo = pd.DataFrame([[marca, modelo, ano, placa]], columns=dados.columns)
            dados = pd.concat([dados, novo], ignore_index=True)
            salvar_veiculo(dados)
            st.success(f"Veículo {marca} {modelo} cadastrado com sucesso!")

st.divider()
st.subheader("📋 Veículos Cadastrados")

if dados.empty:
    st.info("Nenhum veículo cadastrado ainda.")
else:
    st.dataframe(dados, use_container_width=True)



