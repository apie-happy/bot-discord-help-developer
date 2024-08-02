# SECTION library
from typing import List
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from csscompressor import compress as css_compress
from discord.utils import MISSING
from jsmin import jsmin
import requests
import ssl
import socket
import os
from config import DISCORD_TOKEN
# INTENTS
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)





# event laucnh bot
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # Synchroniser les commandes de slash globales
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")


# SECTION message



message_bot_end = f"```markedown\n - ʀᴀᴄᴏᴏɴ 🦝 ```" 

embed_template = discord.Embed(
    title="- ʀᴀᴄᴏᴏɴ 🦝",
    description="Bot create by",
    color=discord.Color.dark_red()  
)

embed_template.set_footer(text="@Apie")
embed_template.set_image(url="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTRxN3UweXA3aXdzcXlwa3RwZjdoNGljOTJmdDdha3I2cWNtYm13eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7CjEqtZUm2OBmJ9eha/giphy.gif")




# SECTION minifie
@bot.tree.command(name="minifie_js", description="Minifies a JS code")
async def minifie_js(interaction: discord.Interaction, code: str):
    js_minifie = jsmin(code)
    await interaction.response.send_message(f"JS minifié: ```js\n{js_minifie}\n```")



    

@bot.tree.command(name="minifie_css", description="Minifies a CSS code")
async def minifie_css(interaction: discord.Interaction, code: str):
    css_minifie = css_compress(code)
    await interaction.response.send_message(f"CSS minifié: ```css\n{css_minifie}``` {message_bot_end}")

# SECTION interaction
@bot.tree.command(name="hey", description="Say Hey!")
async def hey(interaction: discord.Interaction):
    await interaction.response.send_message(f"```Hey {interaction.user} !```{message_bot_end} ")

# ----------------
@bot.tree.command(name="server_info", description="Server info")
async def server_info(interaction: discord.Interaction):
    server = interaction.guild
    number_of_text_channels = len(server.text_channels)
    number_of_voice_channels = len(server.voice_channels)
    number_of_person = server.member_count
    server_name = server.name
    message = (f"The {server_name} server has {number_of_text_channels} text channels, "
               f"{number_of_voice_channels} voice channels and {number_of_person} members.")
    await interaction.response.send_message(f'{message} {message_bot_end}')

# -----------------

# Création de l'embed avec un lien dans la description
embed_credit = discord.Embed(
    title="Racoon developer",
    description="Bot create by [Tim](https://discord.com/users/1242587565907775549)",
    color=discord.Color.dark_red()  
)

embed_credit.set_author(name="Tim", url="https://github.com/apie-happy")
embed_credit.set_image(url="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTRxN3UweXA3aXdzcXlwa3RwZjdoNGljOTJmdDdha3I2cWNtYm13eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7CjEqtZUm2OBmJ9eha/giphy.gif")
embed_credit.set_footer(icon_url="https://i.pinimg.com/564x/4d/4e/68/4d4e68f0005e4bf67aead0778d690017.jpg", text="Tim")

embed_credit.add_field(
        name="Linkedin",
        value="[Tim](https://www.linkedin.com/in/tim-fromentin-339b03208/)",
        inline=False
    )
embed_credit.add_field(
        name="Github",
        value="[Apie](https://github.com/apie-happy)",
        inline=False
    )
embed_credit.add_field(
        name="Serveur",
        value="[Développeur Français](https://discord.gg/qVW48MZVtj)",
        inline=False
    )
embed_credit.add_field(
        name="Profile photo",
        value="[Raccoon Logo Vectors by Vecteezy](https://www.vecteezy.com/free-vector/raccoon-logo)",
        inline=False
    )


# Commande pour envoyer un message avec l'embed de crédit
@bot.tree.command(name="credit", description="Developer credit")
async def credit(interaction: discord.Interaction):
    await interaction.response.send_message(embed=embed_credit)





# @bot.tree.command(name="service")
# async def service(interaction: discord.Interaction, title: str, desc: str, price: str, titlefield1: str = None, valuefield1: str = None):
#     embed_service = discord.Embed(
#         title=f'> {title}',
#         description=desc,
#         color=discord.Color.dark_red()
#     )

#     embed_service.set_author(name="Tim", url="https://github.com/apie-happy")
#     embed_service.set_image(url="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTRxN3UweXA3aXdzcXlwa3RwZjdoNGljOTJmdDdha3I2cWNtYm13eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7CjEqtZUm2OBmJ9eha/giphy.gif")
#     embed_service.set_footer(icon_url="https://i.pinimg.com/564x/4d/4e/68/4d4e68f0005e4bf67aead0778d690017.jpg", text="Tim")

#     if titlefield1 and valuefield1:
#         embed_service.add_field(
#             name=titlefield1,
#             value=f'```{valuefield1}```',  # Utilisation des triples guillemets
#             inline=False,
#         )

#     embed_service.add_field(
#         name="Prix :",
#         value=price,
#         inline=False
#     )

#     await interaction.response.send_message(embed=embed_service)

    









# SECTION code
@bot.tree.command(name="doctype", description="Create an HTML doctype")
async def doctype(interaction: discord.Interaction):
    doctype_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>'''
    await interaction.response.send_message(f"```html\n{doctype_html}``` {message_bot_end}")


@bot.tree.command(name="lite_reset_css", description="Create a simple CSS reset")
async def lite_reset_css(interaction: discord.Interaction):
    reset = '''html{box-sizing:border-box}*,::after,::before{box-sizing:inherit}body{margin:0;padding:0}ol,ul{list-style:none}a{text-decoration:none;color:inherit'''
    await interaction.response.send_message(f"```css\n{reset}``` {message_bot_end}")

# FINISH

@bot.tree.command(name="example_skeleton_css", description="Create a simple web folder skeleton in CSS")
async def example_skeleton_css(interaction: discord.Interaction):
    skeleton = '''
├── public_html
├── assets
│   ├── img
│   ├── font
├── components
│   ├── footer.html
│   ├── navbar.html
├── functions
│   ├── db.php
│   ├── function.php
├── scripts
│   ├── include.js
│   ├── app.js
├── styles
│   └── global.css
├── .gitignore
├── pages
└── index.html'''
    await interaction.response.send_message(f"```markdown\n{skeleton}``` {message_bot_end}")

# FINISH

@bot.tree.command(name="example_skeleton_sass", description="Create a simple web folder skeleton in Sass")
async def example_skeleton_sass(interaction: discord.Interaction):
    skeleton = '''
├── public_html
├── assets
│   ├── img
│   ├── font
├── components
│   ├── footer.html
│   ├── navbar.html
├── functions
│   ├── db.php
│   ├── function.php
├── scripts
│   ├── include.js
│   ├── app.js
├── sass
│   ├── base
│   │   ├── _reset.scss
│   │   ├── _typography.scss
│   │   ├── index.scss
│   ├── components
│   │   ├── _button.scss
│   │   ├── _card.scss
│   │   ├── logo.scss
│   ├── layouts
│   │   ├── _footer.scss
│   │   ├── _navbar.scss
│   ├── themes
│       ├── _themes.scss
├── styles
│   └── global.css
├── .gitignore
├── package.json
├── pages
└── index.html'''
    await interaction.response.send_message(f"```markdown\n{skeleton}``` {message_bot_end}")







# SECTION list
# FINISH

@bot.tree.command(name="best_utils", description="List of the best tools (in my opinion) for web development")
async def utils_list(interaction: discord.Interaction):
    utils_list_message = """ #List of utils :
- Color palettes generator: <https://coolors.co>
- Compress image: <https://compressimage.io>
- Open source icons: <https://ionic.io/ionicons>
- Front-end exercises: <https://www.frontendmentor.io/home>
"""
    await interaction.response.send_message(utils_list_message)

# FINISH
@bot.tree.command(name="best_vscode_extension", description="List of the best VSCode extensions (in my opinion) for web development")
async def best_vscode_extension(interaction: discord.Interaction):
    list_extension =   """
# List :
- Command Anchors: Place anchor tags within comments for easy file and workspace navigation
- GitHub Pull Requests: Pull Request and Issue Provider for GitHub
- Live Server
- Project Templates: Create and apply custom project templates
- px to rem & rpx & vw (cssrem): Converts between px and rem & rpx & vw units in VSCode
"""
    await interaction.response.send_message(f'{list_extension} {message_bot_end}')

# SECTION website analyse
@bot.tree.command(name="request_command", description="f")
async def request_command(interaction: discord.Interaction, website: str):
    request = requests.get(website)
    request_status = request.status_code
    request_url = request.url
    request_request = request.request
    request_encoding = request.encoding
    await interaction.response.send_message(f'''Status: ```markedown\n{request_status}\n``` 
    Url: ```markedown\n{request_url}\n```
    Request: ```markedown\n{request_request}\n``` 
    Encoding: ```markedown\n{request_encoding}``` 
    {message_bot_end} ''')

# SECTION tuto
@bot.tree.command(name="tuto_code_send", description="d")
async def tuto_code_send(interaction: discord.Interaction):
    message = ("""to send code, put your code between backtick and add the language before the code.\n Example :\n \\```css 
    .box {
    background: #000;
    color: white;
}\\```
  Result : ```css
    .box {
    background: #000;
    color: white;
}``` """)
    await interaction.response.send_message(message + "\n" + message_bot_end)



# SECTION ---------- admin

# FINISH

def is_admin(ctx):
    return ctx.author.guild_permissions.administrator
# FINISH





@bot.command()
@commands.check(is_admin)
async def testAdmin(ctx):
    await ctx.send(f'Salut {ctx.author.mention}, vous êtes administrateur! {message_bot_end}')

# FINISH
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        message = """Your not admin
    """
        await ctx.send(f"```markedown\n{message}``` {message_bot_end}")




# FINISH
# @bot.command()
# @commands.check(is_admin)
# async def clear(ctx, limit: int = None):
#     await ctx.channel.purge(limit=limit)




# FIXME 
@bot.command()
@commands.check(is_admin)
async def new(ctx, *, arg):
    title_news = arg
    text_news = arg
    link_news = arg
    await ctx.send(f"{title_news}\n{text_news}\n{link_news}")




@bot.tree.command(name="commands", description="List of all slash commands")
async def list_commands(interaction: discord.Interaction):
    embed_command = discord.Embed(
        title="Liste des commandes",
        description="Voici une liste de toutes les commandes disponibles :",
        color=discord.Color.blue()
    )
    
    # Parcourir toutes les commandes enregistrées dans bot.tree
    for cmd in bot.tree.get_commands():
        embed_command.add_field(
            name=f"/{cmd.name}",
            value=cmd.description or "Pas de description disponible",
            inline=False
        )
    embed_command.add_field(
            name=f"/command_admin",
            value=cmd.description,
            inline=False
        )
    
    embed_command.set_footer(text="- ʀᴀᴄᴏᴏɴ 🦝")
    await interaction.response.send_message(embed=embed_command)


@bot.command(name="command_admin", description="List of all commands")
@commands.check(is_admin)
async def command_admin(ctx):
    embed = discord.Embed(
        title="Liste des commandes",
        description="Voici une liste de toutes les commandes disponibles:",
        color=discord.Color.blue()
    )
    
    # Parcourir toutes les commandes enregistrées
    for cmd in bot.commands:
        embed.add_field(
            name=cmd.name,
            value=cmd.description or "Pas de description disponible",
            inline=False
        )
    
    await ctx.send(embed=embed)
   

# SECTION ---------------------- test

# @bot.command()
# async def quijesuis(ctx):
#     author = ctx.author
#     authorName = author.name
#     message = f"Je suis {authorName}"
#     await ctx.send(message)


# ------------------------

# @bot.command(description="Command for compress css")
# async def compress(ctx, *, arg):
#     message = arg
#     # Remove multi-line comments (/* ... */)
#     messageNoComment = re.sub(r'/\*.*?\*/', '', message, flags=re.DOTALL)
#     # Compress spaces
#     messageNoLine = ' '.join(messageNoComment.split())
#     # messageNoSpace = messageNoLine.replace(" ", "")
#     await ctx.send(messageNoLine)
# ------------------------------

# @bot.command()
# async def cssCorrector(ctx, *, arg):
#     css = arg
#     lexer = CssLexer()
#     formatter = HtmlFormatter()
#     result = highlight(css, lexer, formatter)
#     print(result)


# ---------------
# @bot.tree.command(name="secure_website")
# async def secure_website(interaction: discord.Interaction, website: str):
#     def check_ssl(hostname):
#         try:
#             context = ssl.create_default_context()
#             with socket.create_connection((hostname, 443)) as sock:
#                 with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#                     ssock.do_handshake()
#                 return True
#         except ssl.SSLError:
#             return False
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             return False
    
#     secure = check_ssl(website)
    
#     if secure:
#         await interaction.response.send_message(f"{website} is secure (uses HTTPS). {message_bot_end}")
#     else:
#         await interaction.response.send_message(f"{website} is not secure (does not use HTTPS). {message_bot_end}")

# -----------------------------





# class languageDropDown(discord.ui.Select):
#     def __init__(self, code: str):
#         self.code = code
#         options = [
#             discord.SelectOption(label="HTML", description="html language"),
#             discord.SelectOption(label="CSS", description="css language")
#         ]
#         super().__init__(placeholder="Sélectionnez le format du langage", options=options, min_values=1, max_values=1)

#     async def callback(self, interaction: discord.Interaction):
#         selectLanguage = self.values[0]
#         if selectLanguage == "HTML":
#             # Utiliser des backticks pour le bloc de code et ajouter 'html' pour la coloration syntaxique
#             await interaction.response.send_message(f"```html\n{self.code}\n```")
#         elif selectLanguage == "CSS":
#             # Ajouter ici le traitement pour CSS si nécessaire
#             await interaction.response.send_message(f"```css\n{self.code}\n```")

# class languageView(discord.ui.View):
#     def __init__(self, code: str):
#         super().__init__()
#         self.add_item(languageDropDown(code))

# @bot.tree.command(name="language_formatage")
# async def language_formatage(interaction: discord.Interaction, code: str):
#     await interaction.response.send_message("Sélectionnez un langage :", view=languageView(code))



bot.run(DISCORD_TOKEN)


# photo
# <a href="https://www.vecteezy.com/free-vector/raccoon-logo">Raccoon Logo Vectors by Vecteezy</a>