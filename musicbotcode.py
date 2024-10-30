from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube import download_vid, remove_all_files
import asyncio
import discord
import os
import time



intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!",help_command=None,intents = intents)

@bot.event
async def on_ready():  
    try:

        print('Discord bot succesfully connected')
    except:
        print("[!] Couldn't connect, an Error occured")


@bot.command(name="help")
async def help_command(ctx):
    help_text = """
**Bot Commands:**

- **!join**: Connects the bot to the voice channel you're in.
- **!leave**: Disconnects the bot from the voice channel and removes downloaded files.
- **!play [title]**: Plays the specified song by title. Example: `!play Despacito`.
- **!pause**: Pauses the current playback.
- **!resume**: Resumes playback if paused.
- **!help**: Shows this list of commands.
    """
    await ctx.send(help_text)

@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Playback paused.")
    else:
        await ctx.send('[-] An error occured: You have to be in voice channel to use this commmand')

@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Playback resumed.")
    else:
        await ctx.send('[-] An error occured: You have to be in voice channel to use this commmand')

@bot.command()
async def leave(ctx): 
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Lefted the voice channel")
        time.sleep(1)
        remove_all_files("music")

    else:
        await ctx.send("[-] An Error occured: You have to be in a voice channel to run this command")

@bot.command()
async def join(context):
    if context.author.voice:
        channel = context.message.author.voice.channel
        try:

             await channel.connect()
        except:
            await context.send("[-] An error occured: Couldn't connect to the channel")

    else:
        await context.send("[-] An Error occured: You have to be in a voice channel to run this command")



@bot.command(name="play")
async def play(ctx, *, title):
    filename = download_vid(title)  # Descargamos el video y guardamos el nombre del archivo
    voice_channel = ctx.author.voice.channel

    if not ctx.voice_client:
        await voice_channel.connect()

    try:
        async with ctx.typing():
            player = discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\ffmpeg.exe", source=f"music/{filename}")
            ctx.voice_client.play(player, after=lambda e: after_playback(ctx, filename))
        await ctx.send(f'Now playing: {filename}')

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)

    except Exception as e:
        await ctx.send(f'Error: {e}')


def after_playback(ctx, filename):
    try:
        os.remove(f"music/{filename}")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("No discord token setted")
bot.run(token)
