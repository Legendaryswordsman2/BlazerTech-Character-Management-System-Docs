import os
import yaml

DOCS_FOLDER = "docs"
TOC_FILE = os.path.join(DOCS_FOLDER, "toc.yml")

def title_from_filename(filename):
    # Remove extension and replace dashes/underscores with spaces, capitalize words
    name = os.path.splitext(filename)[0]
    return " ".join(word.capitalize() for word in name.replace("_", " ").replace("-", " ").split())

def generate_toc(folder, base_path=""):
    toc = []
    for entry in sorted(os.listdir(folder)):
        full_path = os.path.join(folder, entry)
        relative_path = os.path.join(base_path, entry).replace("\\", "/")
        if os.path.isdir(full_path):
            children = generate_toc(full_path, relative_path)
            if children:
                toc.append({
                    "name": entry.capitalize(),
                    "items": children
                })
        elif entry.endswith(".md"):
            toc.append({
                "name": title_from_filename(entry),
                "href": relative_path
            })
    return toc

toc_structure = generate_toc(DOCS_FOLDER)

with open(TOC_FILE, "w", encoding="utf-8") as f:
    yaml.dump(toc_structure, f, sort_keys=False, allow_unicode=True)

print(f"Generated {TOC_FILE} successfully!")
