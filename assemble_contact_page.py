
import os

def assemble_contact_page():
    index_path = r"c:\Users\Lenovo\Desktop\prumac connect\index.html"
    contact_path = r"c:\Users\Lenovo\Desktop\prumac connect\contact.html"

    with open(index_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define cleanup ranges (1-based line numbers from logic, converted to 0-based indices)
    # Remove lines 780 to 3509 (inclusive of 780, exclusive of 3510)
    # Line 780 in file is index 779.
    # Line 3510 in file is index 3509.
    
    start_remove_index = 779
    end_remove_index = 3509

    # Keep lines before removal
    new_content_lines = lines[:start_remove_index]
    
    # Keep lines after removal
    new_content_lines.extend(lines[end_remove_index:])

    # Inject CSS fix for visibility in the head
    css_fix = """
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
    """
    
    # Insert CSS fix before </head>
    head_end_index = -1
    for i, line in enumerate(new_content_lines):
        if "</head>" in line:
            head_end_index = i
            break
            
    if head_end_index != -1:
        new_content_lines.insert(head_end_index, css_fix)

    # Inject JS fix for activation
    js_fix = """
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
                el.classList.add("active");
                el.classList.add("pxl-animated");
            });
        });
    </script>
    """
    
    # Insert JS fix before </body>
    body_end_index = -1
    for i, line in enumerate(new_content_lines):
        if "</body>" in line:
            body_end_index = i
            break
            
    if body_end_index != -1:
        new_content_lines.insert(body_end_index, js_fix)


    with open(contact_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content_lines)

    print(f"Created {contact_path} from {index_path} with sections removed and fixes applied.")

if __name__ == "__main__":
    assemble_contact_page()
