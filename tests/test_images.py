import os
from bs4 import BeautifulSoup


def test_image_files_exist():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    index_path = os.path.join(repo_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    img_tags = soup.find_all("img")
    src_paths = [img.get("src") for img in img_tags if img.get("src")]

    for src in src_paths:
        assert src.startswith("images/"), f"{src} not under images/ directory"
        img_file = os.path.join(repo_root, src)
        assert os.path.isfile(img_file), f"Missing image file: {src}"

