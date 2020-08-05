
import discord
import time
############### VAJA TEHA ##########
# 1. Logi fail käskudest

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(message.content)
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            #print("BOT MESSAGE: pong")
        if message.content == 'exit':
            await client.close()
            #client.logout()
        print(message.author)
        print(message.author.nick)
        if message.author.name + "#" + message.author.discriminator == "marcus99661#6338":
            await message.channel.send("admin")
        
        if message.content.split(" ")[0] == "kursuseMuutmine":
            await message.channel.send("Tehtud kursuse muudatus " + message.content.split(" ")[1] + " ja " + message.content.split(" ")[2])

client = MyClient()
client.run('NzM4ODA4MTg3ODIxNDkwMjM2.XyRSvg.myvR6TCXwOn8hpiC0RFoB63fva4')


#TOKEN = 'NzM4ODA4MTg3ODIxNDkwMjM2.XyRSvg.myvR6TCXwOn8hpiC0RFoB63fva4'
#GUILD = "marcus99661's server"
'''
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!!!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
async def test(ctx):
    await ctx.send("tere")

bot.run('NzM4ODA4MTg3ODIxNDkwMjM2.XyRSvg.myvR6TCXwOn8hpiC0RFoB63fva4')
'''