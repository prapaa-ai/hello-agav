# hello-agav

A tiny Python CLI that greets you and remembers how many times it has been run.

## What it does

- Prints a personalised greeting with the current date and time
- Keeps a run counter in a local `state.json` file
- Supports `--name` to set your name
- Supports `--reset` to clear the counter

## Setup

Install dependencies and run:

```bash
python main.py
```

## Project structure

```
main.py          CLI entry point
greeting.py      Builds the greeting string
counter.py       Reads and writes the run counter
tests/           Unit tests
```

## Contributing

This repository exists so new [Agav](https://agav.dev) users have a safe place to explore code and try small edits. Clone it and experiment!
