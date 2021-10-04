import glob
import json
import numpy as np
from PIL import Image
from PIL import ImageDraw
import os


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


class labelme2coco(object):
    def __init__(self, json_files, save_path):
        self.json_files = json_files
        self.save_path = save_path
        self.coco_data = {}
        self.images = []
        self.categories = []
        self.annotations = []
        self.labels = []
        self.height = 0
        self.width = 0
        self.transform()

    # start transform
    def transform(self):
        for num, json_file in enumerate(self.json_files):
            with open(json_file, 'r') as f:
                data = json.load(f)
                # images
                self.images.append(self.image(data, num))
                shapes = data['shapes']
                for shape in shapes:
                    # categories
                    label = shape['label']
                    if label not in self.labels:
                        self.categories.append(self.category(label))
                        self.labels.append(label)
                    # annotations
                    points = shape['points']
                    shape_type = shape['shape_type']
                    if shape_type == 'recrangle':
                        points.append(points[0][0], points[1][1])
                        points.append(points[1][0], points[0][1])
                    self.annotations.append(
                        self.annotation(points, label, num))
        # save as json
        self.coco_data['images'] = self.images
        self.coco_data['categories'] = self.categories
        self.coco_data['annotations'] = self.annotations
        json.dump(self.coco_data, open(save_path, 'w'),
                  indent=4, cls=MyEncoder)

    '''
    coco 'image', 
    which contains 'id', 'height', 'width', 'file_name'
    '''
    def image(self, data, num):
        image = {}
        image['id'] = num+1
        image['height'] = self.height = data['imageHeight']
        image['width'] = self.width = data['imageWidth']
        image['file_name'] = data['imagePath'].split('\\')[-1]      # on windows
        # image['file_name'] = data['imagePath'].split("/")[-1]     # on linux
        return image

    '''
    coco 'categories', 
    which contains 'supercategory', 'id', 'name'
    '''
    def category(self, label):
        category = {}
        category['supercategory'] = 'None'
        category['id'] = len(self.labels) + 1
        category['name'] = label
        return category

    '''
    coco 'annotations', 
    which contains 'id', 'image_id', 'category_id', 'iscrowd', 'bbox', 'segementation', 'area'
    '''
    def annotation(self, points, label, num):
        annotation = {}
        annotation['id'] = len(self.annotations)+1
        annotation['image_id'] = num+1
        annotation['category_id'] = self.label2id(label)
        annotation['iscrowd'] = 0
        annotation['segmentation'] = [list(np.asarray(points).flatten())]
        img_shape = [self.width, self.height]
        mask = self.points2mask(img_shape, points)
        annotation['bbox'] = list(map(float, self.mask2bbox(mask)))
        annotation['area'] = annotation['bbox'][2] * annotation['bbox'][3]
        return annotation

    # get categoty_id by label
    def label2id(self, label):
        for category in self.categories:
            if label == category['name']:
                return category['id']
        return 1

    # get mask by polygons
    def points2mask(self, img_shape, points):
        mask = np.zeros(img_shape, dtype=np.uint8)
        mask = Image.fromarray(mask)
        xy = list(map(tuple, points))
        ImageDraw.Draw(mask).polygon(xy=xy, outline=1, fill=1)
        mask = np.array(mask)
        return mask

    # get bbox by mask
    def mask2bbox(self, mask):
        '''
        mask: [h, w], contains 0,1
        PIL axis == image axis : [w, h], contrary to array axis [h, w]
        '''
        index = np.argwhere(mask == 1)
        ys = index[:, 0]
        xs = index[:, 1]
        left_top_x = np.min(xs)
        left_top_y = np.min(ys)
        right_bottom_x = np.max(xs)
        right_bottom_y = np.max(ys)
        return [left_top_x, left_top_y, right_bottom_x-left_top_x, right_bottom_y-left_top_y]


if __name__ == "__main__":
    json_files = glob.glob("./files/*.json")
    save_path = "./coco.json"
    labelme2coco(json_files, save_path)
