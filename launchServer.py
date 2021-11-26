import discord
import re
import os
import time
import signal
import subprocess
from subprocess import Popen
from discord.ext import commands
from mctools import RCONClient
from mctools import QUERYClient
import sys

# Setup Code
pid = ""
serverOpen = False	
HOST = "127.0.0.1" #Local address
PORT = 25575
query = QUERYClient(HOST)
rcon = RCONClient(HOST, port = PORT)
count = 0
discordClientId = ""
rconPassword = ''
fileName = "5gb.bat"

bot = commands.Bot(command_prefix='!')

def checkServerOpen():
	try:
		response = rcon.command("thiscommanddoesntmatter")
		return True
	except:
		return False

#Server Opener
@bot.command()
async def mcRun(ctx):
	global pid # Local boolean for window id
	global count # Count of how many times the server has been opened

	if checkServerOpen() == True: # Prevents multiple instances of server
		await ctx.send('The server is already open {0.author.mention}.'.format(ctx))
	elif checkServerOpen() == False:
		await ctx.send('Server launching...')
		try:
			# Opens server .bat
			os.startfile(fileName) # Filename of server bat/jar
			
			# Waits for estimated boot time of server before sending message
			time.sleep(35) 
			await ctx.send('The server *should* be up {0.author.mention}. If it isn\'t up in the next 30 seconds, annoy Tom.'.format(ctx))
			
			# ID of window
			pid = str(os.getpid())
			print("ID = "+pid)

			# McTools Authenticator
			auth = rcon.is_authenticated()
			while auth != True: # Ensures prosess makes it through queue
				try:
					rcon.login('tomsmellsbad')
					auth = rcon.is_authenticated()
				except Exception as x:
					print(x)
		except Exception as e:
			await ctx.send('Something fucked up. Tom can\'t code.')
			print(e)
		count = count + 1	

#Server Closer
@bot.command()
async def mcClose(ctx):
	if checkServerOpen() == True:
		await ctx.send('Server closing...')

		# Sends warning to server with 15 second buffer before issuing stop command
		rcon.command("say Server closing in 15 seconds...")
		time.sleep(10)
		rcon.command("say 5")
		time.sleep(1)
		rcon.command("say 4")
		time.sleep(1)
		rcon.command("say 3")
		time.sleep(1)
		rcon.command("say 2")
		time.sleep(1)
		rcon.command("say 1")
		time.sleep(1)

		try:
			rcon.command("stop") # Issues stop command to server
			time.sleep(10)
			rcon.stop() # Closes RCON connection
			await ctx.send('Server is closed.')
		except Exception as e:
			await ctx.send('Something went wrong, annoy Tom if it looks like it\'s something major.')
			print(e)

	elif checkServerOpen() == False:
		await ctx.send('Server is already closed.')

#Server Stats
@bot.command()
async def mcStatus(ctx):
	if checkServerOpen() == True: 
		try:
			stats = query.get_full_stats() # Dictionary
			await ctx.send('The server is online with {0} players logged in!'.format(stats["numplayers"]))
		except Exception as e:
			await ctx.send('Status are not currently available.')
			print (e)

	elif checkServerOpen()	== False: 
		await ctx.send('The server is currently not open.')

#Rain Toggle
@bot.command()
async def mcRain(ctx):
	if checkServerOpen() == True:
		rcon.command("weather clear") # Issues /weather clear command to server
		rcon.command("say The rain has been cleared by a Discord user.") # Issues say command to server
		await ctx.send('The rain has been cleared.')
	elif checkServerOpen()	== False:
		await ctx.send('The server is currently not open.')

#Debug RCON Connect
@bot.command()
async def mcRCON(ctx):
	auth = rcon.is_authenticated()
	if auth != True:
		try:	
			rcon.login(rconPassword)
		except Exception as e:
			print(e)
			await ctx.send('Failed to connect to RCON.')
	else:
		await ctx.send('RCON is already connected and authenticated.')

# Help
@bot.command()
async def mcHelp(ctx):
	await ctx.send('Welcome to the Minecraft Server Launcher Discord Bot!\n```Currently Loaded Server: Winter 2021 (5gb)``````!mcRun - Opens the Minecraft server.\n!mcClose - Closes the Minecraft server.\n!mcStatus - Displays server stats.\n!mcRain - Sets in-game weather to "clear".```')

bot.run(discordClientId) # Put Discord client ID here to run bot
