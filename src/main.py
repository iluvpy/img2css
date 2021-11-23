import os
import sys
from PIL import Image
import numpy as np

HTML_PATH = "./index.html"
CSS_PATH = "./style.css"
STEP = 10

HTML_TEMPLATE1 = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="./style.css">
	<title>Document</title>
</head>
<body>

"""
HTML_TEMPLATE2 = """
</body>
</html>
"""

DIV_TEMPLATE = "<div class=\"{}\"></div>"
CSS_POSITION = """
position:absolute;left:{}px;top:{}px;
"""
CSS_TEMPLATE = f"""
width:{STEP}px;height:{STEP}px;
""" \
	+"background-color:rgb({},{},{});"


def create_website(img_as_array: np.ndarray) -> None:

	if os.path.exists(HTML_PATH):
		os.remove(HTML_PATH)
	if os.path.exists(CSS_PATH):
		os.remove(CSS_PATH)

	html_fd = open("index.html", "a+")
	style_fd = open("style.css", "a+")
	html_fd.write(HTML_TEMPLATE1)
	
	shape = img_as_array.shape
	for i in range(0, shape[0], STEP):
		for j in range(0, shape[1], STEP):
			class_ = f"classij{i}{j}"
			div = DIV_TEMPLATE.format(class_)
			css = "." + class_ + "{" + CSS_POSITION.format(j, i) + CSS_TEMPLATE.format(*img_as_array[i][j]) + "}"
			html_fd.write(div)
			style_fd.write(css.replace("\n", ""))
		
	html_fd.write(HTML_TEMPLATE2)
	html_fd.close()
	style_fd.close()

def main(argv) -> None:
	if len(argv) > 1:
		image_path = argv[1]
		if os.path.exists(image_path):
			image = Image.open(image_path)
		else:
			print("path doesnt exists!")
			return
		
		array = np.array(image)
		create_website(array)

if __name__ == "__main__":
	main(sys.argv)