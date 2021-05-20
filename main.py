import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import networking

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
    print('MemeBot is online...')

@bot.command(name="meme", help="gives you a random meme from redit!")
async def meme(ctx):

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=' redit'
        ),
        status=discord.Status.online
    )

    embed = discord.Embed(
        description=f'Enjoy the meme {ctx.author.display_name}!',
        color=discord.Color.blurple()
    )

    embed.set_author(
        name='Redit Meme',
        icon_url=ctx.author.avatar_url
    )

    x = networking.Meme().getMeme()
    embed.set_image(url=x)

    print('bot is alive')

    await ctx.send(embed=embed)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=' my fav youtuber KSI!'
        ),
        status=discord.Status.idle
    )

bot.run(TOKEN)

