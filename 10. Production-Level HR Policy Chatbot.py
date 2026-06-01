from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory

# Load HR policy PDF
loader = PyPDFLoader("ANN guide.pdf")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)

# Embeddings
embeddings = OllamaEmbeddings(model="llama3")

# Create vector DB
db = FAISS.from_documents(docs, embeddings)

# Retriever
retriever = db.as_retriever()

# Load LLM
llm = Ollama(model="llama3")

# Memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Conversational RAG
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

print("ANN Chatbot Started")
print("Type 'exit' to stop\n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    result = qa_chain({"question": query})

    print("Bot:", result["answer"])