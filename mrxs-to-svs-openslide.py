import argparse
import openslide
from PIL import Image

def convert_mrxs_to_tiff(input_path, output_path, level):
    try:
        slide = openslide.OpenSlide(input_path)
        
        if level >= slide.level_count:
            raise ValueError(f"Level {level} is not available. Max level is {slide.level_count - 1}.")
        
        dimensions = slide.level_dimensions[level]
        
        img = slide.read_region((0, 0), level, dimensions)

        background = Image.new("RGBA", img.size, (255, 255, 255, 255))

        img = Image.alpha_composite(background, img.convert("RGBA"))
        
        img = img.convert("RGB")
        
        img.save(output_path, "TIFF")
        
        slide.close()
        
        print(f"Saved level {level} to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MRXS file to TIFF at a specified level.")
    parser.add_argument("input", help="Input MRXS file path")
    parser.add_argument("output", help="Output TIFF file path")
    parser.add_argument("level", type=int, help="Level to extract from the MRXS file")

    args = parser.parse_args()

    convert_mrxs_to_tiff(args.input, args.output, args.level)
