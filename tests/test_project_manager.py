import os
import setup_tests
from RTE.views.project_manager import ProjectManagerView
import tkinter as tk


if __name__ == '__main__':
    cwd = os.getcwd()
    path = os.path.join(cwd, "tests", "project")
    root = tk.Tk()
    gui = ProjectManagerView(root)
    gui.project_path = path
    gui.populate_roots()
    gui.grid(sticky="nswe")
    root.mainloop()
