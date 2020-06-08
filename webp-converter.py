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