# Memology - A visual RAG system for finding your memes on the fly

A simple tool based on Python, Ollama and Langchain that indexes your local meme folder 
and suggests to you memes based on embeddings of descriptions created by llama3.2-vision.
It also renames the images with a short catchy title.

To use it you need to start the rag.py script. It will scann your keystrokes and then you can use the arrow keys to 
retrieve the meme from your folder. Based on what you have previously written.
You can also copy something to the clipboard and then have it use that as the promt.

This could be integrated into chat clients like Discord in the future. 
As it is not allowed as of now it remains a standalone python tool.
