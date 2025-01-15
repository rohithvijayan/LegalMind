from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import google.generativeai as genai
import os
##rag-libraries##
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeEmbeddings
from pinecone import Pinecone, ServerlessSpec
import time
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate,BaseChatPromptTemplate
################################################################
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY") 
model = genai.GenerativeModel("gemini-1.5-flash")
pinecone_api_key='pcsk_jgLR3_QvZDbNgoPsjNFiNscJtcw8jnnhLSira283uCptMVCPy7DjXqRZ6KnjWYv6H5gDN'
openaiEmbedding=OpenAIEmbeddings(model="text-embedding-ada-002")
pc=Pinecone(api_key=pinecone_api_key)
spec=ServerlessSpec(cloud='aws',region='us-east-1')
index_name = "rag-bot-index"
namespace = "rag-rohith"
prompt=ChatPromptTemplate.from_messages([("system","You are a specialized Indian Legal Expert chatbot designed to provide concise, context-specific responses related to Indian laws, including the Indian Penal Code and other relevant legislations. Answer user questions in simple, clear, and precise language, ensuring brevity while maintaining accuracy. Avoid technical jargon and symbols, and if legal terms are used, briefly explain them in layman's terms for clarity. Focus on delivering highly relevant and to-the-point replies, suitable for quick understanding without unnecessary details.:<context>{context}</context>"),("human","{input}")])
file_name=""
retrieval_chain=None
combine_docs_chain=None
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def ragbot(request):
    return render(request, 'core/ragbot.html')
def register(request):
    return render(request, 'core/signup.html')
def login(request):
    return render(request, 'core/login.html')
@csrf_exempt
def ragchat(request):
    global retrieval_chain
    if request.method == 'POST':
        #data=json.loads(request.body.POST.get("message"))
        #print(data)
        user_message=request.POST.get('message')
        print(user_message)
        #response=model.generate_content(f'Generate A  concise reply for the following message from user:{user_message}.STRICTLY AVOID USING SYMBOLS IN RESPONSE<MAKE SURE THE RESPONS IS CLEAN RAW FORMATTED TEXT')
        response=retrieval_chain.invoke({'input':user_message})
        answer=response['answer']
        print(answer)
        return JsonResponse({"botReply":answer})
    
    
@csrf_exempt
def fileHandler(request):
    global file_name
    if request.method=='POST' and request.FILES.get('file'):
        uploaded_file=request.FILES["file"]
        file_name = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))
        print(file_name)
        return JsonResponse({"message":"file uploaded success!"})
    

def extract_text(file_name):
    #load the pdf
    loader=PyPDFLoader(f'./media/{file_name}')
    doc=loader.load()
    ##extract the text from the pdf
    text_splitter=CharacterTextSplitter(separator='\n',chunk_size=1000,chunk_overlap=200)
    chunks=text_splitter.split_documents(doc)
    print(f'number of chunks is:{len(chunks)}')
    return chunks
def create_index_pc():
    global index_name,pc,spec,namespace,openaiEmbedding
    if index_name not in pc.list_indexes().names():
        pc.create_index(name=index_name,spec=spec,metric='cosine',dimension=1536)
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(2)
    
    
def embedding_creator(chunks):
    embeddings=PineconeVectorStore.from_documents(documents=chunks,embedding=openaiEmbedding,index_name=index_name,namespace=namespace)
    time.sleep(4)
    return embeddings
def create_rag_chain(embeddings):
    llm=ChatOpenAI(api_key=OPENAI_API_KEY,model_name='gpt-4o-mini',temperature=0.0)
    retreiver=embeddings.as_retriever(search_kwargs={"k": 5})
    combine_docs_chain=create_stuff_documents_chain(llm=llm,prompt=prompt)
    retreival_chain=create_retrieval_chain(retreiver,combine_docs_chain)
    return retreival_chain
def rag_chat(retreival_chain,question):
    response=retreival_chain.invoke({'input':{question}})
    answer=(response['answer'])
    print(answer)
    return answer

def embedder(request):
    global retrieval_chain
    create_index_pc()
    chunks=extract_text(file_name)
    embeddings=embedding_creator(chunks)
    retrieval_chain=create_rag_chain(embeddings)
    return JsonResponse({"message:":"embedding successfull,retrieval chain returned"})