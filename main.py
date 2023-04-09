from processors.image_processor import process_image
from processors.gif_processor import process_gif
from PIL import Image
import shutil
import os

original_directory = "C:/Original/Path/"    # Directory containing images to convert
processed_directory = "C:/Processed/Path/"  # Directory to save converted images
ratio = 16 / 9                              # Aspect ratio of converted images
blur = 0.1                                  # Blur level of the background
contrast = 0.6                              # Contrast level of the background
skip_redundant = True                       # Whether to skip processing images that's already been converted

os.makedirs(processed_directory, exist_ok=True)

for file in os.listdir(original_directory):
  if os.path.isdir(original_directory + file) or file.endswith(".bat"):
    continue

  if skip_redundant and os.path.exists(processed_directory + file):
    continue

  try:
    with Image.open(original_directory + file) as input_image:
      if file.endswith(".gif"):
        shutil.copyfile(original_directory + file, processed_directory + file)
        #output_frames, output_duration = process_gif(input_image, ratio, blur, contrast)
        #output_frames[0].save(processed_directory + file, format='GIF', save_all=True, append_images=output_frames[1:], loop=0, duration=output_duration)
      else:
        output_image = process_image(input_image, ratio, blur, contrast)
        output_image.save(processed_directory + file)
  except Exception as e:
    print("Error processing :", original_directory + file)
    print(str(e))

print("Done processing.")