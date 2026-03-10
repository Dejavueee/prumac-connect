$files = Get-ChildItem "c:\Users\Lenovo\Desktop\prumac connect\*.html"
foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..."
    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    # Email
    $content = $content -replace "hello@apexusglobal\.com", "info@prumacconnect.co.zw"
    
    # Phone Link
    $content = $content -replace "tel:14081234567", "tel:0775454692"
    
    # Phone Display
    $content = $content -replace "\+1\s*408\s*123\s*4567", "0775454692"
    
    # Address (Single-line regex with DOTALL equivalent handling or specific match)
    # PowerShell dot matches newline only if specified or we use (?s)
    # Using specific markers for robustness
    $addressRegex = "(?s)Apexus Inc\.<br>.*?United States"
    $newAddress = "Cnr L. Takawira <br>& J. Tongogara Ave, <br>Property Center, 2nd Floor Suite 7<br>Bulawayo"
    $content = $content -replace $addressRegex, $newAddress

    # Copyright
    $content = $content -replace "©2025\s*<a[^>]*>Apexus</a>\.\s*All rights reserved\.", "©2025 Prumac Connect. All rights reserved."
    $content = $content -replace "©2025\s*Apexus\.\s*All rights reserved\.", "©2025 Prumac Connect. All rights reserved."

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}
