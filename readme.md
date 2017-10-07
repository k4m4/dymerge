<h1 align="center">
    <img width="650" src="https://nikolaskama.me/content/images/2017/02/dymerge_small.png" alt="DyMerge Logo">
</h1>


> A simple, yet powerful tool - written purely in python - which takes given wordlists and merges them into one dynamic dictionary that can then be used as ammunition for a successful dictionary based (or bruteforce) attack.

- Compatible with Python 2.6 & 2.7.
- Author: [Nikolaos Kamarinakis](mailto:nikolaskam@gmail.com) ([nikolaskama.me](https://nikolaskama.me/))

<br>

[![Build Status](https://travis-ci.org/k4m4/dymerge.svg?branch=master)](https://travis-ci.org/k4m4/dymerge)
[![Donations Badge](https://yourdonation.rocks/images/badge.svg)](https://yourdonation.rocks)
[![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/k4m4/dymerge/blob/master/license)
[![Say Thanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/k4m4)
[![GitHub Stars](https://img.shields.io/github/stars/k4m4/dymerge.svg)](https://github.com/k4m4/dymerge/stargazers)

---

<p align="center">
    <sub>Visit <a href="https://nikolaskama.me/dymergeproject/"><code>nikolaskama.me/dymergeproject</code></a> for more information. Check out my <a href="https://nikolaskama.me">blog</a> and follow me on <a href="https://twitter.com/nikolaskama">Twitter</a>.</sub>
</p>

<br>

# Installation 

You can install DyMerge by cloning the [Git Repo](https://github.com/k4m4/dymerge):

```
~ ❯❯❯ git clone https://github.com/k4m4/dymerge.git
~ ❯❯❯ cd dymerge/
~/dymerge ❯❯❯ python dymerge.py
```

<br>

# Usage

```
Usage: python dymerge.py {dictionaries} [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output=OUTPUT_FILE
                        output filename
  -i INCLUDE_VALUES, --include=INCLUDE_VALUES
                        include specified values in dictionary
  -z ZIP_TYPE, --zip=ZIP_TYPE
                        zip file with specified archive format
  -s, --sort            sort output alphabetically
  -u, --unique          remove dictionary duplicates
  -r, --reverse         reverse dictionary items
  -f, --fast            finish task asap

Examples:
  python dymerge.py ~/dictionaries/ -s -u -o ~/powerful.txt
  python dymerge.py /usr/share/wordlists/rockyou.txt /lists/cewl.txt -s -u
  python dymerge.py /lists/cewl.txt /lists/awlg.txt -s -u -i and,this
  python dymerge.py ~/fsocity.dic -u -r -o ~/clean.txt
  python dymerge.py /dicts/crunch.txt /dicts/john.txt -u -f -z bz2
```

To view all available options run:

```
~/dymerge ❯❯❯ python dymerge.py -h
```

<br>

# Demo

Here's a short demo:

[![DyMerge Demo](https://asciinema.org/a/84067.png)](https://asciinema.org/a/84067?autoplay=1)

(For more demos click [here](https://asciinema.org/~k4m4))

<br>

# Developer

- Nikolaos Kamarinakis (k4m4) - [@nikolaskama](https://twitter.com/nikolaskama)

<br>

# License

Copyright 2016-2017 by [Nikolaos Kamarinakis](mailto:nikolaskam@gmail.com). Some rights reserved.

DyMerge is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](https://raw.githubusercontent.com/k4m4/dymerge/master/license).

<br>

For more information head over to the [official project page](https://nikolaskama.me/dymergeproject/).
You can also go ahead and email me anytime at **nikolaskam{at}gmail{dot}com**. 