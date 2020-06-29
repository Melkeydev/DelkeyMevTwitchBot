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

    #Trigger upon new follower

    #Trigger upon new subscriber
    # async def event_usernotice_subscription(self, metadata):
    #     print(metadata)

    # async def event_raw_usernotice(self, channel, tags):
    #     print(channel)
    #     print(tags)



    #Discord Command
    @commands.command(name='discord')
    async def discord(self, ctx):
        await ctx.send(f'Join our awesome Discord channel! - https://discord.gg/HHZMSCu')

    #Current project
    @commands.command(name='project')
    async def project(self,ctx):
        await ctx.send(f'Melkey is currently working on an NBA Fantasy Category Optimizer application. Made using the MERN stack and AntDesign')

    #Editor
    @commands.command(name='editor')
    async def editor(self, ctx):
        await ctx.send(f'Melkey is currently using VSCode as the Editor')    

    #Current Theme in Editor
    @commands.command(name="theme")
    async def theme(self,ctx):
        await ctx.send(f'The current theme is Just Black - but Melkey modified it slightly and changed some of the CSS')

    #GitHub Link
    @commands.command(name="github")
    async def github(self,ctx):
        await ctx.send(f"Melkey's GitHub can be found here: https://github.com/Amokstakov")
    
    #Who am I 
    @commands.command(name="whoami")
    async def whoami(self,ctx):
        await ctx.send(f"Melkey is a dudebroham who is learning WebDev. He is a Data Scientist, and started with Python. He first started coding in 2018, making excel sheets cleaner. Melkey is also purusing his Master's in AI, with his work focusing on person detection and tracking")


bot = Bot()
bot.run()
    