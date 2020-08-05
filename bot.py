import os
import twitchio
#from selenium import webdriver
from twitchio.ext import commands


class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']])


    #start Bot
    async def event_ready(self):
        print(f'Ready | {self.nick}')


    #Triggers for particular events
    async def event_message(self,msg):
        # print(msg.author.name)
        ctx = await self.get_context(msg, cls=twitchio.Context)

        await self.handle_commands(msg, ctx=ctx)

        # if '' in ctx.content.casefold():
        #     await ctx.channel.send(f"Hi, @{ctx.author.name}!")




    #Discord Command
    @commands.command(name='discord')
    async def discord(self, ctx):
        await ctx.send(f'Join our awesome Discord channel! - https://discord.gg/HHZMSCu')

    #Current project
    @commands.command(name='project')
    async def project(self,ctx):
        await ctx.send(f'I am currently working on learning websockets, Type Script for the new app: Snackchat')

    #Editor
    @commands.command(name='editor')
    async def editor(self, ctx):
        await ctx.send(f'Melkey is currently using NVIM as the Editor')    

    #Current Theme in Editor
    @commands.command(name="theme")
    async def theme(self,ctx):
        await ctx.send(f'The current theme is something i forget')


    #GitHub Link
    @commands.command(name="github")
    async def github(self,ctx):
        await ctx.send(f"Melkey's GitHub can be found here: https://github.com/Amokstakov")


    #config
    @commands.command(name="config")
    async def github(self,ctx):
        await ctx.send(f"Melkey's config can be found here: https://github.com/Amokstakov/NvimConfig")
    
    #Who am I 
    @commands.command(name="whoami")
    async def whoami(self,ctx):
        await ctx.send(f"Melkey is a dudebroham who is learning WebDev. He is a Data Scientist, and started with Python. He first started coding in 2018, making excel sheets cleaner. Melkey is also purusing his Master's in AI, with his work focusing on person detection and tracking")

    #Shoutout Commands
    @commands.command(name="so")
    async def shoutout(self, ctx, username:str) -> None:
        print(ctx.author.badges)
        print(ctx.author.name)
        print(ctx.channel)
        if ctx.author.is_mod == 1:
            await ctx.send(f'A big warm shoutout to the this person right here - show them some LOVE and FOLLOW, https://www.twitch.tv/{username}')

bot = Bot()
bot.run()
    
