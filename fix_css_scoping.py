import sys
import re

def main():
    try:
        with open('services.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the div containing 'ef083ac'
        match = re.search(r'<div[^>]*ef083ac[^>]*>', content)
        if not match:
            print("Could not find the start of the Request Quote section.")
            return

        print("Replacing start tag...")
        start_idx = match.start()
        end_idx_of_tag = match.end()
        # Insert <div class="elementor-2761"> before this tag
        content = content[:start_idx] + '<div class="elementor-2761">\n' + content[start_idx:]

        # Now find the </article> and close the div
        # Since we shifted content, we need to search after start_idx + a bit
        end_str = '</article>'
        article_idx = content.find(end_str, start_idx)
        if article_idx == -1:
            print("Could not find </article>.")
            return
            
        print("Closing the wrapper before </article>...")
        content = content[:article_idx] + '</div>\n\t\t\t\t\t\t\t\t\t' + content[article_idx:]

        # Insert missing CSS links into <head>
        head_end_str = '</head>'
        links_to_add = """
    <link rel="stylesheet" id="elementor-post-2761-css" href="./assets/post-2761.css" type="text/css" media="all">
    <link rel="stylesheet" id="elementor-post-3696-css" href="./assets/post-3696.css" type="text/css" media="all">
    <link rel="stylesheet" id="elementor-post-3725-css" href="./assets/post-3725.css" type="text/css" media="all">
"""
        if 'post-2761.css' not in content:
            print("Adding missing stylesheets to head...")
            content = content.replace(head_end_str, links_to_add + '\n' + head_end_str)

        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Successfully updated services.html layout scoping.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
