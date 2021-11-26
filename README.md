# Minecraft-Server-Launcher-Discord-Bot
A very simple bot that allows discord users to open your personal Minecraft server.

NOT SECURE! This is designed specifically for PERSONAL Minecraft and Discord servers.

To use this, it will take a little bit of setting up. In future I may make the data accessable from a JSON file to avoid the need to edit the source code so it can be an exe. Everything that may need to be edited can be found in the #Setup Code section. 

HOST = Your local address for your server
PORT = Your MC RCON Port
discordClientId = Your Discord client ID for your bot. You will need to go to to this address https://discord.com/developers/applications, and make a bot to use this program.
rconPassword = Your RCON password in your server propeties file. A password is required to connect to RCON.
fileName = The name of your .bat file that launches your server. The default value is "5gb.bat".

HOW TO RUN BOT:
1. Create a discord bot throuh https://discord.com/developers/applications and invite it to your Discord server. 

2. Set all values from above at the header of program. That is HOST, PORT, discordClientId, rconPassword and fileName. In a future version of this program, this will be accessabile through a JSON file.

3. Enable RCON to your Minecraft server in the server properties file. 

4. Place your modified launchServer.py file into the same directory as your Minecraft Server.

5. Open launchServer.py and use !mcHelp in your Discord server to see all commands.
