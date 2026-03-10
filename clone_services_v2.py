import os
import re
import urllib.request
from bs4 import BeautifulSoup

def download_file(url, local_path):
    print(f"Downloading {url} to {local_path}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    assets_dir = 'assets'
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        
    font_dir = os.path.join(assets_dir, 'fonts', 'pixelart')
    if not os.path.exists(font_dir):
        os.makedirs(font_dir)

    # 1. Download the fonts to fix the missing icons
    font_files = ['pxli.ttf', 'pxli.woff', 'pxli.svg']
    for file in font_files:
        url = f"https://demo.7iquid.com/apexus/wp-content/themes/apexus/assets/fonts/pixelart/{file}"
        download_file(url, os.path.join(font_dir, file))
        # Also put it in assets directly just in case style.css is looking there
        download_file(url, os.path.join(assets_dir, file))
        
    # Download the style(2).css if missing
    download_file("https://demo.7iquid.com/apexus/wp-content/themes/apexus/style.css", os.path.join(assets_dir, 'style(2).css'))
    
    # 2. Read the local temp_services_clone.html
    with open('temp_services_clone.html', 'r', encoding='utf-8') as f:
        target_soup = BeautifulSoup(f, 'html.parser')
        
    # Extract the full content of <div class="elementor-1232">
    elementor_1232 = target_soup.find('div', class_=re.compile(r'elementor-1232'))
    if not elementor_1232:
        print("Could not find elementor-1232 inside temp_services_clone.html")
        return
        
    # Process images to download them and rewrite URLs
    sections_to_process = [elementor_1232]
    for section in sections_to_process:
        if not section:
            continue
        for img in section.find_all('img'):
            if 'src' in img.attrs:
                img_url = img['src']
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = "https://demo.7iquid.com" + img_url
                
                if 'http' in img_url:
                    filename = img_url.split('/')[-1].split('?')[0]
                    local_img_path = os.path.join(assets_dir, filename)
                    if not os.path.exists(local_img_path):
                        download_file(img_url, local_img_path)
                    img['src'] = f"./assets/{filename}"
                
                # Cleanup srcset and sizes
                if 'srcset' in img.attrs:
                    del img['srcset']
                if 'sizes' in img.attrs:
                    del img['sizes']
                    
    # 3. Read the local services.html
    services_file = 'services.html'
    with open(services_file, 'r', encoding='utf-8') as f:
        services_soup = BeautifulSoup(f, 'html.parser')
        
    # Inject CSS link into head
    head_tag = services_soup.head
    if not services_soup.find('link', id='elementor-post-1232-css'):
        new_link = services_soup.new_tag('link', rel='stylesheet', id='elementor-post-1232-css', href='./assets/post-1232.css', type='text/css', media='all')
        if head_tag:
            head_tag.append(new_link)

    # We want to replace the inner workings of <main id="pxl-content-main">
    main_content = services_soup.find('main', id='pxl-content-main')
    
    if main_content:
        # Clear main_content
        main_content.clear()
        
        # Insert the elementor_1232
        new_article = services_soup.new_tag('article', id='post-1232', attrs={'class': 'post-1232 page type-page status-publish hentry'})
        new_entry_content = services_soup.new_tag('div', attrs={'class': 'pxl-entry-content clearfix'})
        new_entry_content.append(elementor_1232)
        new_article.append(new_entry_content)
        main_content.append(new_article)
        print("Successfully injected new elementor-1232 into main_content.")
        
    else:
        print("Could not find <main id='pxl-content-main'> in services.html")

    # Save the file
    with open(services_file, 'w', encoding='utf-8') as f:
        f.write(str(services_soup))
    print("Done writing to services.html")

if __name__ == "__main__":
    main()
