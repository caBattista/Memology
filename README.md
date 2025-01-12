# Memology - A visual RAG system for finding fitting memes for the situation

A simple tool based on Python, Ollama and Langchain that indexes your local meme folder 
and suggests to you memes based on embeddings of descriptions created by llama3.2-vision.
It also renames the images with a short catchy title. 

*If you collected an ungodly amount of memes locally over the years like me. This tool ist for you!*

## Prerequisites
You will need to install 
  + ollama and llama3.2-vision as well as an embedding model such as nomic-embed-text
  + python (Im using 3.11) (requirements.txt coming)
You need a decent graphics card. I'm having good results with a RTX4070.

## Usage
  1) First you will need to index your memes. This will take a while depending on how many you have.

  2) To use it you need to start the rag.py script. It will scan your keystrokes and then you can use the arrow keys to 
  retrieve memes from your folder. Based on what you have previously written.
  You can copy something to the clipboard and then have it use that as the promt as well.

## Goal

This could be integrated into chat clients like Discord in the future. 
As it is not allowed as of now it remains a standalone python tool.
