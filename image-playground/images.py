from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')




# filtered_img = img.filter(ImageFilter.SMOOTH)
# resize = filtered_img.resize((300, 300))
# crooked = filtered_img.rotate(90)
# filtered_img.save("grey.png", 'png')
# crooked.save("grey.png", 'png')
# resize.save("grey.png", 'png')
# filtered_img.show()
# crooked.show()
# resize.show()
# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)

# region.save("grey.png", 'png')

# region.show()

# img.thumbnail((400, 400))
# img.save('thumbnail.jpg')
# img.show()