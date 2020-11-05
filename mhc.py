import argparse
from markdown import markdown
import os

parser = argparse.ArgumentParser(description="Arguments for MHC")
parser.add_argument("--output", "-o", default="output")
parser.add_argument("--targets", "-t", nargs="+")
parser.add_argument("--header", "-hr")
parser.add_argument("--head", "-hd")
parser.add_argument("--footer", "-f")
parser.add_argument("--style", "-s")
args = parser.parse_args()

if not args.targets:
    print("error: no target given")
    exit()

if not os.path.exists(args.output):
    os.makedirs(args.output)

header_output, head_output, footer_output, style_output = "", "", "", ""

if args.header:
    with open(args.header, "r") as f:
        header_output = f.read()

if args.head:
    with open(args.head, "r") as f:
        head_output = f.read()

if args.footer:
    with open(args.footer, "r") as f:
        footer_output = f.read()

if args.style:
    with open(args.style, "r") as f:
        style_output = f.read()

for target in args.targets:
    with open(args.output + "/" + target + ".html", "w+") as f:
        with open(target, "r") as g:
            html_output = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
                "<html>",
                head_output,
                "<body>",
                header_output,
                markdown(g.read()),
                footer_output,
                "</body>",
                style_output,
                "</html>",
            )
            f.write(html_output)
