$source = Get-Content "faq_source.html" -Raw -Encoding UTF8
$target = Get-Content "faq.html" -Raw -Encoding UTF8

# Extract New Content
$match = [regex]::Match($source, '(<article id="post-593".*?</article>)', [System.Text.RegularExpressions.RegexOptions]::Singleline)
if ($match.Success) {
    $newContent = $match.Groups[1].Value
}
else {
    Write-Error "Could not find article content in source."
    exit 1
}

# Replace Old Content
$pattern = '<article id="post-1849".*?</article>'
$target = [regex]::Replace($target, $pattern, $newContent, [System.Text.RegularExpressions.RegexOptions]::Singleline)

# Update Paths using Regex to avoid encoding issues with "FAQs – Apexus"
# Pattern: ./FAQs.*?Apexus_files/
$target = [regex]::Replace($target, '\./FAQs.*?Apexus_files/', './assets/')

# Update Title
$target = $target.Replace("<title>About Us - Prumac Connect</title>", "<title>FAQs - Prumac Connect</title>")

# Inject CSS
$cssLink = '<link rel="stylesheet" id="pxl-faq-css" href="./assets/css/faq.css" type="text/css" media="all">'
if ($target -notmatch "pxl-faq-css") {
    $target = $target.Replace('href="./assets/main.css" type="text/css" media="all">', 'href="./assets/main.css" type="text/css" media="all">' + "`n`t" + $cssLink)
}

# Update Navigation
$target = $target.Replace("current-menu-ancestor", "")
$target = $target.Replace("current-menu-parent", "")
$target = $target.Replace("current_page_parent", "")
$target = $target.Replace("current_page_ancestor", "")

# Fix active link
# Remove aria-current from About (case insensitive check might be needed but typically it's consistent)
$target = $target.Replace('<a href="About.html" aria-current="page">', '<a href="About.html">')
# Also check lowercase
$target = $target.Replace('<a href="about.html" aria-current="page">', '<a href="about.html">')

# Add active class to FAQ items
$target = $target.Replace('menu-item-4300">', 'menu-item-4300 current-menu-item">')
$target = $target.Replace('menu-item-864">', 'menu-item-864 current-menu-item">')

Set-Content "faq.html" $target -Encoding UTF8
Write-Host "Done."
