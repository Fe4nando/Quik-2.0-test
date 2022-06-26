
import discord 
from discord.ext import commands 
from discord.ui import Button,View
import datetime 
from datetime import datetime

class Admin(commands.Cog):
    def __init__(self,client):
         self.client=client
    
    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def warn(self,ctx,member:discord.Member,*,reason):
            await ctx.send('The User has been warned!')
            timestamp=datetime.now()
            warn=ctx.guild.get_role(852770025521807400)
            await member.add_roles(warn)
            try:
             ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt','a', encoding='utf-8')
            except:
             ent=open(r'/workspace/logs/userologs.txt','a', encoding='utf-8')
            ent.write(f"On:{timestamp} {member.display_name} has been warned.With the reason of:{reason} \n")
            ent.close
            
    @commands.has_permissions(kick_members=True)
    @commands.command(pass_conext=True)
    async def kick(self,ctx,member:discord.Member,*,reason):
            await member.kick(reason=reason)
            await ctx.send("The User has been Kicked")
            timestamp=datetime.now()
            try:
             ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt','a', encoding='utf-8')
            except:
             ent=open(r'/workspace/logs/userologs.txt','a', encoding='utf-8')
            ent.write(f"On:{timestamp} {member.display_name} Was Kicked!.With the reason of:{reason} \n")
            ent.close
            
    @commands.has_permissions(kick_members=True)
    @commands.command(pass_conext=True)
    async def ban(self,ctx,member:discord.Member,*,reason):
            try:
             embed=discord.Embed(title="Ban",
                                description="It looks like you have been banned from the server!\n You can request for a unban appeal by click the button below.")
             button=Button(label="Request Appeal",url="https://docs.google.com/forms/d/e/1FAIpQLSdvYvZGKhi4VDoiKs6lleraftf-ke4Yxh_SGe5vBRsdGUIEbg/viewform?usp=sf_link")
             view=View()
             view.add_item(button)
             await member.send(embed=embed,view=view)
            except:
              await ctx.send("Cannot Message User! They cant request for a ban appeal")
            await member.ban(reason=reason)
            await ctx.send("The User has been Banned")
            timestamp=datetime.now()
            try:
             ent=open(r'C:\Users\LENOVO\OneDrive\Documents\Desktop\Python Bot\PIE\Quik-2.0-test\logs\userologs.txt','a', encoding='utf-8')
            except:
             ent=open(r'/workspace/logs/userologs.txt','a', encoding='utf-8')
            ent.write(f"On:{timestamp} {member.display_name} Was Banned!.With the reason of:{reason} \n")
            ent.close
        
        
async def setup(client):
     await client.add_cog(Admin(client))