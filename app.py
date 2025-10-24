import discord
from discord.ext import commands
import os

# Carga el token del bot desde las variables del entorno de Server.pro
TOKEN = os.getenv("TOKEN")

# Puedes cambiar el prefijo de comandos si quieres (por ejemplo: ! o ?)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Evento al iniciar el bot
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Evento cuando alguien entra al servidor
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"👋 ¡Bienvenido/a {member.mention} al servidor!")

# Evento cuando alguien se va del servidor
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"👋 {member.name} ha salido del servidor.")

# Comando simple de prueba
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Inicia el bot
if TOKEN is None:
    print("❌ No se encontró el token del bot. Asegúrate de configurarlo en las variables de entorno.")
else:
    bot.run(TOKEN)
