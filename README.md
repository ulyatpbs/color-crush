# Color Crush Game

A beginner programming exercise written in **December 2021** as Project 4 when first learning programming with Python.

## Purpose
A tile-matching puzzle game where players remove groups of adjacent same-colored balls. Implements file I/O, 2D list manipulation, neighbor detection algorithms, gravity mechanics, and scoring system. Includes bomb cells that clear entire rows/columns.

## Usage
```bash
python3 colorcrush.py input.txt
```

Select cells by entering `row column` coordinates. Game ends when no valid moves remain.

**Scoring:** Each color has a weight (1-9). Score = removed balls × color weight. Bombs clear rows/columns and add their total weight.
