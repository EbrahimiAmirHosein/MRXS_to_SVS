import argparse
import openslide
from PIL import Image

def convert_mrxs_to_tiff(input_path, output_path, level):
    try:
        slide = openslide.OpenSlide(input_path)
        
        if level >= slide.level_count:
            raise ValueError(f"Level {level} is not available. Max level is {slide.level_count - 1}.")
        
        dimensions = slide.level_dimensions[level]
        
        # Read region and keep alpha channel
        img = slide.read_region((0, 0), level, dimensions)

        # Create a white background image in "RGBA" mode
        background = Image.new("RGBA", img.size, (255, 255, 255, 255))

        # Paste the image onto the background using the alpha channel as mask
        img = Image.alpha_composite(background, img.convert("RGBA"))
        
        # Convert to "RGB" to save as TIFF
        img = img.convert("RGB")
        
        img.save(output_path, "TIFF")
        
        slide.close()
        
        print(f"Saved level {level} to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert MRXS file to TIFF at a specified level.")
    parser.add_argument("input", help="Input MRXS file path")
    parser.add_argument("output", help="Output TIFF file path")
    parser.add_argument("level", type=int, help="Level to extract from the MRXS file")

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function with parsed arguments
    convert_mrxs_to_tiff(args.input, args.output, args.level)
