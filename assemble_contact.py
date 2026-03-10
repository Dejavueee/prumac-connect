import re

def assemble_contact():
    # File Paths
    index_path = "index.html"
    contact_path = "contact.html"
    
    # 1. Read Index.html (Source for Request Quote + Footer)
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    # Extract from Request Quote Start to End of File
    # Marker: elementor-element-613369c is the Request Quote section container
    req_quote_marker = 'elementor-element-613369c'
    if req_quote_marker not in index_content:
        print("Error: Could not find Request Quote section in index.html")
        return

    # Find the start of the div containing this class
    # We look for the class string, then backtrack to the start of the tag
    start_pos = index_content.find(req_quote_marker)
    # Backtrack to find '<div'
    # The actual line in index.html is: <div style="clip-path: ... class="... 613369c ...">
    # So we look for the last "<div" before the marker
    tag_start = index_content.rfind('<div', 0, start_pos)
    
    index_part = index_content[tag_start:]
    
    # 2. Read Contact.html (Source for Header + Hero)
    with open(contact_path, "r", encoding="utf-8") as f:
        contact_content = f.read()

    # Extract up to the end of Hero Section
    # Hero container: elementor-element-dd79734
    # The next section is "Trusted Brands" with style block starting at line 785 approx
    # Search for the style block comment or the class of next section elementor-element-6ff3863
    
    # We will cut BEFORE the style block that follows the hero
    cut_marker = '/* Remove spacing from Hero Section */'
    if cut_marker in contact_content:
        cut_pos = contact_content.find('<style>', contact_content.rfind('<style>', 0, contact_content.find(cut_marker)))
        # Actually simplest is to find the Hero Container End. 
        # But cutting at the specific style tag we identified in view_file is safer if unique.
        # Let's try locating the Next Section Class: elementor-element-6ff3863
        # And the style tag before it.
        pass
    else:
        # Fallback: Find "About Us" Title and cut after its container closes? Risky.
        # Let's use the elementor-element-6ff3863 marker
        next_section_marker = 'elementor-element-6ff3863'
        if next_section_marker in contact_content:
             # Find the style tag preceding this
             content_start_of_next = contact_content.find(next_section_marker)
             cut_pos = contact_content.rfind('<div', 0, content_start_of_next) # This is the container start
             # We want to remove the style block before it too?
             # The style block contained ".elementor-element-6ff3863" css rules.
             # So searching for the first occurrence of ".elementor-element-6ff3863" in a style tag?
             cut_pos = contact_content.find('.elementor-element-6ff3863')
             # Backtrack to <style>
             cut_pos = contact_content.rfind('<style>', 0, cut_pos)
        else:
            print("Error: Could not find extraction point in contact.html")
            return

    contact_part = contact_content[:cut_pos]

    # 3. Create Map Section
    map_html = '''
    <!-- Map Section -->
    <div class="elementor-element e-con-full e-flex e-con e-parent" data-element_type="container" style="width: 100%; height: 500px; margin-bottom: 0;">
        <div class="elementor-widget-container" style="width: 100%; height: 100%;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15198.814045934524!2d31.053028!3d-17.824858!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1931a4f00994f797%3A0xe5433066d929b775!2sHarare%2C%20Zimbabwe!5e0!3m2!1sen!2szw!4v1700000000000!5m2!1sen!2szw" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
    </div>
    '''

    # 4. Assemble
    final_html = contact_part + "\n" + map_html + "\n" + index_part

    # 5. Text Replacements
    # Logic: "About Us" -> "Contact Us" in Title and Hero
    final_html = final_html.replace('<title>About Us', '<title>Contact Us')
    final_html = final_html.replace('<h1 class="main-title">About Us</h1>', '<h1 class="main-title">Contact Us</h1>')

    # Update Navigation
    # Remove active class from About (menu-item-2700)
    # Add active class to Contact? 
    # Contact is a button <a href="contact.html" class="pxl-btn ...">
    # Maybe highlighting isn't needed for the button in the same way.
    # But we should remove "current-menu-item" from Home or About if present in the header we kept.
    # The header we kept is from About.html, so 'About Us' (menu-item-2700) likely has 'current-menu-ancestor' etc.
    final_html = final_html.replace('current-menu-ancestor', '')
    final_html = final_html.replace('current-menu-parent', '')
    final_html = final_html.replace('current_page_parent', '')
    final_html = final_html.replace('current_page_ancestor', '')
    # Ensure About Us link is clean
    final_html = final_html.replace('<a href="About.html" style="opacity: 1;">', '<a href="About.html">')
    
    # 6. Save
    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("Success: contact.html assembled.")

if __name__ == "__main__":
    assemble_contact()
