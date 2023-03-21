# greektext-antoniades
## What is this?

This is the official GitHub home for Dr. Maurice A. Robinson's Greek
texts with morphological parsing and Strong's numbers.

This repo contains Dr. Robinson's New Testament Greek text of
Antoniades' 1904/1912 Patriarchal edition, with morphological parsing
tags and Strong's numbers

For more information, see the documentation files in the `textonly`
subdirectory.

We invite you to visit the official repository of the Byzantine
Majority text at: https://github.com/byztxt/byzantine-majority-text/ It was
collated by Dr. Robinson using most of the extant Greek manuscripts of the
New Testament (the Antoniades edition was created using only a few dozens of
Constantinopolitan lectionaries).

## Internet addresses?

1. https://www.byzantinetext.com

2. https://github.com/byztxt/

## License?

Public Domain. Copy freely.

## Responsible parties?

- Dr. Maurice A. Robinson, Wake Forest, North Carolina, USA is the
  primary editor.

- Jussi Ala-Konni is a contributor.

- Dr. Ulrik Sandborg-Petersen, Scripture Systems ApS, Denmark, is a
  maintainer of this repo.
  
- Norman Rodríguez, National University of Colombia, Medellín, Colombia, is a
  maintainer of this repo.

## Unicode files

The official files produced by Dr. Robinson are in the `textonly` folder
and are in a format similar to Beta code. This repo also contains a script
(located in the `scripts` folder) that converts those files to Unicode.

To use the script, run `pip install -r requirements.txt` (while in the `scripts`
folder) and then `python3 beta_to_unicode.py`. We provide copies of the generated
Unicode files in the `textonly/unicode` subfolder. The conversion script was
created by @mrgreekgeek. Should you find a bug in the script, feel free to open
an issue and tag Norman (@normansimonr).

## Maintenance?

Yes.

1. Dr. Robinson sometimes sends updates to Ulrik.

2. Should you find any errors, please open a
Github issue.
