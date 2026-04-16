import fitz  # PyMuPDF
import os

def extract_text_and_images(pdf_path, output_folder="extracted_images"):
    doc = fitz.open(pdf_path)

    all_text = ""
    image_paths = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num, page in enumerate(doc):
        all_text += page.get_text()

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            img_path = f"{output_folder}/page{page_num}_img{img_index}.png"

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_path)

    return all_text, image_paths