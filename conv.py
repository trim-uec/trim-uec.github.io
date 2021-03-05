import markdown
import sys
args = sys.argv
filename = args[1]
f = open(filename, 'r')
data = f.read()
f.close
md = markdown.Markdown()
md.convert(data)
f = open("filename", 'w')
