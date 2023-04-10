from PIL import ImageFilter, ImageEnhance
from statistics import mean

def process_image(original_image, ratio, blur, contrast):
    if original_image.mode != "RGB":
        original_image = original_image.convert("RGB")
    
    width, height = original_image.size

    if width / height < ratio :
        # Stretch horizontally
        new_width = int(height * ratio)
        new_height = height
    else:
        # Stretch vertically
        new_width = width
        new_height = int(width / ratio)

    result_image = original_image.resize((new_width, new_height))\
                .filter(ImageFilter.GaussianBlur(radius=new_width*blur))
    
    result_image = ImageEnhance.Contrast(result_image).enhance(contrast)

    # auto-adjust the saturation of the background
    saturation_original = mean(list(original_image.convert("HSV").getdata(1)))
    saturation = (1 + (1 - saturation_original / 100) / 2)
    result_image = ImageEnhance.Color(result_image).enhance(saturation)

    # auto-adjust the brightness of the background
    brightness_original = mean(list(original_image.convert("L").getdata()))
    if brightness_original < 100:
        brightness = (1 + (1 - brightness_original / 100) / 2)
        result_image = ImageEnhance.Brightness(result_image).enhance(brightness)

    left_coor = int((new_width - width) / 2)
    top_coor = int((new_height - height) / 2)

    result_image.paste(original_image, (left_coor, top_coor))

    return result_image