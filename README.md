# Mnemonamer

File renamer that generates random words that can (hopefully) facilitate searching.
I created it to acces faster my memes in a huge meme folder, but I guess it can work with any type of files.

## Warning!

This program can and will rename all of the files in the specified directory. It is intended to be used on Linux. Author cannot guarantee that it will work normally on any other OS. Test or use at your own risk.

## Installation

Setup the venv

```bash
> python -m venv ./
```

Then you can just run the build script and it will generate a one-file exacutable ready for usage in the `dist/` directory.

Alternatively, you can run the commands yourself!

```bash
> source ./bin/activate

> pip install -r requirements.txt

> pyinstaller --clean -F -y -n "mnemonamer" --collect-data wonderwords main.py
```

You can, and probably should, add the executable to your PATH environmental variable, or `~.local/bin/` folder, if you use Linux

## Usage

```bash
> mnemonamer [options] PATH
```

-wc, --word-count <int> - Number of words to generate for new file name (each file - new name of <count> words)

PATH - relative or absolute to a folder (e.g "./", "./what/ever/folder/")
