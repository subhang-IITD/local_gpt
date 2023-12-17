
# run the python script following this syntax like python chatgpt.py "the promt that you want to give to chatgpt"

# it will write the output in the output file output.txt



import os
import sys
import nltk

from langchain.document_loaders import TextLoader
from langchain.document_loaders import  DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI



import constants
os.environ["OPENAI_API_KEY"] = constants.APIKEY
query = sys.argv[1]

loader = TextLoader('data.txt')
# loader = DirectoryLoader('.', glob = '*.txt') 
index = VectorstoreIndexCreator().from_loaders([loader])


output = index.query(query, llm = ChatOpenAI())


with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output)

