# slider-qt
Sldiing Puzzle App made with PyQt6

![image](https://user-images.githubusercontent.com/53500251/218300571-df32b708-9cd5-47de-9ff3-02590d7f3c06.png)

## Basic version of app done:
- Implemented working game board, timer, scramble and reset buttons
- Best time storing

## TODO:
- Fullscreen support
- Database implementation to store solve history
- Mouse support
- Variable puzzle size (?)

## Compiling
run `pyinstaller --onefile --windowed --name "Slider" --icon "assets/icon.ico" main.py`

After compiling copy the `assets` folder and place it in the same directory with the executable

*Note for compiling on Linux:* change `self.png_path` in `gamewindow.py` to `os.path.join(full_path, "0.png")`
