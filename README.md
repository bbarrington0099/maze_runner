# Maze Runner

## Requirements

This project requires **Python 3** and the **Tkinter** library (`python3-tk`) for graphical user interface (GUI) support. Tkinter is the standard Python interface to the Tk GUI toolkit, and it comes bundled with Python, but in some cases, you may need to install it separately.

### Python 3

You will need Python 3 installed on your system to run this project. Most Linux distributions come with Python 3 pre-installed, but you can verify the installation by running the following command:

```bash
python3 --version
```

If not installed, install with the following command:
```bash
sudo apt install python3
```

No the installation can be verified with the command from before:

```bash
python3 --version
```

### Python 3 Tkinter

Tkinter is used for building GUI applications in Python. It may not be installed by default on all systems, even if Python 3 is present. You can check if Tkinter is installed by running:

```bash
python3 -m tkinter
```

If Tkinter is installed, a small window should pop up. If you get an error like ModuleNotFoundError: No module named 'tkinter', it means Tkinter is not installed, in which case you should run the following command to install:

```bash
sudo apt install python3-tk
```

No the installation can be verified with the command from before:

```bash
python3 -m tkinter
```

### Python Libraries

Proceed with installing any required libraries with the following command:

```bash
pip3 install -r requirements.txt
```