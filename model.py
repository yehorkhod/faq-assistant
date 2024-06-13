# Imports
from langchain_openai import  ChatOpenAI
from langchain_openai  import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

from documents_load import PERSIST_DIRECTORY


# Model parameters
MODEL_NAME: str = 'gpt-4o'
TEMPERATURE: float = 0.1

# LLM
llm: ChatOpenAI = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
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
template: PromptTemplate = PromptTemplate(
    input_variables=['context', 'question'],
    template='----------------------------------------------------------------\n' \
             'Fragments of our company FAQ-site that might be useful:\n' \
             '\n' \
             '{context}\n' \
             '----------------------------------------------------------------\n' \
             'User\'s question:\n' \
             '\n' \
             '{question}\n' \
             '----------------------------------------------------------------\n' \
             'Useful answer:'
)

# LLM chain
chain: ConversationalRetrievalChain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever()
)
