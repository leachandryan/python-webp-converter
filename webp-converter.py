#!/usr/bin/env python3
import os
import glob
import subprocess
import sys
import platform
import shutil
from pathlib import Path

def check_and_install_dependencies():
    """Check if cwebp is installed and install it if missing."""
    print("Checking dependencies...")
    
    # Check if cwebp is in PATH
    if shutil.which("cwebp") is not None:
        print("✓ cwebp is already installed.")
        return True
    
    print("× cwebp is not installed. Attempting to install...")
    
    # Determine operating system
    system = platform.system().lower()
    
    try:
        if system == "linux":
            # Try to determine the package manager
            if shutil.which("apt-get"):
                print("Detected apt package manager. Installing webp...")
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", "webp"], check=True)
            elif shutil.which("dnf"):
                print("Detected dnf package manager. Installing libwebp-tools...")
                subprocess.run(["sudo", "dnf", "install", "-y", "libwebp-tools"], check=True)
            elif shutil.which("yum"):
                print("Detected yum package manager. Installing libwebp-tools...")
                subprocess.run(["sudo", "yum", "install", "-y", "libwebp-tools"], check=True)
            elif shutil.which("pacman"):
                print("Detected pacman package manager. Installing libwebp...")
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "libwebp"], check=True)
            elif shutil.which("zypper"):
                print("Detected zypper package manager. Installing libwebp-tools...")
                subprocess.run(["sudo", "zypper", "install", "-y", "libwebp-tools"], check=True)
            else:
                print("Unable to detect package manager. Please install cwebp manually.")
                return False
                
        elif system == "darwin":  # macOS
            if shutil.which("brew"):
                print("Detected Homebrew. Installing webp...")
                subprocess.run(["brew", "install", "webp"], check=True)
            else:
                print("Homebrew not found. Please install it first: https://brew.sh/")
                return False
                
        elif system == "windows":
            print("Automatic installation on Windows is not supported.")
            print("Please download and install from: https://developers.google.com/speed/webp/download")
            return False
            
        else:
            print(f"Unsupported operating system: {system}")
            return False
            
        # Verify installation
        if shutil.which("cwebp") is not None:
            print("✓ cwebp has been successfully installed.")
            return True
        else:
            print("× Failed to install cwebp. Please install it manually.")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        return False

def main():
    # Check and install dependencies
    if not check_and_install_dependencies():
        print("Required dependency cwebp could not be installed. Exiting.")
        sys.exit(1)
    
    # Default parameters
    params = ['-m', '6', '-q', '70', '-mt', '-af', '-progress']
    
    # Use command line arguments if provided
    if len(sys.argv) > 1:
        params = sys.argv[1:]
    
    # Change to current working directory
    os.chdir(os.getcwd())
    
    # Find all image files
    img_extensions = ['*.jpeg', '*.jpg', '*.png', '*.tiff', '*.tif', '*.bmp']
    img_files = []
    for ext in img_extensions:
        img_files.extend(glob.glob(f"**/{ext}", recursive=True))
    
    # Find all GIF files
    gif_files = glob.glob("**/*.gif", recursive=True)
    
    total_img = len(img_files)
    total_gif = len(gif_files)
    
    print(f"There are {total_img} image files and {total_gif} GIF files to be converted.")
    
    # Convert image files
    for idx, img in enumerate(img_files, 1):
        print(f"Converting {img}, {idx}/{total_img}")
        output_file = f"{os.path.splitext(img)[0]}.webp"
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Construct cwebp command
        cmd = ['cwebp'] + params + [img, '-o', output_file]
        
        # Run conversion
        try:
            subprocess.run(cmd, check=True)
            success = "✓"
        except subprocess.CalledProcessError:
            print(f"Error converting {img}")
            success = "×"
        
        # Print progress with green color
        print(f"\033[0;32m {success} {idx} out of {total_img} images converted \033[0m")
        print(f"\033[0;32m {0} out of {total_gif} GIFs converted \033[0m")
    
    # Convert GIF files
    for idx, gif in enumerate(gif_files, 1):
        print(f"Converting {gif}, {idx}/{total_gif}")
        output_file = f"{os.path.splitext(gif)[0]}.webp"
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Construct cwebp command
        cmd = ['cwebp'] + params + [gif, '-o', output_file]
        
        # Run conversion
        try:
            subprocess.run(cmd, check=True)
            success = "✓"
        except subprocess.CalledProcessError:
            print(f"Error converting {gif}")
            success = "×"
        
        # Print progress with green color
        print(f"\033[0;32m {success} {idx} out of {total_gif} GIFs converted \033[0m")

if __name__ == "__main__":
    main()