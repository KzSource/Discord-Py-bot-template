import discord                                   #installing discord module.
from discord.ext import commands

TOKEN = "your bot token"

bot = commands.Bot(command_prefix="/")            #your command prefix

@bot.command()
async def say(ctx, word):                         #the name of the function is also the name of the command the second parameter
  await ctx.send(word)                            #of the function is from the message for example:/say hello! the bot will respond "hello"

@bot.command(name="your command name")            #Creating a command, change the name to wathever you want ^^.
async def example_function(ctx):                  #call the function if you want.
  return

bot.run(TOKEN)                                    #Run the bot with the TOKEN function.
