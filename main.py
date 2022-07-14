# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import requests
import random
import os
from dotenv import main
from bs4 import BeautifulSoup
main.load_dotenv()
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

def getEuroRate():
    URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD"
    fake_id = random.randint(1000,9999)
    fake_id_string = str(fake_id)
    r = requests.get(URL,params={"id":fake_id_string, "availability":"available"})
  
    soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    table = soup.find('p', attrs = {'class':'result__BigRate-sc-1bsijpp-1 iGrAod'})
    txt = table.get_text()
    return txt

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "euro":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send(getEuroRate())

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(os.getenv("BOT_TOKEN"))
