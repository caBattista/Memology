from PIL import Image
import base64
import io
import ollama


def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        return img_base64


def doImage(promt, image_path):
    base64_image = image_to_base64(image_path)
    response = ollama.chat(
        model="llama3.2-vision:latest",
        messages=[{
            "role": "user",
            "content": promt,
            "images": [base64_image]
        }],
    )
    return response['message']['content'].strip()


def doText(promt):
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{
            "role": "user",
            "content": promt
        }],
    )
    return response['message']['content'].strip()


def writeText(text, path):
    f = open(path, "w", encoding="utf-8")
    f.write(text)
    f.close()
    return text


def log(text):
    print(text)
    f = open("log.txt", "a", encoding="utf-8")
    f.write(text)
    f.close()
    return text
