# Mancala Board

A Python implementation of Mancala with a simple Pygame interface.

## Overview

This project includes a playable Mancala game using `pygame`. It supports two modes:

- **Human vs Computer**
- **Computer vs Computer**

The game logic is defined in `script.py`, while `game.py` provides the Pygame UI and mode selection.

## Prerequisites

- Python 3.8 or newer
- `pygame`

## Installation

Install `pygame` using `pip`:

```bash
pip install pygame
```

## Running the Game

From the project root, run:

```bash
python game.py
```

Then choose a mode by pressing:

- `1` for Human vs Computer
- `2` for Computer vs Computer

## Gameplay

- In **Human vs Computer** mode, click on one of your pits to make a move.
- The game continues until one side has no remaining stones in its pits.
- The winner is determined by the highest store score.

## Files

- `game.py` — Pygame user interface, input handling, and game loop.
- `script.py` — Mancala board state, rules, evaluation, and AI search logic.

## Notes

This implementation uses a basic minimax search with alpha-beta pruning for computer moves.
