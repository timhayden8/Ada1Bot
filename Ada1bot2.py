import discord
import requests
from bs4 import BeautifulSoup
def codescrape():
    page = requests.get("https://xurlocation.com/ada-1-mods-today-destiny-2/")
    soup = BeautifulSoup(page.content, 'html.parser')
    weapons = soup.find_all('ul')[2]
    weapons = weapons.text
    return weapons
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('!ada1'):
        weapons=codescrape()
        await message.channel.send(f'{weapons}')
client.run('<YOUR BOT TOKEN HERE>')
