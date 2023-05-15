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


st.write("""  The Uniswap protocol employs an on-chain voting mechanism to facilitate decision-making and governance processes within the platform. The voting mechanism enables UNI token holders to actively participate in shaping the direction and evolution of Uniswap.
When a governance proposal is submitted, a voting period begins during which UNI token holders can cast their votes on the proposal. The voting period typically lasts for a predefined duration, allowing sufficient time for token holders to review and evaluate the proposal.
The voting power of UNI token holders is directly proportional to the number of tokens they hold. This means that those with a larger stake in the platform have a greater influence on the outcome of the vote. For example, if a token holder possesses 1% of the total UNI token supply, their vote will carry 1% of the total voting weight.
To cast their vote, UNI token holders can interact with the Uniswap governance interface or utilize compatible wallets and dApps that support the voting functionality. Through these platforms, token holders can indicate whether they are in favor of the proposal, against it, or choose to abstain.
To enhance participation and decentralization, Uniswap also introduced a delegation feature. This allows UNI token holders to delegate their voting power to specific addresses or trusted entities, known as delegates. Delegation empowers token holders to assign their voting rights to individuals or organizations they trust to make decisions aligned with their interests. Delegates can cast votes on behalf of the token holders who have delegated their voting power.
    """)


if Collection == 'Weekly':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Weekly Vote Weight Based On Supporter')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly VOTES Power')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(50), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Recent Propsal Based On Supporters')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly NUMBER OF VOTES')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Weekly Vote Weight Based On Proposal IDs')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='VOTES Power')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_ADRESSES", color="SUPPORT",
                 title='Weekly Number of Adresses Based On Supporters')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='NUMBER OF Adresses')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

elif Collection == 'Daily':
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Block Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily VOTES Power')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df3.tail(50), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='VOTES Power')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                 title='Daily Number of Distinct Miners Before and After Shanghai Update')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily VOTES Power')
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

st.write("""  At the end of the voting period, the votes are tallied, and the proposal's outcome is determined based on the majority vote. If the proposal receives a sufficient majority of votes in favor, it is considered approved, and the proposed changes can be implemented.
Uniswap's on-chain voting mechanism ensures transparency, immutability, and tamper-proof decision-making. All voting activities and results are recorded on the Ethereum blockchain, making them publicly verifiable. This transparency fosters trust within the community and provides a clear audit trail of governance decisions.
Through the voting mechanism, Uniswap enables a decentralized governance process where the collective voice of the token holders shapes the protocol's direction. It emphasizes inclusivity, giving stakeholders the opportunity to express their opinions, contribute to discussions, and influence the platform's development.
By actively involving UNI token holders in the decision-making process, Uniswap strives to create a platform that aligns with the interests and needs of its community, fostering a vibrant and dynamic ecosystem within the decentralized finance (DeFi) space.
    """)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.bar(df3.tail(250), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='VOTES Power')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Uniswap_Query.jpg'))

##########################################################################
