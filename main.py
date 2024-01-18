import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import gemini
import asyncio

load_dotenv()

def troll():
    return "<@1025941981211414608> is kinda g@y"

token = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        mentioned_message = message.clean_content.replace('@Pineapple Bot', '')
        async with message.channel.typing():
            answer = gemini.getresponse(mentioned_message)
            #answer = troll()
            if not answer:  # check if answer is not empty
                answer = "I'm sorry, I couldn't generate a response."
        await asyncio.sleep(1)
        await message.channel.send(answer, reference=message)



bot.run(token)
