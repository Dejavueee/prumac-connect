
$indexPath = "c:\Users\Lenovo\Desktop\prumac connect\index.html"
$contactPath = "c:\Users\Lenovo\Desktop\prumac connect\contact.html"

$lines = Get-Content -Path $indexPath
$list = New-Object System.Collections.Generic.List[string]

# Cast parsed lines to string array to satisfy AddRange
$part1 = [string[]]$lines[0..778]
$list.AddRange($part1)

# CSS Fix
$cssFix = @"
	<style>
		/* HARD FIX FOR REQUEST QUOTE VISIBILITY */
		.elementor-element-613369c .pxl-tabs .tabs-content .tab-content {
			display: block !important;
			opacity: 1 !important;
			visibility: visible !important;
			height: auto !important;
		}

		.elementor-element-613369c .pxl-animated-waypoint,
		.elementor-element-613369c .pxl_fadeInUp {
			opacity: 1 !important;
			visibility: visible !important;
			transform: none !important;
			animation: none !important;
		}

		.elementor-element-613369c .content-inner {
			display: block !important;
			opacity: 1 !important;
		}
		
		/* Ensure the container itself is visible */
		.elementor-element-613369c {
			opacity: 1 !important;
			visibility: visible !important;
		}
	</style>
"@

# Insert CSS before </head>
$headIndex = -1
for ($i = 0; $i -lt $list.Count; $i++) {
    if ($list[$i] -match "</head>") {
        $headIndex = $i
        break
    }
}

if ($headIndex -ne -1) {
    $list.Insert($headIndex, $cssFix)
}
else {
    $list.Add($cssFix)
}

# Add Part 2
$part2 = [string[]]$lines[3509..($lines.Count - 1)]
$list.AddRange($part2)

# JS Fix
$jsFix = @"
	<script>
		document.addEventListener("DOMContentLoaded", function() {
			// Force active class on the tab content just in case
			var tabContent = document.querySelector("#907e2de-205a47e");
			if (tabContent && !tabContent.classList.contains("active")) {
				tabContent.classList.add("active");
			}
			
			// Force active on waypoints in this section
			var waypoints = document.querySelectorAll(".elementor-element-613369c .pxl-animated-waypoint");
			waypoints.forEach(function(el) {
                if (el) {
				    el.classList.add("active");
				    el.classList.add("pxl-animated");
                }
			});
		});
	</script>
"@

# Insert JS before </body>
$bodyIndex = -1
for ($i = $list.Count - 1; $i -ge 0; $i--) {
    if ($list[$i] -match "</body>") {
        $bodyIndex = $i
        break
    }
}

if ($bodyIndex -ne -1) {
    $list.Insert($bodyIndex, $jsFix)
}
else {
    $list.Add($jsFix)
}

$list | Set-Content -Path $contactPath -Encoding UTF8

Write-Host "Success: Created $contactPath"
