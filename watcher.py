from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess
import os

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_event = 0

    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return

        now = time.time()
        file = os.path.basename(event.src_path)

        if now - self.last_event > 0.5:
            self.last_event = now
            print(f"\n🔄 Change detected in {file} — running debug.py")
            print("==========================================")
            try:
                python_executable = os.path.join(os.getcwd(), '.venv', 'bin', 'python')
                result = subprocess.run(
                    [python_executable, "debug.py"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(result.stdout or "(no output)")
                if result.stderr:
                    print("⚠️ ERROR:\n" + result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"⚠️ ERROR during execution:\n{e.stderr}")
            except Exception as e:
                print(f"🔥 Failed to run debug.py: {e}")
            print("==========================================\n")

if __name__ == "__main__":
    path = "."
    observer = Observer()
    handler = ChangeHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    print("👀 Watching all .py files for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watcher stopped.")
    observer.join()
