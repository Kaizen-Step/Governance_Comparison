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
st.title('🧶 Compound Governance')

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
    elif query == 'Modified_Compound_Proposal_Created':
        return pd.read_csv('Data/Compound/Modified_Compound_Created_Table.csv')
    elif query == 'Modified_Compound_voted_daily':
        return pd.read_csv('Data/Compound/Modified_Compound_Vote_Daily.csv')
    elif query == 'Modified_Compound_voted_weekly':
        return pd.read_csv('Data/Compound/Modified_Compound_Vote_Weekly.csv')
    elif query == 'Modified_Compound_Vote':
        return pd.read_csv('Data/Compound/Modified_Compound_Vote_ID.csv')
    return None


Compound_Proposal_Created_Table = get_data('Compound_Proposal_Created_Table')
Compound_voted_daily = get_data('Compound_voted_daily')
Compound_voted_weekly = get_data('Compound_voted_weekly')
Modified_Compound_Proposal_Created = get_data(
    'Modified_Compound_Proposal_Created')
Modified_Compound_voted_daily = get_data('Modified_Compound_voted_daily')
Modified_Compound_voted_weekly = get_data('Modified_Compound_voted_weekly')
Modified_Compound_Vote = get_data('Modified_Compound_Vote')


df = Compound_Proposal_Created_Table
df2 = Compound_voted_daily
df3 = Compound_voted_weekly
df11 = Modified_Compound_Proposal_Created
df111 = df11.groupby(['PROPOSAL_STATUES'])[
    'PROPOSAL_ID'].count().reset_index()
df112 = Modified_Compound_Proposal_Created
df113 = df112.groupby(['PROPOSAL_STATUES'])[
    'PROPOSER'].nunique().reset_index()
df12 = Modified_Compound_voted_daily
df13 = Modified_Compound_voted_weekly
df14 = Modified_Compound_Vote
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

c1, c2 = st.columns(2)

with c2:
    fig = px.pie(df111, values='PROPOSAL_ID', names='PROPOSAL_STATUES',
                 title='Percentages of Proposal Outcome in Compound Governance')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c1:
    # Daily Number of Distinct Miners Before and After Shanghai Update
    fig = px.bar(df113, x="PROPOSAL_STATUES", y="PROPOSER", color="PROPOSAL_STATUES",
                 title='Number of Unique Proposer In Compound Proposals')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Number of Unique Proposers')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Most Recent Proposal Outcome  """)


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


st.write("""  The Compound protocol implements an on-chain voting mechanism to facilitate governance decisions and empower COMP token holders to actively participate in shaping the platform's future.
When a governance proposal is submitted, it undergoes a voting process that allows COMP token holders to express their opinion on the proposed change. The voting mechanism enables token holders to collectively determine whether the proposal should be implemented or rejected.
To cast their votes, COMP token holders can interact with the Compound governance interface or use compatible wallets and dApps that support the voting functionality. The voting process is conducted on-chain, meaning that all voting activities and results are recorded on the Ethereum blockchain, ensuring transparency and immutability.
The voting power of COMP token holders is directly proportional to the number of tokens they hold. If a token holder possesses 1% of the total COMP token supply, their vote will carry 1% of the total voting weight. This mechanism ensures that those with a larger stake in the platform have a greater influence on the outcome of the vote.
    """)


if Collection == 'Weekly':

    c1, c2 = st.columns(2)

    with c1:
        # Daily Number of Distinct Miners Before and After Shanghai Update
        fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_VOTES", color="SUPPORT",
                     title='Weekly Vote Weight Based On Supporter')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='Weekly VOTES Power')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Daily Number of Distinct Miners Before and After Shanghai Update
        fig = px.bar(df14.head(25), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                     title='Recent Propsal Based On Supporters')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='Weekly NUMBER OF VOTES')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        # Daily Number of Distinct Miners Before and After Shanghai Update
    with c2:
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
    c1, c2 = st.columns(2)

    with c1:
        # Daily Number of Distinct Miners Before and After Shanghai Update
        fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="SUPPORT",
                     title='Daily Block Before and After Shanghai Update')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='Daily VOTES Power')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Daily Number of Distinct Miners Before and After Shanghai Update
        fig = px.bar(df14.head(50), x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
                     title='Daily Number of Distinct Miners Before and After Shanghai Update')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='VOTES Power')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        # Daily Number of Distinct Miners Before and After Shanghai Update
    with c2:
        fig = px.bar(df2, x="DAILY", y="NUMBER_OF_VOTES", color="PROPOSAL_ID",
                     title='Daily Number of Distinct Miners Before and After Shanghai Update')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='Daily VOTES Power')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
        # Daily Number of Distinct Miners Before and After Shanghai Update
        fig = px.bar(df3, x="WEEKLY", y="NUMBER_OF_ADRESSES", color="SUPPORT",
                     title='Weekly Number of Adresses Based On Supporters')
        fig.update_layout(legend_title=None, xaxis_title=None,
                          yaxis_title='NUMBER OF Adresses')
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

st.write("""  For a proposal to be approved, it generally requires a sufficient majority of votes in favor. Once the voting period concludes, the votes are tallied, and the outcome is determined. If the proposal receives the necessary majority of votes, it is considered approved, and the proposed changes can be implemented.
The Compound governance mechanism also allows for delegation, enabling COMP token holders to delegate their voting rights to specific addresses or trusted entities. Delegation enables token holders to assign their voting power to individuals or organizations they trust to make decisions aligned with their interests. Delegates can cast votes on behalf of the token holders who have delegated their voting power.
The on-chain voting mechanism within Compound ensures transparency, security, and decentralized decision-making. It provides a verifiable record of all voting activities and results, allowing anyone to audit the governance process.
By incorporating the voting mechanism, Compound encourages community participation and involvement in governance decisions. It enables token holders to contribute to the protocol's development, propose changes, and influence the parameters and functioning of the platform.
Through the voting mechanism, Compound aims to create a decentralized governance process that reflects the collective will of the COMP token holders. This mechanism ensures that the protocol remains adaptable, responsive to the needs of its users, and evolves in line with the changing dynamics of the decentralized finance (DeFi) ecosystem.
    """)

# Daily Number of Distinct Miners Before and After Shanghai Update
fig = px.bar(df14, x="PROPOSAL_ID", y="NUMBER_OF_VOTES", color="SUPPORT",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='VOTES Power')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################

st.text(" \n")

st.info(""" #### SnowFlake Query: #### """)

st.image(Image.open('Images/SQL_Compound_Quary.jpg'))

##########################################################################
