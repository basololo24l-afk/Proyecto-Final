import discord
import random
from discord.ext import commands
import os, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Ha iniciado sesión como {bot.user}')

'''
# ---- COMANDO MEME LOCAL ----
@bot.command()
async def mem(ctx):
    imagen = random.choice(os.listdir('images'))
    with open(f'images/{imagen}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
'''

# ---- MENÚ DE INFORMACIÓN ----
@bot.command()
async def informacion(ctx):
    menu = (
        "📘 Opciones de información:\n"
        "1 Info sobre tala de árboles 🌳🌲🌱🌿\n"
        "2️ Info sobre el mar 🌊💧\n"
        "3️ Info sobre contaminación 🏭⛽🛩️🚗\n"
        "4 info sobre el clima ☀️⛈️🌤️🌨️🌧️\n"
        "5 info sobre Metales pesados: Mercurio, Plomo, Cadmio, Arsénico, Cromo 🔩\n"
        "6 info sobre la contaminacion de la energia ⚡🔋\n"
        "7 info sobre la contaminacion de residuos solidos 🚮\n"
        "8 info de la onu sobre el clima \n"
        "9 info de la Nasa sobre el clima \n"
        "10 info de la IPCC sobre el clima \n"
        "11 info de worldweather sobre el clima \n"
        "12 info de NOAA sobre el clima \n"
        "13 info de la AEMET sobre el clima \n"
        "14 informacion extra"
        "👉 Responde con el número de la opción /n"
    )
    await ctx.send(menu)

# ---- RESPUESTA SEGÚN OPCIÓN ----
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "1":
        await message.channel.send("🌳 La tala indiscriminada de árboles contribuye a la pérdida de biodiversidad y al cambio climático.")     

    if message.content == "2":
        await message.channel.send("🚿 El consumo del agua innecesaria afecta al mundo por que sin el agua no pueden crecer los arboles.")

    if message.content == "3":
        await message.channel.send("🚬 La contaminación es la presencia de sustancias o energía en el ambiente que dañan la salud de los seres vivos y el equilibrio de los ecosistemas. Puede ocurrir en el aire, agua o suelo, y normalmente es causada por actividades humanas. 🌍⚠️ .")    

    if message.content == "4":
        await message.channel.send("⛅🌦️ El clima es de  los mas importante en nuestro mundo ya que sin el ni siquiera existiriamos .")

    if message.content == "5":
        await message.channel.send("🔩 Son muy peligrosos porque permanecen mucho tiempo en el ambiente Mercurio Plomo Cadmio Arsénico Cromo Estos pueden entrar al agua o a los alimentos y causar enfermedades.  .")    
    
    if message.content == "6":
        await message.channel.send("⚡ No siempre son sustancias; también puede ser energía. Ruido excesivo (contaminación sonora) Luz artificial excesiva (contaminación lumínica) Radiación .")
  
    if message.content == "7":
        await message.channel.send("🚮 La basura mal manejada contamina el suelo, el agua y el aire. Plásticos Microplásticos Vidrio Latas Residuos electrónicos Pilas y baterías Neumáticos .")
  
    if message.content == "8":
        await message.channel.send("https://www.un.org/es/")

    if message.content == "9":
        await message.channel.send("https://www.nasa.gov/")

    if message.content == "10":
        await message.channel.send("https://www.ipcc.ch/")

    if message.content == "11":
        await message.channel.send("https://worldweather.wmo.int")

    if message.content == "12":
        await message.channel.send("https://www.noaa.gov/")

    if message.content == "13":
        await message.channel.send("https://www.aemet.es/es/portada")

    if message.content == "14":
        await message.channel.send("No contamines porque si contaminas todo lo que haras sera expandir el efecto invernadero lo que provocara sera que o se extinga la vida o que el mundo termine en las peores condiciones")

    # 👇 Esto asegura que los comandos ($mem, $climate_change, etc.) sigan funcionando
    await bot.process_commands(message)

bot.run("")
