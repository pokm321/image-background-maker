from PIL import Image, ImageSequence
from processors.image_processor import process_image

def process_gif(frames, ratio, blur, contrast):
    processed_frames = []
    for frame in ImageSequence.Iterator(frames):
      frame = frame.quantize()
      processed_frame = process_image(frame, ratio, blur, contrast)
      processed_frames.append(processed_frame)
      
    duration = frames.info['duration']

    return processed_frames, duration