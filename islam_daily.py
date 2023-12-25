import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
from lxml import html

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

#To make the bot sync commands, appear as playing the following game, and to notify us when the bot is online
@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.activity.Game(name="getting daily islam"))
    print(f"{bot.user.name} has connected to Discord!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
        
#The following code is for the bot to send a message every 24hrs and sending specific messages from the designated URL using Xpath
@tasks.loop(hours=24)
async def scheduled_message():
    url = 'https://ahadith.co.uk'     
    response = requests.get(url)
    
    if response.status_code == 200:
        yes = html.fromstring(response.content)
        
        xpather = '/html/body/main/div[1]/div/div[1]/div/div[1]/div'
        
        element = yes.xpath(xpather)
        
        embed = discord.Embed(title="Your Daily Dose of Islam", color=discord.Color.red())
        
        channel = bot.get_channel(CHANNEL_ID)
        
        for i in element:
            embed.add_field(name=' ', value=i.text_content().strip(), inline=False)
            
        
        yesser = html.fromstring(response.content)
        
        xpathing = '/html/body/main/div[1]/div/div[1]/div/div[3]/div/div'
        
        fire = yesser.xpath(xpathing)
        
        for j in fire:
            embed.add_field(name=' ', value=j.text_content().strip(), inline=False)
            
        yessing = html.fromstring(response.content)
        
        xpathering = '/html/body/main/div[2]/div/article/div[3]/div[1]'
        
        water = yessing.xpath(xpathering)
        
        for k in water:
            embed.add_field(name='Daily Islam Fact', value=k.text_content().strip(), inline=False)
            
        await channel.send('@everyone', embed=embed)
            
            
    else:
        print("⚠️ERROR: Invalid Xpath ")
        
#This code is for the bot to start the loop of the scheduled message
@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.activity.Game(name="getting daily islam"))
    print(f"{bot.user.name} has connected to Discord!")
    scheduled_message.start()
            
        
        

    

bot.run("YOUR-BOT-TOKEN")
