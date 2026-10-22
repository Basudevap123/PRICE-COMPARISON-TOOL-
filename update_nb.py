import json

path = "e:/Bia project/PRICE COMPARISON TOOL 4/neww_gravity.ipynb"
try:
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # First cell is markdown
    source = nb["cells"][0]["source"]
    
    # Check if already added to avoid duplication
    if not any("Scraping Logic" in line for line in source):
        source.extend([
            "\n",
            "## Scraping Logic\n",
            "- **Selenium**: Launches a real Chrome browser to open Amazon and Flipkart. This helps load dynamic content and avoid bot detection.\n",
            "- **BeautifulSoup**: Parses the HTML code of the page to find and extract product details (Name, Price, Rating) using specific tags and classes.\n",
            "- **Data Processing**: Cleans the extracted data (removing currency symbols, etc.) and organizes it into a table for comparison."
        ])

        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=4)
        print("Notebook updated successfully.")
    else:
        print("Explanation already exists.")

except Exception as e:
    print(f"Error: {e}")
