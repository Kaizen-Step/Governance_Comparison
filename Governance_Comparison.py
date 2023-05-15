# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' Governance Comparison',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Governance Comparison')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Uniswap1.jpg'))

with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Compound8.png'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Voting_Mech.jpg'))


st.write("""


### Blockchain Governance: What Is It, What Types Are There and How Does It Work in Practice? ###  
Governance is a term that relates to decision making processes within an organization — who is responsible for what, how are major decisions being taken or implemented, is authority vested in a select few or distributed among all participants, etc. All those questions have different implications on an organization’s operational system, whether on a macro level (e.g. a decision on a new feature or goal) or on a micro level (e.g. how much is spent on marketing or who is responsible for a certain task). A successful governance model is usually what makes an organization click. Logically, there is no one-size-fits-all here — every model is situational and its viability largely depends on the specific circumstances.  While a participative democracy could work for some, having powers vested in a central authority may be preferable for others.    
Though as diverse as they may be, exemplary governance models are often centered around a set of qualities: transparency, integrity, effective performance and collaboration. In the context of blockchain, the discussion on governance currently revolves around two sets of models: centralized vs. decentralized and on-chain vs. off-chain. The first duel is the classic blockchain paradox which calls into question contemporary authority structures. The second refers to human involvement and the extent to which decision making processes are automated. Regardless of the governance structure, matters at stake typically involve network access, funding allocation, block size, reward systems, voting and decision making (e.g. reversing transactions via a fork).[[1]](https://watsonlaw.nl/en/blockchain-governance-what-is-it-what-types-are-there-and-how-does-it-work-in-practice/)    
      
### Nouns Governance Structure ###
Nouns DAO utilizes a fork of Compound Governance and is the main governing body of the Nouns ecosystem. The Nouns DAO treasury receives 100% of ETH proceeds from daily Noun auctions. Each Noun is an irrevocable member of Nouns DAO and entitled to one vote in all governance matters. Noun votes are non-transferable (if you sell your Noun the vote goes with it) but delegatable, which means you can assign your vote to someone else as long as you own your Noun.  
The proposal veto right was initially envisioned as a temporary solution to the problem of ‘51% attacks’ on the Nouns DAO treasury. While Nounders initially believed that a healthy distribution of Nouns would be sufficient protection for the DAO, a more complete understanding of the incentives and risks has led to general consensus within the Nounders, the Nouns Foundation, and the wider community that a more robust game-theoretic solution should be implemented before the right is removed.
The Nouns community has undertaken a preliminary exploration of proposal veto alternatives (‘rage quit’ etc.), but it is now clear that this is a difficult problem that will require significantly more research, development and testing before a satisfactory solution can be implemented.
Consequently, the Nouns Foundation anticipates being the steward of the veto power until Nouns DAO is ready to implement an alternative, and therefore wishes to clarify the conditions under which it would exercise this power.
The Nouns Foundation considers the veto an emergency power that should not be exercised in the normal course of business. The Nouns Foundation will veto proposals that introduce non-trivial legal or existential risks to the Nouns DAO or the Nouns Foundation, including (but not necessarily limited to) proposals that:
unequally withdraw the treasury for personal gain
bribe voters to facilitate withdraws of the treasury for personal gain
attempt to alter Noun auction cadence for the purpose of maintaining or acquiring a voting majority
make upgrades to critical smart contracts without undergoing an audit
There are unfortunately no algorithmic solutions for making these determinations in advance (if there were, the veto would not be required), and proposals must be considered on a case by case basis.[[2]](https://nouns.wtf/)     

### Compound Governance Structure ###
At Compound, our goal is to create financial infrastructure that applications and developers can rely on, forever. To get there, we intend to fully decentralize the Compound protocol — removing the largest single point of failure (our team), and creating an indestructible, open protocol that can evolve in entirely new ways.
Today, we’re proud to introduce a governance system that will replace the Compound protocol’s administrator with community governance — allowing you to suggest, debate, and implement changes to Compound — without relying on, or requiring, our team whatsoever.    
Participation starts with the Compound governance token, COMP.
In addition to being a standard ERC-20 asset, COMP allows the owner to delegate voting rights to the address of their choice; the owner’s wallet, another user, an application, or a DeFi expert. Anybody can participate in Compound governance by receiving delegation, without needing to own COMP. The token also includes code to query an address’ historical voting weight, which is useful for building complex voting systems.
We hope that COMP can set the standard for how governance tokens operate, and our team will write an Ethereum Improvement Plan (similar to the ERC-20 standard) to accelerate decentralization for the entire ecosystem.
COMP empowers community governance — it isn’t a fundraising device or investment opportunity. Until the decentralization process is complete, COMP will not be available to the public.[[3]](https://medium.com/compound-finance/compound-governance-5531f524cf68)  


### Uniswap Governance Structure ###
Several governance venues available to Uniswap governance are mentioned, each serving its own particular purpose. Gov.uniswap.org 278 is a Discourse forum for governance-related discussion. Community members must register for an account before sharing or liking posts. New members are required to enter 4 topics and read 15 posts over the course of 10 minutes before they are permitted to post themselves.     
Snapshot is a simple voting interface that allows users to signal sentiment off-chain. Votes on snapshot are weighted by the number of UNI delegated to the address used to vote.  
A governance portal can be accessed through the Uniswap interface 405. Votes can be delegated and cast through this portal. There are also several other governance interfaces that users can use to cast their votes.  
##### Phase 1: Temperature Check—Snapshot
The purpose of the Temperature Check is to determine if there is sufficient will to make changes to the status quo.   
To create a Temperature Check:  
Ask a general, non-biased question to the community on gov.uniswap.org 418 about a potential change (example: “Should Uniswap governance add liquidity mining for XYZ token?”). Forum posts should be labeled as follows: “Temperature Check - [Your Title Here]”. The forum post should include a link to the associated Snapshot poll.
Voters use Snapshot to indicate their interest in bringing it forward to the next stage. Snapshot poll lengths should be set to 3 days.
That’s it! You’ve just started the process of gaining support for a proposal. At the end of the 3 days, a majority vote with a 25k UNI yes-vote threshold wins.
If the Temperature check does not suggest a change from the status quo, the topic will be closed on the governance site. If the Temperature Check does suggest a change
##### Phase 2: Consensus Check — Discourse/Snapshot   #####   
The purpose of the Consensus Check is to establish formal discussion around a potential proposal.
To create a Consensus Check:
Use feedback from the Temperature Check post and create a new Snapshot poll which covers the options which have gained support. This poll can either be binary or multiple choice but should include the option “Make no change” or its equivalent. Set the poll duration to 5 days.
Create a new topic in the Proposal Discussion category on gov.uniswap.org 418 titled “Consensus Check — [Your Title Here]”. This will alert the community that this topic has already passed Temperature Check. Any topics beginning with Consensus Check that have not passed Temperature Check should be immediately be removed by community moderators. Make sure that the discussion thread links to the new Snapshot poll and the Temperature Check thread.
Reach out to your network to build support for the proposal. Discuss the proposal and solicit delegates to vote on it. Be willing to respond to questions on the Consensus Check topic. Share your view point, although try to remain as impartial as possible.
At the end of 5 days, whichever option has the majority of votes wins, and can be included in a governance proposal for Stage 3. A 50k UNI yes-vote quorum is required for the Consensus Check to pass. If the option “Make no change” wins, the Consensus Check topic should be closed by community moderators.  
##### Phase 3: Governance Proposal — Governance Portal
Phase 3 — Governance Proposal — is the final step of the governance process. The proposal should be based on the winning outcome from the Consensus Check and can consist of one or multiple actions, up to a maximum of 10 actions per proposal.
To create a Governance Proposal:
Write the code for your proposal, which can be voted on through any Governance Portal. More resources can be found here 219. All proposed code should be audited by a professional auditor. This auditing process could be paid or reimbursed by the community treasury.
Ensure at least 10 million UNI is delegated to your address in order to submit a proposal, or find a delegate who has enough delegated UNI to meet the proposal threshold to propose on your behalf.
Create a topic in the Proposal Discussion category on gov.uniswap.org 418 titled “Governance Proposal [Proposal Number] — [Your Title Here]” and link to any relevant Snapshot polls/discussion threads as well as the code audit report. Proposal numbers should be in a “UP###” format. For example, the first Uniswap Proposal should be titled UP001, the second UP002, and so on. Topics that begin with “Governance Proposal” that have not successfully passed the Temperature Check and Consensus Check stages should be removed by community moderators.
Call the propose() function of the Governor Alpha to deploy your proposal.
Once the propose() function has been called, a seven day voting period is started. Ongoing discussion can take place in the gov.uniswap.org 418 forum. If the proposal passes successfully, a two day timelock will follow before the proposed code is executed.[[4]](https://gov.uniswap.org/t/community-governance-process/7732)  


""")


st.write("""
## Methodology ##  

In this dashboard, we compare the governance structures of three protocols, namely nouns, uniswap, and compound, using the Coherent  ETHEREUM_DATASET_RAW_DECODED_AND_ENRICHED Data Sets tables. 
For the Nouns governance investigation, we used the 'ENRICHED.DECODED.DECODED_LOGS' table of the Coherent Enriched data set with the contract address '0x6f3E6272A167e8AcCb32072d08E0957F9c79223d' and the 'HASHABLE_SIGNATURE' of this table to filter each different functionality of this contract. First, we looked up the proposal using the "ProposalCreated" function, then we looked at "ProposalExecuted" and "ProposalCanceled" to see what happened to these proposals, and finally, using the "VoteCast" function, we totaled up all the votes that each proposal received. For Uniswap governance, the governance contract address changed over time, so we included addresses from the beginning to the present (such as "0xc4e172459f1e7939d522503b81afaac1014ce6f6" and "0xeCa491E162d157760F167c4DD92b45AE6E5Cf0f1") and investigated all of them in the same table.
 The Coherent tables also contained the description of the proposal and reasons for each vote. Finally, using these data sets, we compare the governance metrics across the three platforms, including the number of proposals, votes, addresses, and the outcomes of each proposal over time.
""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://watsonlaw.nl/en/blockchain-governance-what-is-it-what-types-are-there-and-how-does-it-work-in-practice/      
        2.https://nouns.wtf/     
        3.https://medium.com/compound-finance/compound-governance-5531f524cf68      
        4.https://gov.uniswap.org/t/community-governance-process/7732       
        5. Image source:https://twitter.com/compgovernance       

            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Project Supervisor:  [MetricsDao](https://github.com/Kaizen-Step/Russia_Ukraine_Conflict)**', icon="👨🏻‍💼")


with c2:
    st.info(
        '**Project Github:  [Ethereum After Shanghai Update](https://metricsdao.xyz/app/challenges)**', icon="💻")
    st.info(
        '**Data Set:  [Coherent-ETHEREUM DATASET RAW DECODED AND ENRICHED](https://app.snowflake.com/marketplace/listing/GZ2FQZL2LXD/coherent-ethereum-dataset-raw-decoded-and-enriched?search=coherent)**', icon="🧠")
