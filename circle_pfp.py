# This function makes a member's avatar circle. So this function is needed to be defined in order to create circle avatars.
def circle(pfp, size=(215, 215)):
  pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

  bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
  mask = Image.new("L", bigsize, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0, 0) + bigsize, fill=255)
  mask = mask.resize(pfp.size, Image.ANTIALIAS)
  mask = ImageChops.darker(mask, pfp.split()[-1])
  pfp.putalpha(mask)
  return pfp