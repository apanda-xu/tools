import json
import xml.etree.ElementTree as ET
import glob
import numpy as np


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


class labelimg2coco(object):
    def __init__(self, xml_files, save_path):
        self.xml_files = xml_files
        self.save_path = save_path
        self.coco_data = {}
        self.labels = []
        self.images = []
        self.categories = []
        self.annotations = []
        self.height = 0
        self.width = 0
        self.transform()

    def transform(self):
        for num, xml_file in enumerate(self.xml_files):
            root = ET.parse(xml_file)                   # get root
            self.images.append(self.image(root, num))   # images
            objects = root.findall('object')            
            for object in objects:
                # print(object.tag)
                label = object.find('name').text
                if label not in self.labels:
                    self.categories.append(self.category(label, num))
                    self.labels.append(label)
                self.annotations.append(self.annotation(object, label, num))
        # save as json
        self.coco_data['images'] = self.images
        self.coco_data['categories'] = self.categories
        self.coco_data['annotations'] = self.annotations
        json.dump(self.coco_data, open(self.save_path, 'w'),
                  indent=4, cls=MyEncoder)

    def image(self, root, num):
        image = {}
        image['id'] = num+1
        size = root.find('size')
        image['width'] = size.find('width').text
        image['height'] = size.find('height').text
        image['file_name'] = root.find('filename').text
        return image

    def category(self, label, num):
        category = {}
        category['supercategory'] = "None"
        category['id'] = len(self.labels)+1
        category['name'] = label
        return category

    def annotation(self, object, label, num):
        annotation = {}
        annotation['id'] = len(self.annotations)+1
        annotation['image_id'] = num+1
        annotation['category_id'] = self.label2id(label)
        annotation['iscrowd'] = 0
        # annotation['segmentation'] = []
        bndbox = object.find('bndbox')
        x1 = float(bndbox.find('xmin').text)
        y1 = float(bndbox.find('ymin').text)
        x2 = float(bndbox.find('xmax').text)
        y2 = float(bndbox.find('ymax').text)
        annotation['bbox'] = [x1, y1, x2-x1, y2-y1]
        annotation['area'] = annotation['bbox'][2] * annotation['bbox'][3]
        return annotation

    def label2id(self, label):
        for category in self.categories:
            if label == category['name']:
                return category['id']
        return 1


if __name__ == "__main__":
    xml_files = glob.glob("./files/*.xml")
    save_path = "./coco.json"
    labelimg2coco(xml_files, save_path)
    
