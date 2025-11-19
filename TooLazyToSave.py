import time
import os
import hashlib
import re  # Used for regular expressions
from datetime import datetime
from PIL import ImageGrab, Image

# --- 🚀 CONFIGURATION ---
# Set your variable part of the filename here
# Example: "FEATURE_LOGIN" will result in "TC_FEATURE_LOGIN_01.png"
TC_PREFIX_NAME = "AFE"
# -----------------------

def get_next_tc_number(save_directory, prefix_name):
    """
    Finds the first available test case number (e.g., TC_TEST_01.png).
    If TC_TEST_01.png and TC_TEST_03.png exist, this will return 2.
    """
    
    # This pattern is now dynamic based on the prefix_name.
    # It will match "TC_<prefix_name>_" followed by digits, and ".png".
    pattern = re.compile(f"^TC_{re.escape(prefix_name)}_(\\d+)\\.png$", re.IGNORECASE)
    
    existing_numbers = set()
    
    try:
        for filename in os.listdir(save_directory):
            match = pattern.match(filename)
            if match:
                # match.group(1) is the captured digits (e.g., "01", "02")
                existing_numbers.add(int(match.group(1)))
    except FileNotFoundError:
        pass 

    # Start checking from 1
    current_number = 1
    while True:
        # Loop until we find a number NOT in the set
        if current_number in existing_numbers:
            current_number += 1
        else:
            # Found the first gap!
            return current_number

def main():
    save_directory = os.path.dirname(os.path.abspath(__file__))
    
    print(f"🚀 Screenshot Watcher Started.")
    print(f"Saving files to: {save_directory}")
    print(f"Files will be named: TC_{TC_PREFIX_NAME}_01.png, TC_{TC_PREFIX_NAME}_02.png, etc.")
    print("Press Ctrl+C to stop.")

    last_image_hash = None

    try:
        while True:
            clipboard_content = ImageGrab.grabclipboard() 
            img = None 

            # Case 1: It's already an image object
            if isinstance(clipboard_content, Image.Image):
                img = clipboard_content
            
            # Case 2: It's a list (from Win+Shift+S on your system)
            elif isinstance(clipboard_content, list):
                if clipboard_content:
                    filepath = clipboard_content[0]
                    if isinstance(filepath, str) and filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                        try:
                            img = Image.open(filepath)
                        except Exception:
                            pass # Failed to open file

            # --- SAVING LOGIC ---
            if img:
                current_image_hash = hashlib.md5(img.tobytes()).hexdigest()

                if current_image_hash != last_image_hash:
                    
                    # --- UPDATED NAMING LOGIC ---
                    # Get the next available TC number, passing our prefix
                    tc_number = get_next_tc_number(save_directory, TC_PREFIX_NAME)
                    
                    # Format the filename with the prefix and zero-padded number
                    # {tc_number:02d} means "format as integer, pad with 0 to 2 digits"
                    filename = f"TC_{TC_PREFIX_NAME}_{tc_number:02d}.png"
                    # --- END UPDATED NAMING LOGIC ---

                    save_path = os.path.join(save_directory, filename)
                    
                    img.save(save_path, 'PNG')
                    
                    print(f"✅ Saved: {filename}")
                    last_image_hash = current_image_hash
                else:
                    pass
            
            else:
                last_image_hash = None

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Watcher stopped. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()