import os
import sys

def local_main(main):
    sys.stdin = open("input.txt")
    main()


def local__entry(main_fn, filename):
    import logging
    import multiprocessing
    import pyperclip
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    # (fix) linux to reload solve()
    if sys.platform != 'win32':
        multiprocessing.set_start_method('spawn')

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger("AutoReload")
    process = None

    def start_process():
        nonlocal process
        with open(filename) as fd:
            pyperclip.copy(fd.read())
        
        process = multiprocessing.Process(target=local_main, args=[main_fn])
        process.start()

    def stop_process():
        if process:
            process.terminate()

    class event_handler(FileSystemEventHandler):
        def on_modified(self, event):
            stop_process()
            logger.info("Changed: %s", event.src_path)
            start_process()

    dir_name = os.path.dirname(__file__)

    start_process()
    observer = Observer()
    observer.schedule(event_handler(), dir_name)
    observer.start()
    observer.join()
