# Documentation can be found at https://nighty.one/docs/#customscripts #
@bot.command()
async def ipgrab(nighty, grabLink, videoName="memes that caught me off guard", videoAuthor="Memecorp", thumbnail="https://images-ext-1.discordapp.net/external/CvV7ySZWFWrvYOrZLTs6Pv3yTdPgxxRVIFps-yoxV4k/https/i.ytimg.com/vi/iE-m--mhuG4/maxresdefault.jpg"):  # NAME OF THE COMMAND: ipgrab
    await nighty.message.delete() #Delete Commands sent and executes function
    embed = discord.Embed(
    description="YouTube", 
    color=0xFF0000
    )
    embed.add_field(
        name=videoAuthor, 
        value=f"["+ videoName+ "]("+ grabLink +")", 
        inline=False
        )
    embed.set_image(url=thumbnail)
    await nighty.send( embed=embed)