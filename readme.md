# Algo Slide Formatter

## Purpose

UoB Algorithms slides have weird formatting, every step is a new slide which makes it a pain to scroll through and annotate (iPad, OneNote etc.).

This simple script removes all the redundant slides leaving you with a *clean* viewing experience.

The way it works is that it that the slides contain a number at the bottom which only changes when there is actually new content, the script simply collects the last of each number and combines it into a new pdf.

The algorithm content can be found [here](https://bristolalgo.github.io/courses/2022_2023_COMS10017/coms10017.html)

## Installation

``` bash
git pull git@github.com:aiden-d/algo_slide_formatter.git
```

### Usage

Navigate to the containing directory

``` bash
cd algo_slide_formatter
```

Run the script

``` bash
python3 slide_formatter.py
```

Input the file name respective to the local directory, eg: "ex/01-Introduction.pdf"

The new slides should be created in the same directory (as the initial slides) with the "_edited.pdf" suffix
