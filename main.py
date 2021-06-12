# Import discord package
import discord
from discord.ext import commands
import random

# The bot
bot = commands.Bot(command_prefix='8! ')

# when the bot starts
@bot.event
async def on_ready(): # async allows the function to run even though there is a delay
    general_channel = bot.get_channel(827643671171039286)

    await general_channel.send('Hello, I am What-If Bot. The absolute memey-est bot on the planet. write 8! help to get started')

# what if
@bot.command(name = "what_if")
async def what_if(context):
    r1 = random.randint(0,5)
    if r1 == 0:
        await context.message.channel.send("Good")
    elif r1 == 1:
        await context.message.channel.send("Bad")
    elif r1 == 2:
        await context.message.channel.send("Sad")
    elif r1 == 3:
        await context.message.channel.send("Trully tragic")
    elif r1 == 4:
        await context.message.channel.send("Best news ever")
    elif r1 == 5:
        await context.message.channel.send("Maybe this is all right")

# help
@bot.command(name = "helps")
async def help(context):
    myEmbed = discord.Embed(title = "List of Functions")
    myEmbed.add_field(name = "8! what if", value = "answers your what if question")
    myEmbed.add_field(name = "8! fun fact", value = "gives you a fun fact")
    myEmbed.add_field(name = "8! funny", value = "sends a funny picture")
    myEmbed.add_field(name = "8! version", value = "states the version")

    await context.message.channel.send(embed = myEmbed)

# version
@bot.command(name = 'version')
async def version(context):
    verEmbed = discord.Embed(title="Current Version:", color=0xA977F1)
    verEmbed.add_field(name="Version Code", value="v1.0.1", inline=False)
    verEmbed.add_field(name="Release Date", value="June 11, 2021", inline=False)
    verEmbed.set_author(name="What-If Bot")

    await context.message.channel.send(embed=verEmbed)

# When the bot disconnects from the server
@bot.event
async def on_disconnet():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('goodbye')


# Run the bot on server
bot.run('token')
