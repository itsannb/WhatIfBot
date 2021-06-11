# Import discord package
import discord
from discord.ext import commands

# The bot
bot = commands.Bot(command_prefix='8! ')

# creates a function
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(827643671171039286)

    await general_channel.send('It is I') # await is needed to wait for the channel to be retrieved

# When the bot disconnects from the server
@bot.event
async def on_disconnet():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('FF')


# Run the bot on server
bot.run('token')
