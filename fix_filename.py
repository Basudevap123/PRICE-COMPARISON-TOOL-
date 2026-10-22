import json

nb_path = "e:/Bia project/PRICE COMPARISON TOOL 4/noeeeww2.ipynb"

try:
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    changed = False
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            new_source = []
            for line in cell["source"]:
                if 'filename = "laptop_price_comparison.csv"' in line:
                    new_source.append(line.replace('laptop_price_comparison.csv', 'laptop_price_comparison_new.csv'))
                    changed = True
                else:
                    new_source.append(line)
            cell["source"] = new_source

    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=4)
        print("Updated notebook filename successfully.")
    else:
        print("Pattern not found.")

except Exception as e:
    print(f"Error: {e}")
