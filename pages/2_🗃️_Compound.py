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
st.set_page_config(page_title=' Compound Governance -  Ethereum After Shanghai Update',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🧩 Compound Governance')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Compound_Proposal_Created_Table':
        return pd.read_csv('Data/Compound/Compound_Created_Table.csv')
    elif query == 'Compound_voted_daily':
        return pd.read_csv('Data/Compound/Compound_Vote_Daily.csv')
    elif query == 'Compound_voted_weekly':
        return pd.read_csv('Data/Compound/Compound_Vote_Weekly.csv')
    return None


Compound_Proposal_Created_Table = get_data('Compound_Proposal_Created_Table')
Compound_voted_daily = get_data('Compound_voted_daily')
Compound_voted_weekly = get_data('Compound_voted_weekly')

df = Compound_Proposal_Created_Table
df2 = Compound_voted_daily
df3 = Compound_voted_weekly
#################################################################################################
st.write(""" ### Compound Finance Governance ##  """)

st.write(""" The Compound protocol is a decentralized lending and borrowing platform built on the Ethereum blockchain. One of the distinguishing features of Compound is its unique governance structure that empowers token holders to actively participate in shaping the protocol's future.
  """)


st.info(""" ##### In This Compound Governance Section you can find: ####

* Compound Governance structure
* Compound Governance outcomes
* Compound Voting Mechanisms
* Voting results


""")


#################################################################################################
st.write(""" ### Compound Governance structure """)
st.write(""" Compound operates on a decentralized governance model where decisions are made through on-chain voting by the platform's native governance token holders, known as COMP token holders. The COMP token serves as a governance and utility token, giving holders the ability to propose and vote on changes to the protocol.
Through the use of the COMP token, token holders can submit proposals for various protocol upgrades, parameter adjustments, and new feature implementations. These proposals can encompass a wide range of topics, such as introducing new assets to the platform, modifying interest rates, or enhancing the protocol's functionality.
Once a proposal is submitted, COMP token holders have the opportunity to vote on the proposal directly on the blockchain. The voting power is proportional to the number of COMP tokens held by each voter. This means that those with a larger stake in the platform have a greater influence on the outcome of the vote.
The voting process is transparent and publicly verifiable, providing a high level of accountability within the governance system. Additionally, COMP token holders have the ability to delegate their voting rights to other addresses, allowing them to entrust their voting power to trusted entities or community representatives.
For a proposal to be implemented, it typically requires a sufficient majority of votes in favor of the proposal. Once approved, the protocol changes are executed automatically, ensuring a seamless integration of the approved updates.
The Compound governance structure reflects the ethos of decentralization, fostering a community-driven decision-making process. By giving COMP token holders the power to participate in the protocol's governance, Compound aims to create a platform that is responsive to the needs and desires of its user base. This decentralized governance model promotes transparency, inclusivity, and the collective evolution of the protocol over time.
""")


st.table(df.head(10))

# # Europian House Price Index
# fig = px.bar(df2, x="DATE", y="TOTAL_DAILY_DIFFICULTY", color="STATUS",
#              title='ETH Total Difficulty')
# fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
#                   yaxis_title='Difficulty')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# # Europian House Price Index
# fig = px.area(df2, x="DATE", y="DAILY_DIFFICULTY", color="STATUS",
#               title='ETH Daily Difficulty')
# fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
#                   yaxis_title='Difficulty')
# st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
st.text(" \n")
st.text(" \n")
c1, c2 = st.columns(2)

with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
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
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.write(""" ## Compound Voting Mechanisms  """)
with c2:
    st.image(Image.open('Images/Voting_Mech.jpg'))


st.write("""  When a 'Compound' holder votes, 1 Noun NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Nouners. In Figure 4 below, we can see that as the population of Noun holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Compound DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Compound, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Compound has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
    """)


if Collection == 'Weekly':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Block Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Block')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(50), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Miners')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Miners')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_ADRESSES", color="SUPPORT",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Miners')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

elif Collection == 'Daily':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Block Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Block')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(50), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Miners')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Miners')
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

st.write(""" ## Compound Voting Results  """)

st.write("""  When a 'Compound' holder votes, 1 Noun NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Nouners. In Figure 4 below, we can see that as the population of Noun holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Compound DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Compound, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Compound has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
    """)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.bar(df3.tail(250), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Number of Miners')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Compound_Quary.jpg'))

##########################################################################
