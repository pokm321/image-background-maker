from processors.image_processor import process_image
from processors.gif_processor import process_gif
from PIL import Image
import shutil
import os

base_dir = "C:/Base/Dir/"                   # Directory containing images to convert
processed = "Processed/"                    # Directory (inside the base_dir) to save converted images
ratio = 16 / 9                              # Aspect ratio of converted images
skip_redundant = True                       # Whether to skip processing images that have already been converted

blur = 0.15                                 # Blur level of the background
contrast = 0.6                              # Contrast level of the background


processed_dir = base_dir + processed
temp_dir = base_dir + "temp/"
os.makedirs(processed_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

count_processed, count_skip, count_error = 0, 0, 0

for file in os.listdir(base_dir):
  if os.path.isdir(base_dir + file) or file.endswith(".bat"):
    continue

  if skip_redundant and os.path.exists(processed_dir + file):
    shutil.move(processed_dir + file, temp_dir + file)
    count_skip += 1
    continue

  try:
    with Image.open(base_dir + file) as input_image:
      if file.endswith(".gif"):
        shutil.copyfile(base_dir + file, temp_dir + file)
        #output_frames, output_duration = process_gif(input_image, ratio, blur, contrast)
        #output_frames[0].save(processed_directory + file, format='GIF', save_all=True, append_images=output_frames[1:], loop=0, duration=output_duration)
      else:
        output_image = process_image(input_image, ratio, blur, contrast)
        output_image.save(temp_dir + file)
      count_processed += 1
  except Exception as e:
    print("Error processing :", base_dir + file)
    print(str(e))
    count_error += 1

count_deleted = len(os.listdir(processed_dir))
shutil.rmtree(processed_dir)
os.rename(temp_dir, processed_dir)

count_total = count_processed + count_skip + count_error
print(f"Done processing!\n...Processed : {count_processed} \n...Skipped   : {count_skip}\n...Errors    : {count_error} \n...Total     : {count_total}")
if (count_deleted):
  print(f"\n{count_deleted} files got deleted because they no longer exist in the base directory.")