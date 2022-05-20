import discord 
from discord.ext import commands
import datetime 
from datetime import datetime

class Logs(commands.Cog):
    def __init__(self,client):
        self.client=client
        
    @commands.Cog.listener()
    async def on_message_delete(self,message):
     timestamp=datetime.now()
     try:
      ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\messagelogs.txt','a', encoding='utf-8')
     except:
      ent=open(r'/workspace/logs/messagelogs.txt','a', encoding='utf-8')
     ent.write(f"Time:{timestamp} Message:{message.content} Location:{message.channel.name} Author:{message.author.display_name} ID:{message.author.id} \n")
     ent.close()
    
    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
     timestamp=datetime.now()
     try:
      ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\messagelogs.txt','a', encoding='utf-8')
     except:
      ent=open(r'/workspace/logs/messagelogs.txt','a', encoding='utf-8')
     ent.write(f"Time:{timestamp} Message was:{before.content} Message is:{after.content} Location:{before.channel.name} Author:{before.author.display_name} ID:{before.author.id} \n")
     ent.close()
    
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def view_logs(self,ctx):
     try:
       await ctx.send(file=discord.File(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\messagelogs.txt'))
       await ctx.send(file=discord.File(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt'))
     except:
       await ctx.send(file=discord.File(r'/workspace/logs/messagelogs.txt'))
       await ctx.send(file=discord.File(r'/workspace/logs/userologs.txt'))
      
      
    @commands.Cog.listener()
    async def on_member_join(self,member):
      timestamp=datetime.now()
      try:
       ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt','a', encoding='utf-8')
      except:
       ent=open(r'/workspace/logs/userologs.txt','a', encoding='utf-8')
      ent.write(f"On:{timestamp} {member.display_name} joined the Server. User Id:{member.id} \n")
      ent.close
       
    @commands.Cog.listener()
    async def on_member_leave(self,member):
      timestamp=datetime.now()
      try:
       ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt','a', encoding='utf-8')
      except:
       ent=open(r'/workspace/logs/userologs.txt','a', encoding='utf-8')
      ent.write(f"On:{timestamp} {member.display_name} left the Server. User Id:{member.id} \n")
      ent.close
      
      
    
async def setup(client):
     await client.add_cog(Logs(client))