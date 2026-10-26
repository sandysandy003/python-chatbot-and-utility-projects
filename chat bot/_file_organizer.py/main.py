
# Task 15: File Organizer

from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_folder(folder):
    folder = Path(folder).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("That folder does not exist.")
        return

    moved_count = 0

    for item in list(folder.iterdir()):
        if not item.is_file():
            continue

        # Skip this program and its own Python source file.
        if item.name == Path(__file__).name:
            continue

        category = get_category(item.suffix)
        destination_folder = folder / category
        destination = destination_folder / item.name

        # Avoid overwriting a file with the same name.
        if destination.exists():
            print(f"Skipped duplicate: {item.name}")
            continue

        destination_folder.mkdir(exist_ok=True)
        item.rename(destination)
        print(f"Moved: {item.name} -> {category}/")
        moved_count += 1

    print(f"\nFinished. Files organized: {moved_count}")


if __name__ == "__main__":
    print("=" * 40)
    print("FILE ORGANIZER")
    print("=" * 40)
    print("Tip: Test with a folder containing sample files first.")
    folder_path = input("Enter the folder path to organize: ").strip().strip('"')

    if folder_path:
        confirm = input(
            "This will move files. Type YES to continue: "
        ).strip()

        if confirm == "YES":
            organize_folder(folder_path)
        else:
            print("Cancelled. No files were moved.")
