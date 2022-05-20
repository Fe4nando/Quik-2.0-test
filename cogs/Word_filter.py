import discord
from discord.ext import commands
import datetime 
from datetime import datetime
import assests.words
from assests.words import word

filtered_word=word
class filter(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.Cog.listener()
    async def on_message(self,ctx):
     for word in filtered_word:
        if word in ctx.content:
            await ctx.delete()
            timestamp=datetime.now()
            try:
              ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\messagelogs.txt','a', encoding='utf-8')
            except:
              ent=open(r'/workspace/logs/messagelogs.txt','a', encoding='utf-8')
            ent.write(f"Time:{timestamp} Swear:{ctx.content} Location:{ctx.channel.name} Author:{ctx.author.display_name} ID:{ctx.author.id} \n")
            ent.close()
     


async def setup(client):
     await client.add_cog(filter(client))













