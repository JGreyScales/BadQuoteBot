import discord, os, json, time
from scripts import scriptClass


client = discord.Client()
sC = scriptClass()
f = open('config.json')
d = json.load(f)
f.close()
config = {
    "Prefix":d["Prefix"]
}



@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_message(message):
    prefix = config["Prefix"]

    if message.content[:len(prefix)].lower() == prefix:
        print(f'{message.author} used command {message.content[len(prefix):]}')
        content = message.content[len(prefix):].lower()
        if content[:6] == "prefix" and len(content[7:]) > 0:
            config["Prefix"] = content[7:]
            prefix = config["Prefix"]
            f = open('config.json', 'w')
            f.write(json.dump(config, f, indent=4))
            f.close()

        if content[:5] == "quote":
            if len(content[5:]) > 0:
                try:
                    x = int(content[5:])
                    for m in range(x):
                        await message.channel.send(sC.generateQuote())
                        time.sleep(.75)
                except(ValueError):
                    await message.channel.send("ValueError, Invalid input. Must be type [INT]")
            else:
                await message.channel.send(sC.generateQuote())

        if content[:5] == 'image':
            await message.channel.send(file=discord.File(sC.generateImage()))

        if content[:6] == 'qimage':
            img = sC.overlayQuote(sC.generateImage(), sC.generateQuote())
            await message.channel.send(file=discord.File(img))
            Sc.clearCache(img)



client.run(os.getenv("GreyBot"))
