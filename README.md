# Icon frame reference kit

A small reproducible ICO fixture and its decoded entry measurements, plus a dependency-free directory inspector. This is a file-format test kit, not an operating-system compatibility certification.

The original measurements and browser tools are documented at https://icoforge.com/ico-to-png.

## Inspect a local ICO

Run `python inspect_ico.py sample.ico`. The script checks the directory bounds, reports PNG or DIB encoding, and prints a SHA-256 for each exact stored payload. It does not execute, install or upload the input.

## Included fixture

`sample.ico` contains four PNG-encoded entries (16, 32, 48 and 256 pixels). `MEASUREMENTS.json` records the actual extraction test dated 2026-11-06. It explicitly identifies the test as a local byte-slice and Pillow decode check, not a browser download test. All artwork is a site-created green rectangle on transparent pixels.

## Limits

The inspector validates byte ranges, not every encoding detail. A PNG signature does not prove a valid image. DIB frames require decoding before PNG export. The script does not claim byte-identical conversion for DIB data or infer display behavior from file headers.
