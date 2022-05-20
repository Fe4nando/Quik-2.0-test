import discord
import asyncio
import os
from discord.ext import commands
from assests.config import *
from discord.ui import Button,View

intents = discord.Intents.all()
discord.member = True
client=commands.Bot (command_prefix=commands.when_mentioned_or('!'),intents = intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('!report '))
    print('Quirk Is Online')
    absolute_path = os.path.abspath(__file__)
    print("Full path: " + absolute_path)
    print("Directory Path: " + os.path.dirname(absolute_path))
    
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Please use a vaild Command available. Use the command !help for more info")

@client.command()       
async def report(ctx):
        member=ctx.author
        try:
            button=Button(label="Continue",style=discord.ButtonStyle.green)
            view=View()
            view.add_item(button)
            await ctx.message.add_reaction("✅")
            await member.send("click on continue to start",view=view)
            async def button_callback(interaction):
                button=Button(label="YES",style=discord.ButtonStyle.green)
                button1=Button(label="NO",style=discord.ButtonStyle.red)
                embed=discord.Embed(title="Report",description="For Report the user you must provide the follwing information")
                embed.add_field(name="Information Needed",value="Type of Report:\n[Type here]\nDescription of Report\n[Type here]\nThe name of the user:\n[Type Here]\nScreenshot and evidence\n[Please provide as link]")
                embed.set_footer(text="By clicking on Yes,you can start typing your report in the format given above.Please note the message needs to be sent as one.")
                view=View()
                view.add_item(button)
                view.add_item(button1)
                async def button_callback(interaction):
                    embed=discord.Embed(title="Report",description="For Report the user you must provide the follwing information")
                    embed.add_field(name="Information Needed",value="Type of Report:\n[Type here]\nDescription of Report\n[Type here]\nThe name of the user:\n[Type Here]\nScreenshot and evidence\n[Please provide as link]")
                    embed.set_footer(text="By clicking on Yes,you can start typing your report in the format given above.Please note the message needs to be sent as one.")
                    await interaction.response.send_message(embed=embed)
                    channel=client.get_channel(962389878748880926)
                    def check(m):
                      return m.author.id==ctx.author.id
                    message=await client.wait_for("message",check=check)
                    await message.add_reaction("<:Bruh:905404779860209699>")
                    report=discord.Embed(title="New Report",description=f"This Report was sent by {ctx.author.display_name}")
                    report.add_field(name="The Report",value=f"{message.content}")
                    await channel.send(embed=report)
                button.callback=button_callback
                async def button1_callback(interaction):
                    embed=discord.Embed(title="Rejected Report Request!")
                    view=View()
                    await interaction.response.edit_message(embed=embed,view=view)
                button1.callback=button1_callback
                await interaction.response.send_message(embed=embed,view=view)
            button.callback=button_callback
            
        except:
            embed=discord.Embed()
            embed.set_image(url="https://media.discordapp.net/attachments/966210256847900693/966212516512411698/unknown.png")
            await ctx.send("You have Disabled allow user dm in privacy settings",embed=embed)
            await ctx.message.add_reaction("❌")
            await ctx.message.remove_reaction("✅")

@commands.has_permissions(manage_messages=True)
@client.command(aliases=["purge"])
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def load_extensions(ctx,extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload_extensions(ctx,extension):
    client.unload_extension(f"cogs.{extension}")
    
async def load_extensions():
 for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        await client.load_extension(f'cogs.{filename[:-3]}')
    
async def main():
    async with client:
        await load_extensions()
        await client.start(token)

asyncio.run(main())
        
