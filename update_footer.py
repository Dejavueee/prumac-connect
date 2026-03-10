import glob
import re
import os

def update_files():
    files = glob.glob("c:/Users/Lenovo/Desktop/prumac connect/*.html")
    
    print(f"Found {len(files)} HTML files.")

    # Replacement Definitions
    replacements = [
        # Email
        (r"hello@apexusglobal\.com", "info@prumacconnect.co.zw"),
        
        # Phone Link
        (r"tel:14081234567", "tel:0775454692"),
        
        # Phone Display (flexible spacing)
        (r"\+1\s*408\s*123\s*4567", "0775454692"),
        
        # Address (Multi-line regex handling)
        # We look for Apexus Inc, followed by content until United States
        (r"Apexus Inc\.<br>.*?United States", 
         "Cnr L. Takawira <br>& J. Tongogara Ave, <br>Property Center, 2nd Floor Suite 7<br>Bulawayo"),

        # Copyright - targeted replacement
        # Matches: ©2025 <a ...>Apexus</a>. All rights reserved.
        # Or just "Apexus. All rights reserved." if without link
        (r"©2025\s*<a[^>]*>Apexus</a>\.\s*All rights reserved\.", "©2025 Prumac Connect. All rights reserved."),
        (r"©2025\s*Apexus\.\s*All rights reserved\.", "©2025 Prumac Connect. All rights reserved."),
        
        # Just in case "Apexus" plain text in copyright without date matches differently
        # (r"Apexus\.\s*All rights reserved\.", "Prumac Connect. All rights reserved.")
    ]

    for file_path in files:
        print(f"Processing {os.path.basename(file_path)}...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            for pattern, replacement in replacements:
                # Compile regex with DOTALL for address to span lines
                regex = re.compile(pattern, re.DOTALL | re.IGNORECASE)
                new_content = regex.sub(replacement, new_content)
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Updated {os.path.basename(file_path)}")
            else:
                print(f"  No changes needed for {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"  Error processing {file_path}: {e}")

if __name__ == "__main__":
    update_files()
