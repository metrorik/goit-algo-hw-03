from pathlib import Path
import shutil
import sys

def copy_recursiv(source: Path, destination: Path):
    # створення директорії призначення, якщо вона не існує
    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        # якщо директорія 
        if item.is_dir():
            # Пропуск рекурсиї для самої директорії призначення, щоб уникнути безкінечної рекурсії
            if item.resolve() == destination.resolve():
                continue
            copy_recursiv(item, destination / item.name)
        # інакше файл
        elif item.is_file():
            # створення піддиректорії по розширенню файла
            ext = item.suffix[1:] if item.suffix else "no_extension"
            ext_dir = destination / ext
            ext_dir.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy(item, ext_dir / item.name)
                print(f"Файл {item} скопійовано до {ext_dir}")
            except Exception as e:
                print(f"Не вдалося скопіювати файл {item}: {e}")



def main():
    if len(sys.argv) < 2:
        print("Використання: 'імя_cкрипту.py' <source_directory> <destination_directory>")
        sys.exit(1)
    
    source_dir = Path(sys.argv[1])
    dist_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Шлях {source_dir} не існує або не є директорією.")
        return
    

    print(f"Копіювання з {source_dir} до {dist_dir}...")
    copy_recursiv(source_dir, dist_dir)
    print("Копіювання завершено.")


if __name__ == "__main__":
    main()