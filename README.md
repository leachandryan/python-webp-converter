# WebP Converter

A Python utility that automatically converts image files to WebP format throughout a directory and all its subdirectories.

## Overview

This script recursively searches through the current directory and all subdirectories for image files (JPEG, PNG, TIFF, BMP) and GIF files, then converts them to WebP format. The original files are preserved, and WebP versions are created alongside them.

WebP is a modern image format that provides superior compression for images on the web, resulting in smaller file sizes while maintaining visual quality.

## Features

- Automatically detects and installs the required dependency (`cwebp`) if missing
- Supports recursive conversion (including all subdirectories)
- Preserves original files
- Supports multiple image formats:
  - JPEG (.jpg, .jpeg)
  - PNG (.png)
  - TIFF (.tiff, .tif)
  - BMP (.bmp)
  - GIF (.gif)
- Provides progress tracking with clear visual feedback
- Configurable conversion parameters

## Requirements

- Python 3.6 or higher
- cwebp (automatically installed if missing on supported platforms)

## Installation

1. Download the `webp-converter.py` script
2. Make the script executable (optional, for Unix-like systems):
   ```bash
   chmod +x webp-converter.py
   ```

## Usage

### Basic Usage

1. Place the script in the root directory where your images are located
2. Run the script:
   ```bash
   python3 webp-converter.py
   ```

That's it! The script will:
1. Check if the required `cwebp` dependency is installed
2. Install it if needed (on supported platforms)
3. Find all supported image files in the current directory and subdirectories
4. Convert each file to WebP format with default settings

### Custom Parameters

You can customize the conversion parameters by passing them as command-line arguments:

```bash
python3 webp-converter.py -q 80 -m 5
```

### Common Parameters

- `-q <quality>`: Quality factor (0-100, default: 70)
- `-m <compression>`: Compression method (0-6, default: 6, higher=slower)
- `-lossless`: Use lossless compression
- `-exact`: Preserve RGB values in transparent areas
- `-z`: Use Zlib compression
- `-mt`: Use multi-threading for encoding

For a complete list of parameters, see the [cwebp documentation](https://developers.google.com/speed/webp/docs/cwebp).

## How It Works

The script:
1. Checks for and installs the required `cwebp` dependency if needed
2. Recursively finds all supported image files
3. For each file, creates a WebP version with the same base name and a `.webp` extension
4. Shows progress during conversion

## Supported Platforms

- **Linux**: Supports apt, dnf, yum, pacman, and zypper package managers
- **macOS**: Supports installation via Homebrew
- **Windows**: Automatic installation not supported, but the script will work if `cwebp` is manually installed and added to PATH

## Troubleshooting

- **Permission denied**: Run with `sudo` or ensure you have write permissions to the directories
- **cwebp installation fails**: Install manually following the [official instructions](https://developers.google.com/speed/webp/download)
- **File not found errors**: Ensure file paths don't contain special characters

## License

This project is open-source and free to use. Feel free to modify and distribute as needed.