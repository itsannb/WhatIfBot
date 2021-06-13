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

# help
@bot.command(name = 'help')
async def help(context):
    myEmbed = discord.Embed(title = "List of Functions")
    myEmbed.add_field(name = "what if ...", value = "answers your what if question", inline=False)
    myEmbed.add_field(name = "8! joke", value = "gives a funny dad joke", inline=False)
    myEmbed.add_field(name = "8! version", value = "states the version", inline=False)

    await context.message.channel.send(embed = myEmbed)

# version
@bot.command(name = 'version')
async def version(context):
    verEmbed = discord.Embed(title = "Current Version:", color = 0xA977F1)
    verEmbed.add_field(name = "Version Code", value = "v1.0.2", inline = False)
    verEmbed.add_field(name = "Release Date", value = "June 12, 2021", inline = False)
    verEmbed.set_author(name = "What-If Bot")
    verEmbed.set_footer(name = "Ann B and Huy M")

    await context.message.channel.send(embed = verEmbed)

# jokes
@bot.command(name = 'joke')
async def joke(context):
    
    file = open('dadjokes.txt')
    content = file.readlines()
    r2 = random.randint(0,len(content))

    await context.message.channel.send(content[r2])

# what if
@bot.event
async def on_message(message):
    if "what if" in message.content:
        file = open('what-ifs.txt')
        content = file.readlines()
        r1 = random.randint(0,len(content))

        await message.channel.send(content[r1])

    await bot.process_commands(message)

# When the bot disconnects from the server
@bot.event
async def on_disconnect():
    general_channel = bot.get_channel(827643671171039286)
    await general_channel.send('goodbye')


# Run the bot on server
bot.run('token')
