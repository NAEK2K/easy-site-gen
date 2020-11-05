# markdown-html-converter

## dependencies

- pip
    - markdown

## usage guide

### basic usage

`python3 mhc.py -t file.md`

the default output folder is a folder called output

### params

--targets, -targets
- space separated files containing markdown that will be converted

--output, -o
- choose the output directory

--header, -hr
- choose a header (html) that will be present on all generated pages

--footer, -f
- choose a footer (html) that will be present on all generated pages

--style, -s
- css wrapped in a style tag that will be applied to the generated html