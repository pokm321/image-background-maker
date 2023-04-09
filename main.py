from PIL import Image, ImageFilter

# Open the original image
image_name = "image.jpeg"
ratio = 16 / 9
blur = 0.15

original_image = Image.open(f"C:/Users/pokm9/Desktop/Pics/{image_name}")

width, height = original_image.size

if width / height < ratio :
    # Stretch horizontally
    new_width = int(height * ratio)
    new_height = height
else:
    # Stretch vertically
    new_width = width
    new_height = int(width / ratio)

stretched_image = original_image.resize((new_width, new_height))
blurred_image = stretched_image.filter(ImageFilter.GaussianBlur(radius=new_width*blur))

left_coor = int((new_width - width) / 2)
top_coor = int((new_height - height) / 2)

blurred_image.paste(original_image, (left_coor, top_coor))

# Save resulting image
blurred_image.save(f"C:/Users/pokm9/Desktop/Pics/processed/{image_name}")