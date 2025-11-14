# Secret-Santa-Matcher

This project is designed to generate matches for Secret Santa. Matches are chosen at random.

# Usage

``` sh
usage: matcher.py [-h] [-f FILE] [-o] [participants]
```

## Options

| Option         | Purpose                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------|
| `-f, --file`   |  Read participant list from file (default is comma-separated list). One participant per line. |
| `-o, --output` | Directory to output files. Files will be in format `{PARTICIPANT}/{PARTICIPANT}.txt`. If not used, matches will be displayed via stdout.                 |
