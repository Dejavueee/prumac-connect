$about_path = "About.html"
$index_path = "index.html"
$services_path = "services.html"

# 1. Read About.html
$about_content = Get-Content $about_path -Raw -Encoding UTF8

# Extract Header + Hero
# Find the start of the Trusted Brands section to use as the cut-off point
$header_end_marker = '<div class="elementor-element elementor-element-6ff3863 e-flex e-con-boxed e-con e-parent e-lazyloaded"'
$header_end_idx = $about_content.IndexOf($header_end_marker)
if ($header_end_idx -eq -1) {
    Write-Error "Could not find header/hero end marker in About.html"
    exit
}

# Also grab the <style> block right before it if we want, but actually it's easier to just take everything up to the 6ff3863 marker.
$header_hero_part = $about_content.Substring(0, $header_end_idx)

# Extract Footer Shell
$footer_marker = '<footer id="pxl-footer"'
$footer_idx = $about_content.IndexOf($footer_marker)
if ($footer_idx -eq -1) {
    Write-Error "Could not find pxl-footer in About.html"
    exit
}
$footer_part = $about_content.Substring($footer_idx)

# 2. Read Index.html
$index_content = Get-Content $index_path -Raw -Encoding UTF8

# Extract Services Section
$srv_start_marker = 'class="elementor-element elementor-element-3048bdc e-con-full e-flex e-con e-parent e-lazyloaded"'
$srv_end_marker = '<!--why choose us-->'

$srv_start_idx = $index_content.IndexOf($srv_start_marker)
if ($srv_start_idx -eq -1) {
    Write-Error "Could not find Services start marker in index.html"
    exit
}

$tag_start = $index_content.LastIndexOf('<div', $srv_start_idx)

$srv_end_idx = $index_content.IndexOf($srv_end_marker)
if ($srv_end_idx -eq -1) {
    Write-Error "Could not find Services end marker in index.html"
    exit
}

$services_part = $index_content.Substring($tag_start, $srv_end_idx - $tag_start)

# Strip Animation classes to make elements visible immediately
$services_part = $services_part.Replace('pxl-anm-pxl_fadeInUp', '')
$services_part = $services_part.Replace('pxl-anm-pxl_fadeInDown', '')
$services_part = $services_part.Replace('pxl-anm-pxl_fadeIn', '')
$services_part = $services_part.Replace('pxl-invisible', '')
$services_part = $services_part.Replace('pxl-animated', '')
$services_part = $services_part.Replace('opacity: 0;', 'opacity: 1;')

# 3. Assemble components
$final_html = $header_hero_part + "`n" + $services_part + "`n</div>`n</div>`n" + $footer_part

# 4. Replacements for context
$final_html = $final_html.Replace('<title>About Us - Prumac Connect</title>', '<title>Services - Prumac Connect</title>')
$final_html = $final_html.Replace('<h1 class="main-title">About Us</h1>', '<h1 class="main-title">Our Services</h1>')

# Add spacing above the services grid so it isn't squeezed under the hero
$final_html = $final_html.Replace('<div style="clip-path: polygon(0% 0, 100% 0, 100% 95%, 97.5% 100%, 0 100%, 0 0%);"', '<div style="clip-path: polygon(0% 0, 100% 0, 100% 95%, 97.5% 100%, 0 100%, 0 0%); padding-top: 100px; padding-bottom: 50px;"')

# Update Nav Active State
# Remove active class from 'About.html' li
$final_html = $final_html -replace 'id="menu-item-2700"\s+class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-2690 current_page_item menu-item-2700"', 'id="menu-item-2700" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-2700"'

# Add active class to 'services.html' li
$final_html = $final_html -replace 'id="menu-item-2701"\s+class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-2701"', 'id="menu-item-2701" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item current_page_item menu-item-has-children menu-item-2701"'

# Also remove active state from 'Home' li (current-menu-ancestor etc)
$final_html = $final_html -replace 'current-menu-ancestor current-menu-parent current_page_parent current_page_ancestor', ''

# 5. Save
Set-Content -Path $services_path -Value $final_html -Encoding UTF8
Write-Host "Success: services.html fully assembled with hero and visible services grid."
