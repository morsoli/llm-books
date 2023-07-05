from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document


def test_qa():
    from langchain.chains.question_answering import load_qa_chain
    loader = TextLoader("./测试.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)
    qa_chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
    qa = RetrievalQA(combine_documents_chain=qa_chain, retriever=docsearch.as_retriever())
    qa.run()
    
def test_summary():
    from langchain.chains.summarize import load_summarize_chain
    
    text_splitter = CharacterTextSplitter()
    with open("./测试.txt") as f:
        state_of_the_union = f.read()
    texts = text_splitter.split_text(state_of_the_union)
    docs = [Document(page_content=t) for t in texts[:3]]
    chain = load_summarize_chain(OpenAI(temperature=0), chain_type="map_reduce")
    chain.run(docs)
    
def test_db_chain():
    from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
    db = SQLDatabase.from_uri("sqlite:///../user.db")
    llm = OpenAI(temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, use_query_checker=True)
    db_chain.run("有多少用户?")
    
def test_converstion():
    from langchain.chains import ConversationalRetrievalChain
    from langchain.memory import ConversationBufferMemory
    loader = TextLoader("./test.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectorstore.as_retriever(), memory=memory)
    query = "这本书包含哪些内容？"
    result = qa({"question": query})
    print(result)
    chat_history = [(query, result["answer"])]
    query = "还有要补充的吗"
    result = qa({"question": query, "chat_history": chat_history})
    print(result["answer"])


if __name__ == "__main__":
    test_converstion()