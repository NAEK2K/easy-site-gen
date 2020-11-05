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

    style = ""
    if args.style:
        style = open(args.style, "r")

    html_output.write(markdown.markdown(markdown_input.read()) + "\n" + style.read())

    markdown_input.close()
    html_output.close()
    if args.style:
        style.close()
