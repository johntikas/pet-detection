import os

from collections import Counter

OXFORD_PET_DIR = 'contents/models/research'


def main():
    images_dir = os.path.join(OXFORD_PET_DIR, 'images')
    xmls_dir = os.path.join(OXFORD_PET_DIR, 'annotations/xmls')

    image_folder = os.listdir('images')
    xml_folder = os.listdir('annotations/xmls')
    trimap_folder = os.listdir('annotations/trimaps')

    print('images folder items:', len(image_folder))
    print('xmls folder items:', len(xml_folder))
    print('trimaps folder items:', len(trimap_folder))

    image_names = list(filter(lambda x : x.endswith('.jpg'), image_folder))
    xml_names = list(filter(lambda x : x.endswith('.xml'), xml_folder))
    trimap_names = list(filter(lambda x : x.endswith('.png'), trimap_folder))

    print('images folder .jpg files:', len(image_names))
    print('xmls folder .xml files:', len(xml_names))
    print('trimaps folder .png files:', len(trimap_names))

    image_excl = list(filter(lambda x : not x.endswith('.jpg'), image_folder))
    xml_excl = list(filter(lambda x : not x.endswith('.xml'), xml_folder))
    trimap_excl = list(filter(lambda x : not x.endswith('.png'), trimap_folder))

    print('images folder excluded files:', image_excl)
    print('xmls folder excluded files:', xml_excl)
    print('trimaps folder excluded files:', trimap_excl)

    name_w_ext = lambda x : x.rsplit('.')[0]
    image_files_w_ext = list(map(name_w_ext, image_names))
    xml_files_w_ext = list(map(name_w_ext, xml_names))
    trimap_files_w_ext = list(map(name_w_ext, trimap_names))

    image_xml_common = set(image_files_w_ext).intersection(xml_files_w_ext)
    image_trimap_common = set(image_files_w_ext).intersection(trimap_files_w_ext)
    xml_trimap_common = set(xml_files_w_ext).intersection(trimap_files_w_ext)

    print('matched image and xml files:', len(image_xml_common))
    print('matched image and trimap files:', len(image_trimap_common))
    print('matched xml and trimap files:', len(xml_trimap_common))

    name_wt_ext = lambda x : x.rsplit('_')[0]
    image_files_wt_ext = list(map(name_wt_ext, image_names))
    xml_files_wt_ext = list(map(name_wt_ext, xml_names))
    trimap_files_wt_ext = list(map(name_wt_ext, trimap_names))

    image_cats = dict(Counter(sorted(image_files_wt_ext)))
    xml_cats = dict(Counter(sorted(xml_files_wt_ext)))
    trimap_cats = dict(Counter(sorted(trimap_files_wt_ext)))

    print(image_cats)
    print(xml_cats)
    print(trimap_cats)

if __name__ == "__main__":
    main()