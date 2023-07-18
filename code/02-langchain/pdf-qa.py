from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader,PDFMinerLoader,PDFPlumberLoader,PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def qa(file, query, chain_type, k):
    # load document
    loader = PyMuPDFLoader(file)
    documents = loader.load()
    # split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    # select which embeddings we want to use
    embeddings = OpenAIEmbeddings()
    # create the vectorestore to use as the index
    db = Chroma.from_documents(texts, embeddings)
    # expose this index in a retriever interface
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})
    # create a chain to answer questions 
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type=chain_type, retriever=retriever, return_source_documents=True)
    result = qa({"query": query})
    print(result['result'])
    return result

def qa_result(prompt_text, select_chain_type, select_k):
    result = qa(file="./test.pdf", query=prompt_text, chain_type=select_chain_type, k=select_k)
    print(result)

if __name__ == "__main__":
    import langchain
    langchain.debug = True
    qa_result("可以仔细讲讲免赔额吗", "map_reduce", 3)