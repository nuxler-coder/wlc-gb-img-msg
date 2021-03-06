# Welcome message code
@client.event
async def on_member_join(member):
  guild = client.get_guild(# paste your server's id here)
  channel = guild.get_channel(# paste your server's welcome channel's id here)
  text = "WELCOME"
  name = str(member)

  img = Image.open("cool-forest.jpg").convert("RGBA")
  pfp = member.avatar_url_as(size=256)
  data = BytesIO(await pfp.read())
  pfp = Image.open(data).convert("RGBA")

  draw = ImageDraw.Draw(img)
  pfp= circle(pfp, (385, 389))
  font = ImageFont.truetype("Redwing-Medium.otf", 78)
  font2 = ImageFont.truetype("Redwing-Medium.otf", 100)
  draw.text((500, 499), text, font=font)
  draw.text((430, 560), name, font=font2)
  img.paste(pfp, (435, 80), pfp)

  with BytesIO() as a:
    img.save(a, "PNG")
    a.seek(0)
    file = discord.File(a, "wlc.png")
  await channel.send(f"**Hey{member.mention}!**")
  wlcEmbed = discord.Embed(title="Welcome!", description=f"?? Welcome to **{guild.name}** {member.mention}!\n?? Now we have {guild.member_count} members!\nThanks for joining us!\n? Complete your verification in <#938678975667007499> to join the rest of this server.", color=discord.Color.blue())
  wlcEmbed.set_footer(text="Enjoy your time staying here!")
  wlcEmbed.set_image(url="attachment://wlc.png")
  await channel.send(file = file, embed = wlcEmbed)

# Goodbye message code
@client.event
async def on_member_remove(member):
  guild = client.get_guild(# paste your server's id here)
  channel = guild.get_channel(# paste your server's goodbye channel's id here)
  text = "GOODBYE"
  name = str(member)

  img = Image.open("cool-mountain.jpg").convert("RGBA")
  pfp = member.avatar_url_as(size=256)
  data = BytesIO(await pfp.read())
  pfp = Image.open(data).convert("RGBA")

  draw = ImageDraw.Draw(img)
  pfp= circle(pfp, (385, 385))
  font = ImageFont.truetype("Redwing-Medium.otf", 68)
  font2 = ImageFont.truetype("Redwing-Medium.otf", 100)
  draw.text((500, 499), text, font=font)
  draw.text((430, 560), name, font=font2)
  img.paste(pfp, (435, 80), pfp)

  with BytesIO() as a:
    img.save(a, "PNG")
    a.seek(0)
    file = discord.File(a, "gb.png")
    gbEmbed = discord.Embed(title=f"Someone left **{guild.name}**", description=f"{member.mention} has left this server!\nNow we have {guild.member_count} members!", color=discord.Color.blue())
    gbEmbed.set_image(url="attachment://gb.png")
    await channel.send(file = file, embed = gbEmbed)
