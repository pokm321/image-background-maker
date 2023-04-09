from PIL import ImageFilter, ImageEnhance

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

    left_coor = int((new_width - width) / 2)
    top_coor = int((new_height - height) / 2)

    result_image.paste(original_image, (left_coor, top_coor))

    return result_image