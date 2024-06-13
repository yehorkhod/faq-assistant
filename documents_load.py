# Imports
import os
from langchain.docstore.document import Document
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Loading environment
import dotenv
dotenv.load_dotenv()

# Links from robinhood investing FAQ
LINKS: list[str] = [
    'https://robinhood.com/us/en/support/articles/order-types/',
    'https://robinhood.com/us/en/support/articles/why-hasnt-my-order-been-filled/',
    'https://robinhood.com/us/en/support/articles/why-was-my-order-rejected/',
    'https://robinhood.com/us/en/support/articles/whats-an-untradable-stock/',
    'https://robinhood.com/us/en/support/articles/what-if-a-stock-is-delisted/',
    'https://robinhood.com/us/en/support/articles/why-dont-i-see-a-buy-button/',
    'https://robinhood.com/us/en/support/articles/not-enough-shares-error/',
]

# Directory where vector store will be saved
PERSIST_DIRECTORY: str = r'index'

# Create it if one hasn't been created yet
if PERSIST_DIRECTORY not in os.listdir():
    os.mkdir(PERSIST_DIRECTORY)


def load_documents_from_web(links: list[str]) -> list[Document]:
    # Loading documents
    loader: WebBaseLoader = WebBaseLoader(links)
    documents: list[Document] = loader.load()

    # Split documents into smaller chunks
    splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=64,
    )

    return splitter.split_documents(documents)


def create_vectorstore(documents: list[Document], persist_directory: str) -> None:
    # Embedding model
    embeddings: OpenAIEmbeddings = OpenAIEmbeddings()
    # Vector store
    vectorstore: Chroma = Chroma.from_documents(documents, embeddings, persist_directory=persist_directory)


# Creating vector store
if __name__ == '__main__':
    documents: list[Document] = load_documents_from_web(LINKS)
    create_vectorstore(documents, PERSIST_DIRECTORY)
