import streamlit as st
from blog_generator import generate_blog

st.title("📝 LLaMA Blog Generator")

prompt = st.text_input("Enter blog topic or prompt")
max_words = st.slider("Max words", 50, 1000, 300)
audience = st.selectbox("Target audience", ["General", "Students", "Tech Professionals", "Marketers", "Researchers"])

if st.button("Generate Blog"):
    with st.spinner("Generating..."):
        blog = generate_blog(prompt, max_words, audience)
        st.markdown("### ✍️ Generated Blog:")
        st.write(blog)
