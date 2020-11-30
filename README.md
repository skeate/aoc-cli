# aoc-cli

This is a small utility to help organize and run your solutions to [Advent of
Code](http://adventofcode.com/) problems. It supports multiple languages and (if
you need it for some reason) multiple users.

## how to use

Fork this repo, run `./aoc` and start coding. When you want to run your code,
`./aoc run` will run whatever day you were editing last.

This comes with a setup for Python as an example. If you want to use other
languages, you'll need to set them up yourself. See below for details.

### cli Options

* `-y <year>`, `--year <year>` - set the year. AoC started in 2015, so it's
    gotta be at least that. Defaults to the oldest unstarted problem.
* `-d <day>`, `--day <day>` - set the day. If you set this, you also must set
    the year. A number 1-25, since it's an advent calendar thing. Defaults to
    the oldest unstarted problem.
* `-l <language>`, `--language <language>` - set the language. Defaults to
    `default_lang`
* `-u <user>`, `--user <user>` - set the user. Defaults to `default_user`.

#### examples

`./aoc -y 2016 -l haskell` will open up your `$EDITOR` with a template copied
from your `haskell` setup in `config.yml` focused on the input from year 2016,
and the day being whatever the earliest day you didn't already have a solution
for was.

`./aoc run` will run whatever your last file was. It uses `.last_run.yml` to
track this. (If that file doesn't exist, it will attempt to create a new
solution for the earliest unworked day, and then run it; admittedly not useful)

`./aoc -y 2019 -d 22 -l js -u foo run` will run the solution for 2019, day 22,
from the `js` solution folder, using the input from user `foo`.

## structure

This project is really meant to be a starting point, so it's very flexible. Do
whatever you want with it. That said, the initial structure is as follows:

* `inputs` - contains a directory for each user (as defined in `users.yml`),
    each of which contains a directory for each year, which contain files named
    like `dd.txt` where `dd` is the date.
* `solutions/<language>` - contains the solution code in the given language. Can
    also use this for any kind of runner code or utility library code you have
    (as in the included python example). Also subdivided into year directories,
    with either files or directories, depending on how you set up your templates
* `templates` - contains the templates referenced in `config.yml`. Your
    templates can be either a single file or an entire directory.

## configuration

There are two files for configuration.

### config.yml

This specifies the various language configurations, as well as the default
language (in the key `default_lang`). For each language you want to use, add
a unique key with the following parameters:

* `template`: this is the file (or directory) that will be copied for each
    problem you solve, into `solutions/<language>/<year>/<day>`. If it has
    a file extension, it will also be added to the solution file. For example,
    `template: python.py` will result in e.g. `solutions/python/2015/01.py`
* `run`: this is the command to execute when running a solution. The command
    will be passed two parameters, `-y` and `-d`, for the year and day,
    respectively. Additionally, the input will be fed into the program via
    `stdin`. For example, `run: foo` will mean `./aoc run` actually runs
    something like `cat inputs/<user>/2015/01.txt | foo -y 2015 -d 1`.

### users.yml

This file is `gitignore`d, since it will contain your session credentials and
you probably don't want to be committing those. The first time you run this
tool, it will prompt you for a name (which is mostly arbitrary) and your session
ID (which you can find in your cookies for adventofcode.com). It will then
create a `users.yml` for you, in the correct format. If you want to add more
users, just follow the pattern. If your session key expires, you might need to
update it. You can either edit `users.yml` directly, or delete it and `./aoc`
will prompt you again.
