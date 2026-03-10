import os
import re
from bs4 import BeautifulSoup

def main():
    desktop_dir = r"c:\Users\Lenovo\Desktop\prumac connect"
    index_path = os.path.join(desktop_dir, "index.html")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_soup = BeautifulSoup(f.read(), "html.parser")
        
    fuel_logistics_heading = index_soup.find(string=re.compile("Fuel Logistics"))
    if not fuel_logistics_heading:
        print("Error: Could not find 'Fuel Logistics' text in index.html")
        return
        
    services_section = fuel_logistics_heading.find_parent("div", class_=re.compile(r"\b(e-parent|elementor-top-section)\b"))
    
    if services_section:
        print("Found Services Section Parent:", services_section.get("class"))
        print("First 150 chars:", str(services_section)[:150])
    else:
        print("Error section not found")
        
if __name__ == "__main__":
    main()
