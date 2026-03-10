
$index_path = "c:\Users\Lenovo\Desktop\prumac connect\index.html"
$about_path = "c:\Users\Lenovo\Desktop\prumac connect\About.html"
$target_path = "c:\Users\Lenovo\Desktop\prumac connect\contact.html"

function Get-Section($path, $start, $end) {
    $lines = Get-Content $path -Encoding UTF8
    $selected = $lines[($start - 1)..($end - 1)]
    return $selected -join "`r`n"
}

$content = @()

# 1. Head & Opening Body (index.html 1-587)
$content += Get-Section $index_path 1 587

# 2. Page & Loader Wrapper (index.html 588-600)
$content += Get-Section $index_path 588 600

# 3. Header (index.html 602-768)
$content += "`r`n`t`t<!--header-->`r`n"
$content += Get-Section $index_path 602 768

# 4. Main Content Container Opening (index.html 771-779)
$content += "`r`n`t`t<!--main content-->`r`n"
$content += Get-Section $index_path 771 779

# 5. Hero Styles (About.html 1002-1041)
$content += "`r`n`t`t`t`t`t`t`t`t<style>`r`n"
$content += Get-Section $about_path 1002 1041

# 6. Hero Section (About.html 1042-1122)
$content += Get-Section $about_path 1042 1122

# 7. Request Quote Section (index.html 3511-3860)
$content += Get-Section $index_path 3511 3860

# 8. Main Content Container Closing (index.html 3861-3868)
$content += Get-Section $index_path 3861 3868

# 9. Footer (index.html 3870-4208)
$content += "`r`n`t`t<!--Footer-->`r`n"
$content += Get-Section $index_path 3871 4208

# 10. Closing Page Wrapper & Scripts (index.html 4209-4635)
$content += Get-Section $index_path 4209 4635

$content -join "`r`n" | Out-File $target_path -Encoding UTF8
Write-Host "Successfully reconstructed $target_path"
