import streamlit as st
import time

def main():
    st.title('TÍTULO')
    st.write('texto')

    input = st.text_input('digite')
    selecionada = st.selectbox('selecione', ['1', '2'])
    slider = st.slider('escolha', 0, 100, 10)
    checkbox = st.checkbox('marque')
    if st.button('clique'):
        st.write('vc apertou o botao')
    with st.spinner('aguarde...'):
        time.sleep(3)
    st.success('pronto')
    upload = st.file_uploader('escolha', type=['pdf'])
    if upload:
        st.write(f'vc fez o upload de: {upload.name}')
    data = {'x': [1,2,3,4], 'y': [10,20,30,40]}
    st.line_chart(data)

    st.write('atualizadooo')
main()
