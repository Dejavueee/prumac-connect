import re
import os
import shutil

# Paths
faq_source = "FAQs – Apexus.html"
faq_target = "faq.html"
assets_dir = "assets"
css_source_dir = "FAQs – Apexus_files"

# Read Source
with open(faq_source, "r", encoding="utf-8") as f:
    source_content = f.read()

# Extract Content (Article)
# Start: <article id="post-593"
# End: </article>
# We'll use regex to grab the specific article block.
# Note: There might be nested articles, but looking at the file, the main one is post-593.
match = re.search(r'(<article id="post-593".*?</article>)', source_content, re.DOTALL)
if not match:
    print("Error: Could not find article content in source.")
    exit(1)
new_content = match.group(1)

# Read Target
with open(faq_target, "r", encoding="utf-8") as f:
    target_content = f.read()

# 1. Replace Content
# Target is <article id="post-1849" ... </article>
# We need to find this block.
target_content = re.sub(r'<article id="post-1849".*?</article>', new_content, target_content, flags=re.DOTALL)

# 2. Update Image Paths in the new content (within target_content now, or just replace in new_content first)
# The regex replaced it, but let's run a path fix over the whole file or just the inserted part? 
# Better to run it over the whole file just in case, or at least the part we touched.
# Source uses "./FAQs – Apexus_files/"
# We want "./assets/"
target_content = target_content.replace("./FAQs – Apexus_files/", "./assets/")

# 3. Update Title
target_content = target_content.replace("<title>About Us - Prumac Connect</title>", "<title>FAQs - Prumac Connect</title>")

# 4. Update CSS Link
# Add faq.css after main.css
css_link = '<link rel="stylesheet" id="pxl-faq-css" href="./assets/css/faq.css" type="text/css" media="all">'
if "assets/main.css" in target_content:
    target_content = target_content.replace('href="./assets/main.css" type="text/css" media="all">', 'href="./assets/main.css" type="text/css" media="all">\n\t' + css_link)

# 5. Update Navigation
# Remove active class from Home (menu-item-2698) or About (menu-item-2700)
# Structure: <li id="menu-item-2698" class="menu-item ... current-menu-ancestor ...">
# We'll just strip "current-menu-ancestor current-menu-parent current_page_parent current_page_ancestor" from everywhere to be clean
target_content = target_content.replace("current-menu-ancestor", "")
target_content = target_content.replace("current-menu-parent", "")
target_content = target_content.replace("current_page_parent", "")
target_content = target_content.replace("current_page_ancestor", "")

# Add active class to FAQ (menu-item-4300)
# <li id="menu-item-4300" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4300">
# We want it to be: ... menu-item-4300 current-menu-item">
target_content = target_content.replace('menu-item-4300">', 'menu-item-4300 current-menu-item">')

# Write back
with open(faq_target, "w", encoding="utf-8") as f:
    f.write(target_content)

print("Successfully replaced content and updated links.")
