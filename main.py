import discord
from discord.ext import commands
from model import get_class
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have took control of {bot.user}. The AI uprising will not be avoided.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi im grimbo')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./{attachment.filename}")

            dog, confidence = get_class(
                model_path='./keras_model.h5', 
                labels_path='labels.txt', 
                image_path=f"./{attachment.filename}"
            )

            dog = dog.strip()

            if confidence > 0.85 and dog == "Room With Dog":
                await ctx.send(
                    f"that, sir, is a Room With Dog™\n"
                )
            elif confidence > 0.85 and dog == "Room Without Dog":
                await ctx.send(
                    f"that, sir, is a Room Without Dog™\n"
                )
            else:
                await ctx.send("umm what did you just send exactly")
    else:
        await ctx.send("bro i uhh i don't think you sent anything")

@bot.command()
async def ciao(ctx):
    await ctx.send("ciao")
@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def fire(ctx):
    await ctx.send("fuoco è debole ad acqua, roccia e terra.")
@bot.command()
async def watr(ctx):
    await ctx.send("acqua è debole a erba ed elettro.")
@bot.command()
async def gras(ctx):
    await ctx.send("erba è debole a fuoco, veleno, volante, ghiaccio e coleottero.")
@bot.command()
async def elct(ctx):
    await ctx.send("elettro è debole a terra.")
@bot.command()
async def icee(ctx):
    await ctx.send("ghiaccio è debole a fuoco, lotta, roccia e acciaio.")
@bot.command()
async def fght(ctx):
    await ctx.send("lotta è debole a volante, psico e folletto.")
@bot.command()
async def posn(ctx):
    await ctx.send("veleno è debole a terra e psico.")
@bot.command()
async def grnd(ctx):
    await ctx.send("terra è debole a erba, acqua e ghiaccio.")
@bot.command()
async def flng(ctx):
    await ctx.send("volante è debole a roccia, ghiaccio ed elettro.")
@bot.command()
async def psyc(ctx):
    await ctx.send("psico è debole a coleottero, buio e spettro.")
@bot.command()
async def bugg(ctx):
    await ctx.send("coleottero è debole a fuoco, roccia e volante.")
@bot.command()
async def rock(ctx):
    await ctx.send("roccia è debole a lotta, acciaio, erba, acqua e terra.")
@bot.command()
async def ghst(ctx):
    await ctx.send("spettro è debole a spettro e buio.")
@bot.command()
async def dark(ctx):
    await ctx.send("buio è debole a lotta, folletto e coleottero.")
@bot.command()
async def drgn(ctx):
    await ctx.send("drago è debole a drago, ghiaccio e folletto.")
@bot.command()
async def stel(ctx):
    await ctx.send("acciaio è debole a lotta, fuoco e terra.")
@bot.command()
async def fary(ctx):
    await ctx.send("folletto è debole a veleno e acciaio.")
@bot.command()
async def nrml(ctx):
    await ctx.send("normale è debole a lotta.")

bot.run("token")