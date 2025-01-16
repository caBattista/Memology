from helpers import *
import glob
import re
from pathlib import Path

memes = glob.glob(
    fr"//7_Memes/**/*", recursive=True)

for path in memes:
    p = Path(path)
    print(path)
    if (".jpg" in path.lower() or ".png" in path.lower()) and ("_" not in p.stem):
        memeMeaning = doImage(f"""Describe the meme and it's meaning briefly in no more than 3 sentences. 
                                      Do not try to interpret too much into it and focus what is seen.""", path)
        title = doText(
            "Generate one single short title containing no more than 3 words based on the following context: " + memeMeaning)

        memeFileName = re.sub('[^A-Za-z0-9 ]+', '',
                              title).replace(" ", "_").lower()

        newPath = Path(p.parent, f"{memeFileName}{p.suffix}")
        p.rename(newPath)

        memeFileContent = newPath.absolute().as_posix() + ", " + \
            title + "\n" + memeMeaning

        print(memeFileContent + "\n")

        f = open("./descriptions/" + memeFileName +
                 ".txt", "w", encoding="utf-8")
        f.write(memeFileContent)
        f.close()
