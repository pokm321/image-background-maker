from processors.processor import process_image
import os

original_directory = "C:/Users/pokm9/Desktop/Pics/test/"
processed_directory = "C:/Users/pokm9/Desktop/Pics/test/processed/"
ratio = 16 / 9
blur = 0.15

for file in os.listdir(original_directory):
  if os.path.isdir(original_directory + file):
    continue

  try:
    process_image(original_directory + file, processed_directory + file, ratio, blur)
  except:
    print("Error processing :", original_directory + file)

print("Done processing.")