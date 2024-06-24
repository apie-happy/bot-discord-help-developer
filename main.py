import discord
from discord.ext import commands
# import re
from csscompressor import compress as css_compress
from jsmin import jsmin

intents = discord.Intents.all()
intents.messages = True  # Activer les intents pour les messages

bot = commands.Bot(command_prefix="/", intents=intents)


# @bot.command()
# async def cssCorrector(ctx, *, arg):
#     css = arg
#     lexer = CssLexer()
#     formatter = HtmlFormatter()
#     result = highlight(css, lexer, formatter)
#     print(result)

@bot.command()
async def minifieJS(ctx, *, arg):
     js = arg
     jsMinifie = jsmin(js)
     await ctx.send(f" JS minifie ```js\n{jsMinifie}\n```")

@bot.command()
async def hey(ctx):
    await ctx.send(f"Hey {ctx.author} !")

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def serverInfo(ctx):
    # on stock la props guild
    server = ctx.guild
    # on stock le nmbre de channel textuel
    numberOfTextChannels= len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur {serverName} compte {numberOfTextChannels} canaux textuels, {numberOfVoiceChannels} canaux vocaux et {numberOfPerson} membres."
    await ctx.send(message)

# @bot.command()
# async def quijesuis(ctx):
#     author = ctx.author
#     authorName = author.name
#     message = f"Je suis {authorName}"
#     await ctx.send(message)


# pas fini
# @bot.command(description="Command for compress css")
# async def compress(ctx, *, arg):
#     message = arg
#     # Remove multi-line comments (/* ... */)
#     messageNoComment = re.sub(r'/\*.*?\*/', '', message, flags=re.DOTALL)
#     # Compress spaces
#     messageNoLine = ' '.join(messageNoComment.split())
#     # messageNoSpace = messageNoLine.replace(" ", "")
#     await ctx.send(messageNoLine)

# compress 2
@bot.command()
async def minfieCSS(ctx, *, arg):
    css = arg
    compressed_css = css_compress(css)
    await ctx.send(f"Minifie CSS :\n```css\n{compressed_css}\n```")






@bot.command(description="Command for creating doctype")
async def doctype(ctx):
    doctypeHtml = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>'''
    await ctx.send(f"```html\n{doctypeHtml}\n```")

@bot.command()
async def liteResetCss(ctx):
     reset = '''html{box-sizing:border-box}*,::after,::before{box-sizing:inherit}body{margin:0;padding:0}ol,ul{list-style:none}a{text-decoration:none;color:inherit'''
     await ctx.send(f"```css\n{reset}\n```")

@bot.command()
async def exampleSqueleton(ctx):
     squeleton = '''
    ├── public_html
    │ ├── components
    │ └── footer.html
    │ └── navbar.html
    ├── functions
    │ └── db.php
    │ └── function.php
    ├── scripts
    │ └── include.js
    │ └── app.js
    ├── styles
    │ └──  global.css
    ├── .gitignore
    ├── index.html'''
     await ctx.send(f"```markedown\n{squeleton}\n```")

@bot.command()
async def utils_list(ctx):
    utils_list_message = """List utils :
    color palettes generator : <https://coolors.co>
    compress image : <https://compressimage.io>
    open source icons : <https://ionic.io/ionicons>
    exercice front-end : <https://www.frontendmentor.io/home>
    """
    await ctx.send(utils_list_message)




@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int = None):
        await ctx.channel.purge()

@bot.command()
async def credit(ctx):
     await ctx.send('Bot create by [Tim](https://github.com/apie-happy), Logo [Raccoon Logo Vectors by Vecteezy](https://www.vecteezy.com/free-vector/raccoon-logo)')




bot.run("MTI1MzAzNDAwNTY3OTQ0MDAxNA.Gfkpme.ZSu9gXxCVUdp5gzzr6L0QugKGO1UTH8NSR_d8A")


# photo
# <a href="https://www.vecteezy.com/free-vector/raccoon-logo">Raccoon Logo Vectors by Vecteezy</a>