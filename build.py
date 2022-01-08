import os
import sys
import shutil

if sys.version_info < (3,3,):
    print("Please use Python version 3.3 or newer.")
    sys.exit(1)

if not shutil.which("marked"):
    print("Please install marked.js with the command 'npm install -g marked'.")
    sys.exit(1)

for doc in os.listdir("./markdown"):
    if os.path.isfile("markdown/" + doc):
        print("Converting Markdown File: '%s'" % doc)
        os.system("marked -o %s -i %s" % (
            "build/" + doc.replace(".md", ".html"),
            "markdown/" + doc
        ))
    else:           # Assume to be directory
        for dirdoc in os.listdir("./markdown/" + doc):
            print("Converting Markdown File: '%s'" % (doc + '/' + dirdoc))
            os.system("marked -o %s -i %s" % (
                ("build/%s/" % doc) + dirdoc.replace(".md", ".html"),
                "markdown/" + doc + '/' + dirdoc
            ))