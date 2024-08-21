import streamlit as st
import time
import os

def notas_disponiveis():
    arquivos = []
    notas = []
    for arquivo in os.listdir(r'Y:\Publico\PS-SCM-COUNTRY LOGISTICS\Tableau\Base Consumos'):
        if arquivo.endswith('.xlsx'):
            arquivos.append(arquivo)
    for nota in arquivos:
        nota = nota[:-5]
        notas.append(nota)
    return notas

def main():
    notas = notas_disponiveis()
    nota = st.selectbox('Selecione a nota fiscal que deseja cadastrar:', notas, index=None, placeholder="Escolha uma opção")


    # st.title('TÍTULO')
    # st.write('texto')

    # input = st.text_input('digite')
    # selecionada = st.selectbox('selecione', ['1', '2'])
    # slider = st.slider('escolha', 0, 100, 10)
    # checkbox = st.checkbox('marque')
    # if st.button('clique'):
    #     st.write('vc apertou o botao')
    # with st.spinner('aguarde...'):
    #     time.sleep(3)
    # st.success('pronto')
    # upload = st.file_uploader('escolha', type=['pdf'])
    # if upload:
    #     st.write(f'vc fez o upload de: {upload.name}')
    # data = {'x': [1,2,3,4], 'y': [10,20,30,40]}
    # st.line_chart(data)

main()
