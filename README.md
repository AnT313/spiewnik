# Kwik
Simple songbook browser in python
## Requirements
`python3`, `PySide2`
```
pip install PySide2
```
## Usage
Run gui:
```
python3 kwik.py
```
At startup list of songs is loaded from `songs.db`. To add new song fill form with title, describtion text and chords.
Each verse of the song should start in new line (parser checks for `\n`). Chords should be formated accordingly.
For this moment songs are displayd in plaintext with each line being `text+'\t'+chords`

## Items
- `kwik.py` mainwindow widget and main 
- `adderwidget.py` addinational widget used to add new songs
- `song.py` song class
- `songs.db` storage - pickled list of song objects

## Features
- [x] browsing songs
- [x] adding new songs
- [ ] removing songs
- [ ] sorting songs
- [ ] more import formats
- [ ] nice display
- [ ] pdf export
- [ ] proper database
- [ ] web access
