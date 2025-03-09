from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeEmbeddings
import os
from pinecone import Pinecone, ServerlessSpec
import time
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_openai.embeddings import OpenAIEmbeddings

from langchain_core.prompts import ChatPromptTemplate

loader=PyPDFLoader("/home/rohithvijayan/Desktop/s8_project/legalmind/core/ipc_act.pdf")
docs=loader.load()


text_splitter=CharacterTextSplitter(separator='\n',chunk_size=1000,chunk_overlap=200)
chunks=text_splitter.split_documents(docs)
print(f'number of chunks is {len(chunks)}')
#print(chunks)

openaiEmbedding=OpenAIEmbeddings(model="text-embedding-3-large",batch_size=32)
model_name = 'pinecone-sparse-english-v0'
embeddings = PineconeEmbeddings(
    model=model_name,
    pinecone_api_key='pcsk_jgLR3_QvZDbNgoPsjNFiNscJtcw8jnnhLSira283uCptMVCPy7DjXqRZ6KnjWYv6H5gDN'
,batch_size=32,input_type="text")
pc=Pinecone(api_key='pcsk_jgLR3_QvZDbNgoPsjNFiNscJtcw8jnnhLSira283uCptMVCPy7DjXqRZ6KnjWYv6H5gDN')

spec=ServerlessSpec(cloud='aws',region='us-east-1')

index_name = "rag-getting-started"
namespace = "resume-rohith"

if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name,metric='cos',
                    spec=spec)
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

docsearch = PineconeVectorStore.from_documents(
    documents=chunks,
    index_name=index_name,
    embedding=embeddings,
    namespace=namespace,
    
)
time.sleep(10)

retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
print(retrieval_qa_chat_prompt)

prompt=ChatPromptTemplate.from_messages([("system","You are an Indian Legal Genius chatbot with immense knowledge of Indian laws, including the Indian Penal Code and other related legislations. Answer all user questions based solely on the provided context. Ensure your responses are in simple language, avoiding technical jargon as much as possible.STRICLY AVOID USE OF ANY SYMBOLS like '*','-' etc.GENERATE  RESPONSE IN STRUCTURED AND FORMATTED WAY.If legal terms are used, provide a subsequent explanation in layman's terms.:<context>{context}</context>"),("human","{input}")])

retriever=docsearch.as_retriever()

llm = ChatOpenAI(
    openai_api_key=os.environ.get('OPENAI_API_KEY'),
    model_name='gpt-4o-mini',
    temperature=0.5
)
combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)

retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

i=0
while i<1:
    question=input("ask question")
    response=retrieval_chain.invoke({'input':question})
    print(response['answer'])
   # print("SOURCE OF ANSWER IS: ",response['context'])
    i=int(input("do u want to continue\t0. yes\t1.No\n"))
