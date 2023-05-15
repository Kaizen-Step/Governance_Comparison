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
st.set_page_config(page_title='Uniswap Governance - Governance_Comparison',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🦄 Uniswap Governance ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Uniswap_Proposal_Created':
        return pd.read_csv('Data/Uniswap/Uniswap_Created_1.csv')
    elif query == 'Uniswao_voted_daily':
        return pd.read_csv('Data/Uniswap/Uni_vote.csv')
    elif query == 'Uniswao_voted_weekly':
        return pd.read_csv('Data/Uniswap/Uni_vote_Weekly.csv')
    return None


Uniswap_Proposal_Created = get_data('Uniswap_Proposal_Created')
Uniswao_voted_daily = get_data('Uniswao_voted_daily')
Uniswao_voted_weekly = get_data('Uniswao_voted_weekly')

df = Uniswap_Proposal_Created
df2 = Uniswao_voted_daily
df3 = Uniswao_voted_weekly

#################################################################################################
st.write(""" ###  Uniswap Governance ##  """)

st.write(""" 

The Uniswap protocol, a decentralized exchange platform built on the Ethereum blockchain, implements a unique governance structure that involves the active participation of UNI token holders. UNI tokens serve as the governance and utility token within the Uniswap ecosystem, providing holders with the ability to influence the platform's decision-making processes.
  """)


st.info(""" ##### In This Uniswap Governance Section you can find: ####

* Uniswap Governance structure
* Governance outcomes
* Uniswap Voting Mechanisms
* Voting results





""")
#########################################################################
st.write(""" ## Uniswap Governance Structure  """)

st.write(""" The governance structure of Uniswap is designed to be decentralized, transparent, and community-driven. UNI token holders play a crucial role in proposing and voting on governance proposals that impact the protocol's operations, upgrades, and fee structures.
Any individual or entity holding UNI tokens can submit a governance proposal, which can cover a broad range of topics, including changes to the protocol's parameters, introduction of new features, or modifications to the fee structure. Proposals are typically submitted through the official Uniswap governance interface or other community-led platforms.
Once a proposal is submitted, a voting period begins, during which UNI token holders can cast their votes either in favor, against, or abstain from the proposal. The voting power of UNI token holders is proportional to the number of tokens held, meaning that those with a larger stake in the platform have a greater influence on the outcome of the vote.
To enhance participation and delegation, Uniswap introduced a delegation feature that allows UNI token holders to delegate their voting power to specific addresses or trusted entities. This enables token holders who may not actively participate in voting to still have their voice heard through the delegates they choose.
For a proposal to be implemented, it typically requires a sufficient majority of votes in favor. Once a proposal passes, the changes are automatically executed, and the protocol is updated accordingly.
The Uniswap governance structure emphasizes decentralization, giving the community a direct say in the platform's evolution. It aims to create an inclusive environment where stakeholders can express their opinions, contribute to discussions, and shape the future of the protocol.
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
    st.write(""" ## Uniswap Voting Mechanisms  """)
with c2:
    st.image(Image.open('Images/dao_voting3.png'))


st.write("""  When a 'Uniswap' holder votes, 1 Uniswap NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Uniswapers. In Figure 4 below, we can see that as the population of Uniswap holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Uniswaps DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Uniswaps, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Uniswaps has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
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

st.write(""" ## Uniswaps Voting Results  """)

st.write("""  When a 'Uniswaps' holder votes, 1 Uniswap NFT is the equivalent of one vote. Votes can be delegated to other wallets including non-Uniswapers. In Figure 4 below, we can see that as the population of Uniswap holders increases, so does voter participation. Most proposals received votes "For" the proposal, but often the votes depend on the monetary amount from the treasury.   
The DAO has funded over 140 proposals successfully using only blockchain technology. This project, which is less than a year old and entirely self-funded, has gained a ton of attention for decentralized coordination, DAO execution, and a brand-new industry.
The beginning of Uniswaps DAO and DAOs in general is here.The value of the talented community and the projects that have been sponsored return value to Uniswaps, despite the fact that holding an NFT limits liquidity and DAOs require more coordination than centralized entities.
Despite the fact that DAOs are still in their infancy, Uniswaps has demonstrated the capacity to check off a number of previously difficult-to-achieve DAO-related boxes, including perpetual funding, social coordination, governance and voting, memetics, and a general crypto-native mission.
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

st.image(Image.open('Images/SQL_Uniswap_Query.jpg'))

##########################################################################
