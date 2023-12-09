# Imports
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.vectorstores import Chroma
from documents_load import PERSIST_DIRECTORY

from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain


# Model name
MODEL_NAME = 'gpt-3.5-turbo'

# LLM
llm = ChatOpenAI(
    model_name=MODEL_NAME,
    temperature=0.1,
)

# Embedding model
embeddings: OpenAIEmbeddings = OpenAIEmbeddings()

# Loading vector store
vectorstore: Chroma = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings,
)
vectorstore.get()

# Prompt template
template = PromptTemplate(
    input_variables=['context', 'question'],
    template='''----------------------------------------------------------------
Fragments of our company FAQ-site that might be useful:

{context}
----------------------------------------------------------------
User's question:

{question}
----------------------------------------------------------------
Useful answer:'''
)

# LLM chain
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever()
)
