# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Nouns - Governance_Comparison',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('👓 Nouns Governance ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Nouns_Proposal_Created':
        return pd.read_csv('Data/Nouns/Noun_Propsoe_Created1.csv')
    elif query == 'Nouns_voted_daily':
        return pd.read_csv('Data/Nouns/Noun_Vote_Daily.csv')
    elif query == 'Nouns_voted_weekly':
        return pd.read_csv('Data/Nouns/Noun_Vote_weekly.csv')
    return None


Nouns_Proposal_Created = get_data('Nouns_Proposal_Created')
Nouns_voted_daily = get_data('Nouns_voted_daily')
Nouns_voted_weekly = get_data('Nouns_voted_weekly')

df = Nouns_Proposal_Created
df2 = Nouns_voted_daily
df3 = Nouns_voted_weekly
#################################################################################################
st.write(""" ###  Nouns Governance structure ##  """)

st.write(""" 

The Nouns protocol is a unique and innovative blockchain platform that revolves around the concept of owning and trading nouns.Decentralized governance is a key principle in the blockchain ecosystem, aiming to distribute decision-making power among participants and ensure the platform's long-term sustainability and evolution.
  """)


st.info(""" ##### In This Nouns Governance Section you can find: ####

* Nouns Governance structure
* Governance outcomes
* Nouns Voting Mechanisms
* Voting results





""")
#########################################################################
st.write(""" ## Nouns System Description  """)

st.write(""" This website is a new model of essential DAO (decentralized autonomous organizations), where you can even see that a communal treasury taken to the next level with governance and ownership. In this platform anyone who owns one of these tokens and holds a noun, nft, essentially gets a vote in what happens with this treasury,So if you just go to the website, which is [nouns. wtf], you can see the current auction. With the current concept of one little noun every 15 minutes, the auctions can run every day every 15 minutes, and in real time, there are 28156 Ethereum, or 50.87 million dollars, in this wallet. The only way to access this wallet because of the only through this website, so you can't go to that wallet any other way, and as you can see, there's been 294 different proposals. To put up a proposal, you need to own a certain amount of these, and you need people that are going to vote on them. You can see the votes for it, or the voice against it. You can see people that abstained; it even tells you how many votes are needed, right? So I'm showing you the broad strokes of this so you can get an understanding of what little nouns really are, which is a crowd-funded treasury that can be accessed with a crowd vote. this decentralized autonomous organization It's incredibly cool. There are really interesting opportunities to get funded for, like, literally, ideas you might have that would help this group of little nouns grow. The whole goal of the Treasury department of the group is to figure out how to grow the brand. how to grow awareness around little nouns and the things that are important to those that are in little nouns, and it was started by a founder.
    """)

st.table(df.head(10))


# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df, x="DATE", y="NUMBER_OF_MINERS", color="STATUS",
#              title='Daily Number of Distinct Miners Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Number of Miners')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.area(df, x="DATE", y="DAILY_BLOCK", color="STATUS",
#               title='Daily Block Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Block')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#################################################################################################

st.text(" \n")
st.text(" \n")
c1, c2 = st.columns(2)


with c1:

    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.write(" ### Please Choose Weekly or Daily Chart ")
    st.text(" \n")
    Collection = st.selectbox('Weekly or Daily', options=[
        'Weekly', 'Daily'])

    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.write(""" ## Nouns Voting Mechanisms  """)
with c2:
    st.image(Image.open('Images/dao_voting2.png'))


st.write("""  When a 'Nouns' holder votes, 1 Noun NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Nouners. In Figure 4 below, we can see that as the population of Noun holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Nouns DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Nouns, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Nouns has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
    """)


if Collection == 'Weekly':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Nouns Weekly Vote Weight Based On Supporter ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(100), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Nouns Recenct Proposal Vote Based On Supporter ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Weekly Vote Weight Based On Proposals IDs')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

elif Collection == 'Daily':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Vote Weight Based On Supporter')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(200), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Recent Proposal Vote Based On Supporter')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Weekly Vote Weight Based On Proposals IDs')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="SUPPORT",
#              title='Daily Block Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Block')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df3.tail(100), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
#              title='Daily Number of Distinct Miners Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Number of Miners')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
#              title='Daily Number of Distinct Miners Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Number of Miners')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
#              title='Daily Block Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Block')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# # Daily Number of Distinct Miners Before and After Shanghai Update
# fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
#              title='Daily Block Before and After Shanghai Update')
# fig.update_layout(legend_title=None, xaxis_title=None,
#                   yaxis_title='Daily Block')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ## Nouns Voting Results  """)

st.write("""  When a 'Nouns' holder votes, 1 Noun NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Nouners. In Figure 4 below, we can see that as the population of Noun holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Nouns DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Nouns, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Nouns has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
    """)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.bar(df3.tail(250), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
             title='Each Proposal Vote Based On Supporter')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='NUMBER OF VOTES')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Noun_Quary.jpg'))
