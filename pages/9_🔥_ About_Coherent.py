# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='About Coherent',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Coherent Enriched DataSet Pros and Cons 📑 ')
st.text(" \n")
st.text(" \n")
st.info("""

The Enriched dataset, Coherent's most recent Ethereum decoded data collection, is an original, accurate endeavor. I will provide some ideas, though, that could help it get better.
The timestamp is typically absent from databases, so in order to add time to queries, we must join tables that have block-decoded dates. One of the essential characteristics of data is time, which is largely consumed during the surfing data stage, making it tedious to join the tables again. Additionally, because transaction hashes are such widely used data, and the first step in comprehending the tables is usually to use an ETH scan to check the table's results and understand the columns. It might be a good idea to include transaction hashes in all tables.
""")

st.image(Image.open('Images/Feedback.jpg'))

st.text(" \n")
st.text(" \n")
st.info("""

Although sharing the project's open source code on Github with the previous Ethereum raw data has some drawbacks, I sincerely appreciate it and hope it can be done in the future.
""")


st.image(Image.open('Images/Github.jpg'))
st.text(" \n")
st.image(Image.open('Images/Coherent.png'))
