# Algo Slide Formatter

## Purpose

UoB Algorithms slides have shit formatting, every step is a new slide which makes it a pain to scroll through and annotate.

This simple script removes all the redundant slides leaving you with a *clean* viewing experience.

## Installation

```
git pull git@github.com:aiden-d/algo_slide_formatter.git
```

### Usage

Navigate to the containing directory

```
cd algo_slide_formatter
```

Use the script with any algorithms slides pdf
For this example the slides are called slides.pdf and in the Mac downloads folder

```
python3 slide_formatter.py ~/Downloads/slides.pdf
```

The new slides should be created in the same directory (as the initial slides) with the "_edited.pdf" suffix