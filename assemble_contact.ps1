$index_path = "index.html"
$contact_path = "contact.html"

# 1. Read Index.html
$index_content = Get-Content $index_path -Raw -Encoding UTF8

# Extract Request Quote + Footer
# Find "elementor-element-613369c"
$req_quote_marker = 'elementor-element-613369c'
$start_idx = $index_content.IndexOf($req_quote_marker)

if ($start_idx -eq -1) {
    Write-Error "Could not find Request Quote section in index.html"
    exit
}

# Find the last "<div" before the marker
$tag_start = $index_content.LastIndexOf('<div', $start_idx)
$index_part = $index_content.Substring($tag_start)

# 2. Read Contact.html
$contact_content = Get-Content $contact_path -Raw -Encoding UTF8

# Extract Hero Section (Stop before "Trusted Brands" / Style Block)
$cut_marker = '/* Remove spacing from Hero Section */'
$cut_idx = $contact_content.IndexOf($cut_marker)

if ($cut_idx -eq -1) {
    # Fallback: Try finding next section class
    $next_marker = 'elementor-element-6ff3863'
    $cut_idx = $contact_content.IndexOf($next_marker)
    if ($cut_idx -ne -1) {
        # Find preceding style tag
        $cut_idx = $contact_content.LastIndexOf('<style>', $cut_idx)
    }
}
else {
    # Find preceding style tag
    $cut_idx = $contact_content.LastIndexOf('<style>', $cut_idx)
}

if ($cut_idx -eq -1) {
    Write-Error "Could not find extraction point in contact.html"
    exit
}

$contact_part = $contact_content.Substring(0, $cut_idx)

# 3. Map Content
$map_html = @"
    <!-- Map Section -->
    <div class="elementor-element e-con-full e-flex e-con e-parent" data-element_type="container" style="width: 100%; height: 500px; margin-bottom: 0;">
        <div class="elementor-widget-container" style="width: 100%; height: 100%;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15198.814045934524!2d31.053028!3d-17.824858!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1931a4f00994f797%3A0xe5433066d929b775!2sHarare%2C%20Zimbabwe!5e0!3m2!1sen!2szw!4v1700000000000!5m2!1sen!2szw" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
    </div>
"@

# 4. Assemble
$final_html = $contact_part + "`n" + $map_html + "`n" + $index_part

# 5. Replacements
$final_html = $final_html.Replace('<title>About Us', '<title>Contact Us')
$final_html = $final_html.Replace('<h1 class="main-title">About Us</h1>', '<h1 class="main-title">Contact Us</h1>')

# Update Nav
$final_html = $final_html.Replace('current-menu-ancestor', '')
$final_html = $final_html.Replace('current-menu-parent', '')
$final_html = $final_html.Replace('current_page_parent', '')
$final_html = $final_html.Replace('current_page_ancestor', '')

# Remove active from About link
$final_html = $final_html.Replace('<a href="About.html" style="opacity: 1;">', '<a href="About.html">')

# 6. Save
Set-Content -Path "contact.html" -Value $final_html -Encoding UTF8

Write-Host "Success: contact.html assembled."
