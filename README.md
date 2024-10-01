# MRXS_to_SVS


# Steps to Convert MRXS to SVS using Vips and a Bash Script


## 2. Make the Script Executable

Run the following command to make the script executable:

```bash
chmod +x mrxs_to_svs.sh
```

## 3. Run the Script

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
