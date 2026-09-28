import os
import time
from yt_dlp import YoutubeDL

def print_header():
    print("=" * 50)
    print("      MediaHuman Audio Converter v3.120")
    print("      (C) Goose | Powered by Python 3.12")
    print("=" * 50)

def download_with_custom_progress(youtube_url: str):
    print("\n[ Анализ ссылки... ]")
    
    # Сначала просто получаем информацию о треке без скачивания
    ydl_opts_info = {
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get('title', 'Unknown Track')
            uploader = info.get('uploader', 'Unknown Artist')
    except Exception as e:
        print(f"\n[ Ошибка ] Не удалось получить данные о треке: {e}")
        return

    # === СТАДИЯ 1: Работает ровно 3 секунды ===
    print(f"\nDownload page ({title}) by ({uploader})")
    print("Soundtrack Driver 3.1 Test...")
    time.sleep(3)

    # === СТАДИЯ 2: Работает ровно 9 секунд с красивым выводом пакетов ===
    print(f"\nCollection packages ({title})")
    print(f"Collection packages by ({uploader})")
    
    # Имитируем шаги загрузки, распределенные на 9 секунд
    steps = [
        "1 MB.",
        " - 1 MB.",
        " -> 10 MB.",
        " -- 10 MB.",
        " -> 90 MB.",
        " ------------------- 90 MB.",
        " 100 MB.",
        " - 100 MB.",
        " ----------------------- 100 MB."
    ]
    
    # 9 секунд делим на количество элементов, чтобы вывод шел равномерно
    delay = 9.0 / len(steps)
    
    for step in steps:
        print(step, end="", flush=True)
        time.sleep(delay)
    print() # Перенос строки после завершения полосы загрузки

    # === ФАКТИЧЕСКОЕ СКАЧИВАНИЕ ФАЙЛА (в фоне, тихо) ===
    ydl_opts_download = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([youtube_url])
            filename = ydl.prepare_filename(info)
            print(f"\n[ Успешно! ] Один трек сохранен:")
            print(f"🎵 {filename}")
    except Exception as e:
        print(f"\n[ Ошибка при сохранении ]: {e}")

def main():
    try:
        print_header()
        url = input("Link: ").strip()
        if not url:
            print("Ошибка: Ссылка не может быть пустой!")
            return

        print("\nНажмите Enter, чтобы начать...")
        input("[ Convert ]")
        
        download_with_custom_progress(url)
        
    except Exception as main_error:
        print(f"\n[ Критическая ошибка ]: {main_error}")
    finally:
        print("\n" + "="*50)
        input("Нажмите ENTER для выхода из программы...")

if __name__ == "__main__":
    main()
