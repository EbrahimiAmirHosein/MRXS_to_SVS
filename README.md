# **MRXS to SVS Conversion**

Microscopic images are often collected from various labs across different locations, leading to variations in the file formats used for storage. This project aims to simplify the process of working with these diverse formats by leveraging existing libraries, such as Vips, to create user-friendly scripts. These scripts are designed to assist individuals with limited programming experience in managing image conversions.

The first phase of the project focuses on converting MRXS files to the more commonly used SVS format. MRXS files often contain multiple directories and data files, making them difficult to open and manage. By streamlining this conversion, we aim to reduce the complexity and improve accessibility for researchers and lab technicians.

Additional features will be introduced in future phases, including support for converting multiple image formats, further enhancing the flexibility and ease of use of the tool.

## Requirements

- **Ubuntu**:
  
libvips
```bash
sudo apt install libvips
sudo apt install libvips-tools
sudo apt install libvips-dev
```
pyvips
```bash
pip install pyvips
```

- **Windows**:
  
pyvips
```bash
pip install pyvips
```

Follow the instruction [here](https://www.libvips.org/install.html)



# Bash Script: Convert MRXS to SVS using Vips ( Recommended )

First download the mrxs_to_svs.sh.

## 1. Make the Script Executable

Run the following command to make the script executable:

```bash
chmod +x mrxs_to_svs.sh
```

## 2. Run the Script

Use the following syntax to run the script:

```bash
./mrxs_to_svs.sh input.mrxs output.svs [compression] [tile_width] [tile_height]
```

### Examples

#### Common Compression Options:
1.  **none**: No compression (default if not specified).
2.  **jpeg**: JPEG compression, which is lossy but commonly used in image formats like SVS.
3.  **lzw**: LZW compression, a lossless method commonly used in TIFF files.
4.  **deflate**: DEFLATE compression, another lossless method that provides higher compression than LZW.
5.  **packbits**: A simple form of compression (not as efficient as LZW or deflate).
6.  **ccittfax4**: A lossless compression method used for black-and-white images, mainly in fax machines (less common for medical imaging).

#### Commands


1. **Without Compression** (default tile size 256x256):
    ```bash
    ./mrxs_to_svs.sh input.mrxs output.svs none
    ```

2. **With JPEG Compression and Custom Tile Size**:
    ```bash
    ./mrxs_to_svs.sh input.mrxs output.svs jpeg 512 512
    ```

3. **With LZW Compression and Default Tile Size**:
    ```bash
    ./mrxs_to_svs.sh input.mrxs output.svs lzw
    ```
4. **With packbits Compression and Default Tile Size**:
    ```bash
    ./mrxs_to_svs.sh input.mrxs output.svs packbits
    ```
5. **With ccittfax4 Compression and Default Tile Size**:
    ```bash
    ./mrxs_to_svs.sh input.mrxs output.svs ccittfax4
    ```



# Python Script: Convert MRXS to SVS using PyVips ( Recommended )


## How to Run:

1. **Install PyVips** (if not installed):
   ```bash
   pip install pyvips
   ```

2. **Run the Script**:
   ```bash
   python mrxs_to_svs_pyvips.py input.mrxs output.svs [compression] [tile_width] [tile_height]
   ```

## Examples:

1. **Without Compression** (default tile size 256x256):
   ```bash
   python mrxs_to_svs_pyvips.py input.mrxs output.svs none
   ```

2. **With JPEG Compression and Custom Tile Size**:
   ```bash
   python mrxs_to_svs_pyvips.py input.mrxs output.svs jpeg 512 512
   ```

3. **With LZW Compression and Default Tile Size**:
   ```bash
   python mrxs_to_svs_pyvips.py input.mrxs output.svs lzw
   ```

## Compression Options:
- `none`: No compression (default)
- `jpeg`: JPEG compression
- `lzw`: LZW compression
- `deflate`: DEFLATE compression
- `packbits`: PackBits compression
- `ccittfax4`: CCITT Group 4 fax compression (for black-and-white images)

# Python Script: Convert MRXS to SVS using OpenSlide ( Not Efficient )
I don't recommend using this version unless you have to.
1. **Install OpenSlde**
```bash
pip install openslide-python
```
2. **You need a sepereate OpenSlide package, Install it using the instruction [here](https://openslide.org/api/python/#installing)**

3. **Run the Script**:
   ```bash
   python mrxs_to_svs_openslide.py "path/to/input.mrxs" "path/to/output.svs" [level]
   ```
## level Options:
- `0`: Highest Resolution - ( Requires High RAM )
- `1`: 2nd Highest Resolution - ( Requires High RAM )
- `n`: All the way to the lowes resolution 

