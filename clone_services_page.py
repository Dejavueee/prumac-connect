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

    # 1. Read the fetched clone html
    with open('temp_services_clone.html', 'r', encoding='utf-8') as f:
        clone_html = f.read()

    clone_soup = BeautifulSoup(clone_html, 'html.parser')

    # Find the specific CSS link to download (post-1232.css)
    css_link = clone_soup.find('link', id='elementor-post-1232-css')
    if css_link and 'href' in css_link.attrs:
        css_url = css_link['href']
        css_filename = "post-1232.css"
        css_local_path = os.path.join(assets_dir, css_filename)
        download_file(css_url, css_local_path)

    # Extract the target sections
    # Target sections data-id:
    # 81cfd85 : Our Services section
    # 07f4b44 : Trusted By Top-tier Brands section
    # 4bdc593 : Integration section
    
    section_ids = ['81cfd85', '07f4b44', '4bdc593']
    extracted_tags = []
    
    for sid in section_ids:
        tag = clone_soup.find(attrs={"data-id": sid})
        if tag:
            extracted_tags.append(tag)
        else:
            print(f"Could not find section with data-id {sid}")

    # Process extracted tags: download images and rewrite URLs
    base_url = "https://demo.7iquid.com/apexus/"
    for tag in extracted_tags:
        for img in tag.find_all('img'):
            if 'src' in img.attrs:
                img_url = img['src']
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = "https://demo.7iquid.com" + img_url
                elif not img_url.startswith('http'):
                    # Could be relative to current base path? Unlikely for WP, usually absolute.
                    pass

                # Extract filename
                filename = img_url.split('/')[-1].split('?')[0]
                local_img_path = os.path.join(assets_dir, filename)
                download_file(img_url, local_img_path)
                
                # Rewrite src
                img['src'] = f"./assets/{filename}"
                
                # Remove srcset if present since it points to remote files and we only download the main one
                if 'srcset' in img.attrs:
                    del img['srcset']
                if 'sizes' in img.attrs:
                    del img['sizes']

    # 2. Read the local services.html
    services_file = 'services.html'
    with open(services_file, 'r', encoding='utf-8') as f:
        services_html = f.read()
    
    services_soup = BeautifulSoup(services_html, 'html.parser')
    
    # Inject CSS link into head
    head_tag = services_soup.head
    if not services_soup.find('link', id='elementor-post-1232-css'):
        new_link = services_soup.new_tag('link', rel='stylesheet', id='elementor-post-1232-css', href='./assets/post-1232.css', type='text/css', media='all')
        if head_tag:
            head_tag.append(new_link)

    # Find the injection target in services.html
    # We are replacing content inside the main container, but keeping the top banner
    # The main elementor block is <div class="elementor elementor-1849">
    main_el = services_soup.find('div', class_=re.compile(r'elementor-1849'))
    
    if main_el:
        # The first child is the banner <div data-id="dd79734">... we want to KEEP this.
        # We need to find the container next to it.
        # Wait, in the target page, the services list etc are siblings to the primary heading container?
        # Let's just find the banner:
        banner = main_el.find(lambda tag: tag.has_attr('data-id') and tag['data-id'] == 'dd79734')
        if banner:
            # We want to remove all siblings of the banner inside the main_el that come after it.
            # And then insert our extracted tags.
            next_sibling = banner.find_next_sibling()
            while next_sibling:
                to_remove = next_sibling
                next_sibling = next_sibling.find_next_sibling()
                to_remove.decompose()
                
            # Now append the extracted tags
            for extracted_tag in extracted_tags:
                main_el.append(extracted_tag)
                
            print("Successfully injected new sections!")
        else:
            print("Could not find the banner (data-id='dd79734') in services.html to append after.")
    else:
        print("Could not find the main elementor-1849 container in services.html.")

    # Write back to services.html
    with open(services_file, 'w', encoding='utf-8') as f:
        f.write(str(services_soup))
    
    print("Done writing to services.html.")

if __name__ == "__main__":
    main()
