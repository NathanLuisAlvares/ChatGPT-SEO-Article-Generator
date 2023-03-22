import streamlit as st
import openai

openai.api_key = "Paste your api here"
st.title("SEO Article Writer with ChatGPT")

def generate_article(keyword, writing_style, word_count):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
        {"role":"user", "content":"Write a SEO optimized word article about" + keyword},
        {"role":"user", "content":"This article should be in style" + writing_style},
        {"role":"user", "content":"This article length should be" + str(word_count)}
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)
    return result
    # return "This is a test article generated without any API calls."

keyword = st.text_input("Enter a keyword")
writing_style = st.selectbox("Select a writing style", 
    ["Narrative", "Descriptive", "Academic", "Expository", "Persuasive", "Creative", "Technical", "Journalistic"])
word_count = st.slider("Select word count", min_value=300, max_value=1000, step=100, value=300)
submit_button = st.button(
    label="Generate Article", 
    help="Click to generate your SEO article", 
    key="generate_button"
)

if submit_button:
    with st.spinner("Generating article..."):
        article = generate_article(keyword, writing_style, word_count)
        st.write(article)
        st.download_button(
            label="Download Article", 
            data=article, 
            file_name='Article.txt', 
            mime='text/txt'
        )