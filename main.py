# Import discord package
import discord
from discord.ext import commands

# The bot
bot = commands.Bot(command_prefix='8! ')

# when the bot starts
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(827643671171039286)

    await general_channel.send('Hello, I am What-If Bot. The absolute memey-est bot on the planet. write 8! help to get started')

# help
@bot.command(name = "helps")
async def help(context):
    myEmbed = discord.Embed(title = "List of Functions")
    myEmbed.add_field(name = "8! what if", value = "answers your what if question")
    myEmbed.add_field(name = "8! fun fact", value = "gives you a fun fact")
    myEmbed.add_field(name = "8! funny", value = "sends a funny picture")
    myEmbed.add_field(name = "8! version", value = "states the version")

    await context.message.channel.send(embed = myEmbed)

# When the bot disconnects from the server
@bot.event
async def on_disconnet():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('goodbye')


# Run the bot on server
bot.run('token')
