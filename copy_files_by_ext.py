import shutil
import argparse
from pathlib import Path
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Copy and sort files by extention")
    parser.add_argument("-s", "--src", type=Path, required=True, help="Source dir path")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("output"), help="Output dir path"
    )
    return parser.parse_args()


def copy_files_by_ext(src, output):
    try:
        for file in src.iterdir():
            if file.is_dir():
                copy_files_by_ext(file, output)
            else:
                extension = file.suffix[1:]
                extension_dir = output / extension
                if not extension_dir.exists():
                    extension_dir.mkdir(parents=True, exist_ok=True)
                output_file_path = extension_dir / file.name
                shutil.copy(file, output_file_path)
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except FileNotFoundError as e:
        print(f"File or directory not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    args = parse_args()
    copy_files_by_ext(args.src, args.output)


if __name__ == "__main__":
    main()
