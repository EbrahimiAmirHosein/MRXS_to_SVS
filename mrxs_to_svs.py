import sys
import pyvips

def convert_mrxs_to_svs(input_file, output_file, compression="none", tile_width=256, tile_height=256):
    # Open the MRXS file
    image = pyvips.Image.new_from_file(input_file, access="sequential")
    
    # Prepare compression settings
    if compression == "none":
        compression_option = None
    elif compression == "jpeg":
        compression_option = "jpeg"
    elif compression == "lzw":
        compression_option = "lzw"
    elif compression == "deflate":
        compression_option = "deflate"
    elif compression == "packbits":
        compression_option = "packbits"
    elif compression == "ccittfax4":
        compression_option = "ccittfax4"
    else:
        raise ValueError(f"Unsupported compression type: {compression}")
    
    # Save the image to SVS format with the chosen options
    image.tiffsave(output_file, tile=True, tile_width=tile_width, tile_height=tile_height,
                   compression=compression_option, pyramid=True)

    print(f"Conversion completed: {output_file}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python convert_mrxs_to_svs.py input.mrxs output.svs [compression] [tile_width] [tile_height]")
        sys.exit(1)
    
    # Get input and output file names from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Get optional compression and tile size (with defaults)
    compression = sys.argv[3] if len(sys.argv) > 3 else "none"
    tile_width = int(sys.argv[4]) if len(sys.argv) > 4 else 256
    tile_height = int(sys.argv[5]) if len(sys.argv) > 5 else 256
    
    # Run the conversion
    convert_mrxs_to_svs(input_file, output_file, compression, tile_width, tile_height)

