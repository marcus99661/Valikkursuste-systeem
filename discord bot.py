
import discord
from discord import Embed
from discord import Colour
import time
from kursuseMuutmine import kursuseEemaldamine
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

        #### 1. force addAdmin NIMI, 2. force removeAdmin NIMI, 3. force adminList NIMI, 4. force kursuseEemaldamine NIMI KURSUS, 5.(ilma ruumi kontrollita) force kursuseLisamine NIMI KURSUS
        
        admin_prefix = "force "
        prefix = "!!!"
        ### admin commandid
        if message.content.split(" ")[0] == admin_prefix.replace(" ", ""):
            if message.author.name + "#" + message.author.discriminator in adminid:
                await message.channel.send("force command")
                sõnum = message.content.split(" ")
                if sõnum[1] ==  "ping":
                    await message.channel.send("force pong")
                elif sõnum[1] ==  "kursuseEemaldamine":
                    nimi = sõnum[2]
                    kursus = sõnum[3]
                    #await message.channel.send('Eemaldasin ' + nimi + ' kursuselt "' + kursus + '"')
                    await message.channel.send(kursuseEemaldamine(nimi, kursus))
                elif sõnum[1] ==  "help":
                    await message.channel.send("google.com")
                    '''
                    await message.channel.send("ADMINI COMMANDID:")
                    await message.channel.send("force ping - Saadab admini ping käsu")
                    await message.channel.send("force kursuseEemaldamine NIMI KURSUS - Sunnib õpilase eemaldamist kursuselt")
                    for i in range(0, 10):
                        await message.channel.send("spam " + str(i))
                    '''
                    
                elif sõnum[1] == "exit":
                    await message.channel.send("EXIT")
                    await client.close()
                else:
                    await message.channel.send("Ei tunne käsku ära")
            else:
                await message.channel.send("Ei ole admini õigusi")
        #### tavalised commandid
        elif message.content.startswith(prefix):
            sõnum = message.content.split(" ")
            if sõnum[0] == prefix + 'ping':
                await message.channel.send('pong')
                #print("BOT MESSAGE: pong")
            if sõnum[0] == prefix +'exit': ######## hiljem eemaldada
                await message.channel.send("EXIT")
                await client.close()
                #client.logout()
        else:
            pass
            #await message.channel.send("polnud command")

        #print(message.author)
        #print(message.author.nick)
        '''
        if message.author.name + "#" + message.author.discriminator == "marcus99661#6338":
            await message.channel.send("admin")
        '''
        
        if message.content.split(" ")[0] == "kursuseMuutmine":
            await message.channel.send("Tehtud kursuse muudatus " + message.content.split(" ")[1] + " ja " + message.content.split(" ")[2])

adminid = []
with open("adminid.txt") as file:
    for i in file: ########################### KONTROLLIDA VB
        adminid.append(i.replace("\n", ""))
        #adminid = ["marcus99661#6338", "test1#0000"]
print(adminid)

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