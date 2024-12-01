import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} è diventato ecologico. (?????)")
@bot.command()
async def bottle(ctx):
    await ctx.send("step 1, prendi una bottiglia di plastica. step 2, tagliala a metà. step 3, prendi un po' di terriccio e dei semi. step 4, metti il terriccio e i semi nelle due parti della bottiglia. step 5, prenditi cura della pianta (tipo acqua sole cose del genere). congratulazioni, ora hai due vasi. (comunque comprati un depuratore)")
@bot.command()
async def fork(ctx):
    await ctx.send("boh comprale di metallo/carta lololol")
@bot.command()
async def plate(ctx):
    await ctx.send("facci due buchi e dipingici sotto. infila un nastro tra i due buchi. congratulazioni, ora hai una maschera. (ma comprali di ceramica perché hai così tante cose fatte di plastica)")
@bot.command()
async def sporb(ctx):
    await ctx.send("sporb sporb the animator sporb sporb the animator sporb sporb the animator sporb sporb the animator")

bot.run("token :)")
