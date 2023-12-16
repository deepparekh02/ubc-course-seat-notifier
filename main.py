from ui import create_gui
from process import exit_processes

if __name__ == '__main__':
    try:
        create_gui()
    finally:
        exit_processes()