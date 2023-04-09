from processors.image_processor import process_image
from processors.gif_processor import process_gif
from PIL import Image
import os

original_directory = "C:/Users/pokm9/Desktop/Pics/test/"
processed_directory = "C:/Users/pokm9/Desktop/Pics/test/processed/"
ratio = 16 / 9
blur = 0.15

os.makedirs(processed_directory, exist_ok=True)

for file in os.listdir(original_directory):
  if os.path.isdir(original_directory + file):
    continue

  try:
    with Image.open(original_directory + file) as input_image:
      if file.endswith("gif"):
        output_frames, output_duration = process_gif(input_image, ratio, blur)
        output_frames[0].save(processed_directory + file, format='GIF', save_all=True, append_images=output_frames[1:], loop=0, duration=output_duration)
      else:
        output_image = process_image(input_image, ratio, blur)
        output_image.save(processed_directory + file)
  except Exception as e:
    print("Error processing :", original_directory + file)
    print(str(e))

print("Done processing.")