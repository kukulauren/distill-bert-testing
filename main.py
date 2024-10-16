import streamlit as st
from transformers import pipeline
st.title("Tea chatbot")
context = """
Tea is an aromatic beverage prepared by pouring hot or boiling water over cured or fresh leaves of Camellia sinensis,
an evergreen shrub native to China and East Asia. After water, it is the most widely consumed drink in the world.
There are many different types of tea; some, like Chinese greens and Darjeeling, have a cooling, slightly bitter,
and astringent flavour, while others have vastly different profiles that include sweet, nutty, floral, or grassy
notes. Tea has a stimulating effect in humans primarily due to its caffeine content.

The tea plant originated in the region encompassing today's Southwest China, Tibet, north Myanmar and Northeast India,
where it was used as a medicinal drink by various ethnic groups. An early credible record of tea drinking dates to
the 3rd century AD, in a medical text written by Hua Tuo. It was popularised as a recreational drink during the
Chinese Tang dynasty, and tea drinking spread to other East Asian countries. Portuguese priests and merchants
introduced it to Europe during the 16th century. During the 17th century, drinking tea became fashionable among the
English, who started to plant tea on a large scale in India.

The term herbal tea refers to drinks not made from Camellia sinensis: infusions of fruit, leaves, or other plant
parts, such as steeps of rosehip, chamomile, or rooibos. These may be called tisanes or herbal infusions to prevent
confusion with 'tea' made from the tea plant.
"""

# Initialize the question-answering pipeline
question_answerer = pipeline(task="question-answering", model="distilbert-base-cased-distilled-squad")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Ask me anything about tea!"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        # Use the question-answerer to get the answer
        answer = question_answerer(question=prompt, context=context)

        # Prepare the response text
        response = answer['answer']

        # Display the final response
        st.markdown(response)

    # Append the final response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})