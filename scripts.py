import random, os, PIL, json
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
class scriptClass:
    def __init__(self) -> None:
        f = open('storage.json')
        self.data = json.load(f)
        f.close()
        self.responses = []
        self.fonts = []
        for file in os.listdir(r'C:\Windows\Fonts'):
            if file.endswith(".ttf"):
                self.fonts.append(file)
        total = 0
        for i in self.data:
            self.responses.append(i)
            y = 0
            for x in self.data[i]:
                y += 1
            print(f"{i}:{y}")
            total += y
        print(f"Total:{total}")
        

    def generateQuote(self) -> str:
        # get event that occurs
        choice = random.choice(self.data["Events"])
        # find the keyword for each response
        for response in self.responses:
            x = choice.find(response)
            if x != -1:
                # remove the keyword and replace with a ending statement
                return choice[:x] + random.choice(self.data[response])

    def generateImage(self) -> str:
        dirs = os.listdir(os.getcwd() + "\images\\")
        mood = random.choice(dirs)
        files = random.choice(os.listdir(f'{os.getcwd()}\images\\{mood}'))
        return (f'{os.getcwd()}\images\\{mood}\\{files}')
        

    def overlayQuote(self, image, quote) -> str:
        img = Image.open(image)
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype(random.choice(self.fonts), 30)
        pos = 1
        colour = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
        while len(quote) > 30:
            I1.text((5,5 * pos), quote[:30] + '-', fill=(colour), font=myFont)
            pos += 6
            quote = quote[30:]
        I1.text((5,5 * pos), quote, fill=(colour), font=myFont)
        img.save("send_file.png")
        return f"{os.getcwd()}\\send_file.png"

    
    def clearCache(self, image) -> None:
        os.remove(f"{os.getcwd()}\\send_file.png")


# runs the logic behind the discord interface