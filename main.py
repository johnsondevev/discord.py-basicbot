import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is online')


@bot.event
async def on_message(message):
    if message.content  == "Hello".lower():
        await message.channel.send("Hey!")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f'{member.mention} Welcome To Galactic Development')

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f'{member.mention} Goodbye')

bot.run(YOUR BOT TOKEN)
#This command i recommend being at the bottom at all times as its a command that cannot be changed
