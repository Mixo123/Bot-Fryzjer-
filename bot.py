import discord

client = discord.Client()


@client.event
async def on_message(message):
    # komendy
    if message.content.find("f!help") != -1:
        await message.channel.send("```CSS\n""Bot Fryzjer do uslug""\n"
                                   "Prefix = f!\n"
                                   "1. Pepejpg\n"
                                   "2. Ping\n"
                                   "3. Obama""```"
                                   "```")

    if message.content.find("f!ping") != -1:
        await message.channel.send("pong :ping_pong:  ")

    if message.content.find("f!obama") != -1:
        await message.channel.send("obama")

    # jpg
    if message.content.find("f!pepejpg") != -1:
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/580098417267572817/580111305239953455/pepe-the-frog-vinyl-sticker.png")


client.run("NTc5NzEwMzY5OTY3Mzc0MzQ2.XOKuCg.03lnuauOCRMf3bBJnt4EcYOFJEw")
