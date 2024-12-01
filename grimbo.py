import discord
import random, os
import requests
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'È apparso un {bot.user} selvatico!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_pokemon_info(pokemon_name):
    '''Funzione per ottenere informazioni sul Pokémon dalla PokeAPI'''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    res = requests.get(url)

    data = res.json()
    return {
        'name': data['name'].capitalize(),
        'id': data['id'],
        'types': [t['type']['name'] for t in data['types']],
        'weight': data['weight'] / 10,  # Peso in kg
        'sprite': data['sprites']['front_default']
    }
@bot.command()
async def help(ctx):
    await ctx.send("help, pokemon (insert name here), duck, meme, ciao, pasw, fire, watr, gras, elect, icee, fght, posn, grnd, flng, psyc, bugg, rock, ghst, dark, drgn, stel, fary, nrml")
@bot.command('pokemon')
async def pokemon(ctx, pokemon_name: str):
    '''Risponde con informazioni sul Pokémon specificato'''
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        embed = discord.Embed(title=f"{pokemon_info['name']} (ID: {pokemon_info['id']})", color=0x1ABC9C)
        embed.set_thumbnail(url=pokemon_info['sprite'])
        embed.add_field(name='Tipo', value=', '.join(pokemon_info['types']), inline=True)
        embed.add_field(name='Peso', value=f"{pokemon_info['weight']} kg", inline=True)

        await ctx.send(embed=embed)
    else:
        await ctx.send(f"non conosco nessun pokemon chiamato `{pokemon_name}`. hai visto troppi ripoff.")
@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
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
bot.run("token :)")
