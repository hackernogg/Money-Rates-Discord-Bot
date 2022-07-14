import discord
from discord.ext import commands
import json
import requests
import random
import os
from dotenv import main
from bs4 import BeautifulSoup
main.load_dotenv()

bot = commands.Bot(command_prefix='$')

f = open('currency-symbols.json')
cur_data = json.load(f)

def getEuroRate(cur1,cur2):
    URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From="+ cur1 +"&To="+ cur2
    fake_id = random.randint(1000,9999)
    fake_id_string = str(fake_id)
    r = requests.get(URL,params={"id":fake_id_string, "availability":"available"})
  
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = soup.find('p', attrs = {'class':'result__BigRate-sc-1bsijpp-1 iGrAod'})
    txt = table.get_text()
    return txt


@bot.event
async def on_ready():

	guild_count = 0


	for guild in bot.guilds:

		print(f"- {guild.id} (name: {guild.name})")


		guild_count = guild_count + 1


	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


#@bot.event
#async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	#if message.content == "euro":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		#await message.channel.send(getEuroRate())
@bot.command()
async def rate(ctx, cur1, cur2):
	exist1 = False
	exist2 = False
	for element in cur_data:
		if element["abbreviation"] == cur1:
			exist1 = True
		if element["abbreviation"] == cur2:
			exist2 = True
	if exist1 == True and exist2 == True :
		await ctx.send("1 "+cur1+"== "+getEuroRate(cur1,cur2))
	else:
		await ctx.send("Bruh, wrong form !!!")
@bot.command()
async def money(ctx):
	await ctx.send("Sample check rate : $rate USD CNY")
	await ctx.send("Official form : CNY USD EUR ARS INR HUF ...")


		

#print(cur_data[1]["abbreviation"])
bot.run(os.getenv("BOT_TOKEN"))
