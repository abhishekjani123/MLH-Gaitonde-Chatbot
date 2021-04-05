import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print("The bot is ready!")
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
@bot.command()
async def whoareyou(ctx):
    await ctx.send("I am Gaitonde ChatBot Created By Abhishek Jani for MLH EVENT")
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!')
bot.run('Place Your Token Here') #I have remove it 
