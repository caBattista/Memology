from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
import glob
from PIL import Image
from pynput import keyboard
from tkinter import Tk

memeDescriptions = glob.glob("descriptions/*", recursive=True)

texts = []
for path in memeDescriptions:
    print(path)
    f = open(path, "r", encoding="utf-8")
    texts.append(f.read())
    f.close()

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = InMemoryVectorStore.from_texts(texts,  embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

def getMeme(givenText):
    retrieved_documents = retriever.invoke(givenText)
    for page in retrieved_documents:
        print(fr"################### {givenText} ###################" + "\n\n" + page.page_content + "\n")
        img = Image.open(page.page_content.split(",")[0])
        img.show() 

print("Done indexing")

givenText = ""
def on_press(key):
    global givenText

    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char
        givenText += k
    except:
        k = key.name  # other keys

    if k in ['right']:  # keys of interest
        givenText = ""
    if k in ['left']:  # keys of interest
        #self.keys.append(k)  # store it in global-like variable
        getMeme(givenText)
    if k in ['down']:  # keys of interest
        getMeme(Tk().clipboard_get())

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

# while(True):
#     prmt = input("\n>>> ")
#     retrieved_documents = retriever.invoke(prmt)
#     for page in retrieved_documents:
#         print("\n################### NEW PAGE ###################\n\n" + page.page_content)
#         img = Image.open(page.page_content.split(",")[0])
#         img.show() 

