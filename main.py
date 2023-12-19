import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

def api(message):
    return # API call that would return a response from PineappleAi WIP

token = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        mentioned_message = message.clean_content.replace('@Pineapple Bot', '')
        print(mentioned_message)
    



bot.run(token)
