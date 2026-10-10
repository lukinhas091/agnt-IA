import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Admin Perfil - Humor", page_icon="🤡", layout="centered")

st.title("🤡 Gerador de Conteúdo - Humor Besteirol")
st.write("Automatize seu planejamento semanal para Instagram e TikTok com a pior (melhor) qualidade possível.")

# Barra lateral para a Chave de API
st.sidebar.header("Configurações")
api_key = st.sidebar.text_input("Chave de API (Google Gemini):", type="password")
st.sidebar.markdown("[Pegue sua chave gratuita aqui](https://aistudio.google.com/app/apikey)")

# Entrada do usuário
tema = st.text_input("Qual o tema ou nicho desta semana?", placeholder="Ex: Rotina de CLT cansado, universitário falido...")

# Botão de ação
if st.button("Gerar Calendário Completo"):
    if not api_key:
        st.warning("⚠️ Insira sua Chave de API na barra lateral para continuar.")
    elif not tema:
        st.warning("⚠️ Digite um tema para a semana.")
    else:
        try:
            # Configura a IA
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            prompt = f"""
            Você é um estrategista de conteúdo especializado em humor besteirol para Instagram (Reels, Feed, Stories) e TikTok.
            
            Crie um planejamento semanal para o tema: "{tema}".
            
            Retorne EXATAMENTE nesta estrutura:
            1. Calendário Semanal (Tabela Markdown com Dia/Hora, Formato, Ideia, Áudio Trend).
            2. Detalhamento (Roteiro, Legenda absurda e auto-depreciativa, Hashtags).
            3. Respostas prontas para comentários em tom debochado.
            4. Formato JSON com os dados do calendário para automação.
            """
            
            with st.spinner("Fritando os últimos neurônios para criar seu conteúdo..."):
                resposta = model.generate_content(prompt)
                
            st.success("Conteúdo gerado com sucesso!")
            st.markdown(resposta.text)
            
        except Exception as e:
            st.error(f"Deu ruim: {e}")