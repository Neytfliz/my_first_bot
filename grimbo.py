import discord

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)
from bot_logic import gen_pass

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("ciao")
    elif message.content.startswith('$civediamo'):
        await message.channel.send("ciao ci vediamo")
    elif message.content.startswith("$password"):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith("$fuoco"):
        await message.channel.send("fuoco è debole ad acqua, roccia e terra.")
    elif message.content.startswith("$acqua"):
        await message.channel.send("acqua è debole a erba ed elettro.")
    elif message.content.startswith("$erba"):
        await message.channel.send("erba è debole a fuoco, veleno, volante, ghiaccio e coleotero.")
    elif message.content.startswith("$elettro"):
        await message.channel.send("elettro è debole a terra.")
    elif message.content.startswith("$ghiaccio"):
        await message.channel.send("ghiaccio è debole a fuoco, lotta, roccia e acciaio.")
    elif message.content.startswith("$lotta"):
        await message.channel.send("lotta è debole a volante, psico e folletto.")
    elif message.content.startswith("$veleno"):
        await message.channel.send("veleno è debole a psico e terra.")
    elif message.content.startswith("$terra"):
        await message.channel.send("terra è debole ad acqua, erba e ghiaccio.")
    elif message.content.startswith("$volante"):
        await message.channel.send("volante è debole a elettro, ghiaccio e roccia.")
    elif message.content.startswith("$psico"):
        await message.channel.send("psico è debole a coleottero, buio e spettro.")
    elif message.content.startswith("$coleottero"):
        await message.channel.send("coleottero è debole a fuoco, roccia e volante.")
    elif message.content.startswith("$roccia"):
        await message.channel.send("roccia è debole a lotta, acciaio, erba, acqua e terra.")
    elif message.content.startswith("$spettro"):
        await message.channel.send("spettro è debole a spettro e buio.")
    elif message.content.startswith("$buio"):
        await message.channel.send("buio è debole a lotta, folletto e coleottero.")
    elif message.content.startswith("$drago"):
        await message.channel.send("drago è debole a drago, ghiaccio e folletto.")
    elif message.content.startswith("$acciaio"):
        await message.channel.send("acciaio è debole a lotta, fuoco e terra.")
    elif message.content.startswith("$folletto"):
        await message.channel.send("folletto è debole a veleno e acciaio.")
    elif message.content.startswith("$normale"):
        await message.channel.send("normale è debole a terra.")


client.run("insert_token")
