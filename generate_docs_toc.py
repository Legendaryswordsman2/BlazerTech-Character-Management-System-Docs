import os
import yaml

DOCS_FOLDER = "docs"
TOC_FILE = os.path.join(DOCS_FOLDER, "toc.yml")

def title_from_filename(filename):
    """Convert filename to a readable title."""
    name = os.path.splitext(filename)[0]
    return " ".join(word.capitalize() for word in name.replace("_", " ").replace("-", " ").split())

def find_item_by_name(items, name):
    """Find a TOC item by its name."""
    for item in items:
        if item.get("name") == name:
            return item
    return None

def update_toc(folder, base_path="", toc_items=None):
    """Recursively update TOC items based on folder contents."""
    if toc_items is None:
        toc_items = []

    for entry in sorted(os.listdir(folder)):
        full_path = os.path.join(folder, entry)
        relative_path = os.path.join(base_path, entry).replace("\\", "/")
        if os.path.isdir(full_path):
            # Look for existing folder entry
            existing_folder = find_item_by_name(toc_items, entry.capitalize())
            if not existing_folder:
                existing_folder = {"name": entry.capitalize(), "items": []}
                toc_items.append(existing_folder)
            update_toc(full_path, relative_path, existing_folder["items"])
        elif entry.endswith(".md"):
            # Check if this file is already in TOC
            if not any(item.get("href") == relative_path for item in toc_items):
                toc_items.append({
                    "name": title_from_filename(entry),
                    "href": relative_path
                })
    return toc_items

# Load existing TOC if it exists
if os.path.exists(TOC_FILE):
    with open(TOC_FILE, "r", encoding="utf-8") as f:
        existing_toc = yaml.safe_load(f) or []
else:
    existing_toc = []

# Update TOC with new files
updated_toc = update_toc(DOCS_FOLDER, toc_items=existing_toc)

# Write updated TOC back to file
with open(TOC_FILE, "w", encoding="utf-8") as f:
    yaml.dump(updated_toc, f, sort_keys=False, allow_unicode=True)

print(f"Updated {TOC_FILE} with new entries, preserving folder hierarchy!")
