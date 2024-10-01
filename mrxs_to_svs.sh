#!/bin/bash

# Usage: ./mrxs_to_svs.sh input.mrxs output.svs compression_level tile_width tile_height

# Check if the correct number of arguments is provided
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 input.mrxs output.svs [compression_level] [tile_width] [tile_height]"
  exit 1
fi

# Set input and output files
INPUT_FILE=$1
OUTPUT_FILE=$2

# Set compression level (default to 'none' if not provided)
COMPRESSION=${3:-none}

# Set tile width and height (default to 256x256 if not provided)
TILE_WIDTH=${4:-256}
TILE_HEIGHT=${5:-256}

# Check the compression type and build the vips command accordingly
if [ "$COMPRESSION" == "none" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
elif [ "$COMPRESSION" == "jpeg" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --compression jpeg --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
elif [ "$COMPRESSION" == "lzw" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --compression lzw --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
elif [ "$COMPRESSION" == "deflate" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --compression deflate --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
elif [ "$COMPRESSION" == "packbits" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --compression packbits --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
elif [ "$COMPRESSION" == "ccittfax4" ]; then
  vips tiffsave "$INPUT_FILE" "$OUTPUT_FILE" --tile --compression ccittfax4 --tile-width "$TILE_WIDTH" --tile-height "$TILE_HEIGHT" --pyramid
else
  echo "Unsupported compression type: $COMPRESSION"
  exit 1
fi

echo "Conversion completed: $OUTPUT_FILE"
