
import os

def extract_lines(file_path, start_line, end_line):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return "".join(lines[start_line-1:end_line])

index_path = r'c:\Users\Lenovo\Desktop\prumac connect\index.html'
about_path = r'c:\Users\Lenovo\Desktop\prumac connect\About.html'
target_path = r'c:\Users\Lenovo\Desktop\prumac connect\contact.html.html'

# Assemble parts
content = []

# 1. Head & Opening Body (index.html 1-587)
content.append(extract_lines(index_path, 1, 587))

# 2. Page & Loader Wrapper (index.html 588-600)
content.append(extract_lines(index_path, 588, 600))

# 3. Header (index.html 602-768)
content.append("\n\t\t<!--header-->\n")
content.append(extract_lines(index_path, 602, 768))

# 4. Main Content Container Opening (index.html 771-779)
content.append("\n\t\t<!--main content-->\n")
content.append(extract_lines(index_path, 771, 779))

# 5. Hero Styles (About.html 1002-1041)
content.append("\n\t\t\t\t\t\t\t\t\t\t<style>\n")
content.append(extract_lines(about_path, 1002, 1041))

# 6. Hero Section (About.html 1042-1122)
content.append(extract_lines(about_path, 1042, 1122))

# 7. Request Quote Section (index.html 3511-3860)
content.append(extract_lines(index_path, 3511, 3860))

# 8. Main Content Container Closing (index.html 3861-3868)
content.append(extract_lines(index_path, 3861, 3868))

# 9. Footer (index.html 3870-4208)
content.append("\n\t\t<!--Footer-->\n")
content.append(extract_lines(index_path, 3871, 4208))

# 10. Closing Page Wrapper & Scripts (index.html 4209-4635)
content.append(extract_lines(index_path, 4209, 4635))

with open(target_path, 'w', encoding='utf-8') as f:
    f.write("".join(content))

print(f"Successfully reconstructed {target_path}")
