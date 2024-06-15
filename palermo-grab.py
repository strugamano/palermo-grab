import sys
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
from progress.bar import Bar

url = sys.argv[1]

try:
    print("\n> Preparing download...")
    page = urlopen(url)  # trying to open page
except ValueError:
    sys.exit("> Unknown URL type. Please check URL and try again!")
else:
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all("a", class_="bdl-tree-img")  # loading image links and names
    if not elements:
        sys.exit("> No downloadable content found! Please refer to the README for appropriate sites and try again!")

    with Bar(f"> Downloading...", max=len(elements)) as bar:  # downloading images to /download
        for element in elements:
            filename = element.text.strip().replace(": ", "_").replace(". ", "_").replace(" ", "_")
            urlretrieve(element['href'], "download/" + filename + ".jpeg")
            bar.next()

    sys.exit("> Done. Goodbye!")
