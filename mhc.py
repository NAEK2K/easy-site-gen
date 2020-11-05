import argparse
import markdown
import os

parser = argparse.ArgumentParser(description="Arguments for MHC")
parser.add_argument("--output", "-o", default="output")
parser.add_argument("--targets", "-t", nargs="+")
parser.add_argument("--style", "-s")
args = parser.parse_args()

if not args.targets:
    print("error: no target given")
    exit()

if not os.path.exists(args.output):
    os.makedirs(args.output)

for target in args.targets:
    markdown_input = open(target, "r")
    html_output = open(args.output + "/" + target + ".html", "w+")

    style_output = ""
    if args.style:
        style_file = open(args.style, "r")
        style_output = style_file.read()

    html_output.write(markdown.markdown(markdown_input.read()) + "\n" + style_output)

    markdown_input.close()
    html_output.close()
    if args.style:
        style_file.close()
