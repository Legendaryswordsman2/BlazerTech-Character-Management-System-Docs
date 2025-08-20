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

def clean_and_update_toc(folder, base_path="", toc_items=None):
    """
    Recursively update TOC:
    - Add new files
    - Remove missing files
    - Preserve existing structure
    """
    if toc_items is None:
        toc_items = []

    # Gather actual files/folders in current directory
    actual_entries = sorted(os.listdir(folder))

    # --- Remove missing files from TOC ---
    cleaned_items = []
    for item in toc_items:
        if "href" in item:
            # It's a file
            if os.path.exists(os.path.join(DOCS_FOLDER, item["href"])):
                cleaned_items.append(item)  # keep if file exists
        elif "items" in item:
            # It's a folder
            folder_name = item["name"].lower()
            folder_path = os.path.join(folder, folder_name)
            if os.path.isdir(folder_path):
                # Recursively clean sub-items
                item["items"] = clean_and_update_toc(folder_path,
                                                     os.path.join(base_path, folder_name).replace("\\", "/"),
                                                     item["items"])
                cleaned_items.append(item)  # keep if folder still exists

    toc_items = cleaned_items

    # --- Add new files and folders ---
    for entry in actual_entries:
        full_path = os.path.join(folder, entry)
        relative_path = os.path.join(base_path, entry).replace("\\", "/")

        if os.path.isdir(full_path):
            folder_display = entry.capitalize()
            existing_folder = find_item_by_name(toc_items, folder_display)
            if not existing_folder:
                existing_folder = {"name": folder_display, "items": []}
                toc_items.append(existing_folder)
            existing_folder["items"] = clean_and_update_toc(full_path, relative_path, existing_folder["items"])

        elif entry.endswith(".md"):
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

# Update TOC with add/remove sync
updated_toc = clean_and_update_toc(DOCS_FOLDER, toc_items=existing_toc)

# Write updated TOC back to file
with open(TOC_FILE, "w", encoding="utf-8") as f:
    yaml.dump(updated_toc, f, sort_keys=False, allow_unicode=True)

print(f"Synchronized {TOC_FILE} with file system (added new entries, removed missing ones).")
