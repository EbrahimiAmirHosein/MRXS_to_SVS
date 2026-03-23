import sys
import pyvips

def convert_mrxs_to_svs(input_file, output_file, compression="none", tile_width=256, tile_height=256):

    image = pyvips.Image.new_from_file(input_file, access="sequential")

    compression_options = {
        "none": "none",
        "jpeg": "jpeg",
        "lzw": "lzw",
        "deflate": "deflate",
        "packbits": "packbits",
        "ccittfax4": "ccittfax4"
    }

    if compression not in compression_options:
        raise ValueError(f"Unsupported compression type: {compression}")

    compression_option = compression_options[compression]

    save_params = {
        "tile": True,
        "tile_width": tile_width,
        "tile_height": tile_height,
        "compression": compression_option,
        "pyramid": True,
        "bigtiff": True,
        "region_shrink": "mean"
    }

    if compression == "jpeg":
        save_params["Q"] = 85 

    image.tiffsave(output_file, **save_params)

    print(f"Conversion completed: {output_file}")

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python convert_mrxs_to_svs.py input.mrxs output.svs [compression] [tile_width] [tile_height]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    compression = sys.argv[3] if len(sys.argv) > 3 else "none"
    tile_width = int(sys.argv[4]) if len(sys.argv) > 4 else 256
    tile_height = int(sys.argv[5]) if len(sys.argv) > 5 else 256
    
    convert_mrxs_to_svs(input_file, output_file, compression, tile_width, tile_height)
