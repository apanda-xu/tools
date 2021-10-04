## json in labelme 
labelme.json
```json
{
    "version": "4.5.9",
    "flags": {},
    "shapes": [
        {
            "label": "person",
            "points": [
                [
                    236.52941176470586,
                    112.25490196078431
                ],
                [
                    224.76470588235293,
                    120.58823529411764
                ],
                ...
            ],
            "group_id": null,
            "shape_type": "polygon",
            "flags": {}
        },
        ...
    ],
    "imagePath": "1.jpg",
    "imageData": "/9j/4AAQSkZJRgABAQAAAQABAAD...",
    "imageHeight": 575,
    "imageWidth": 640
}
```
## json in COCO
### for segmentation
coco.json
```json
{
    "images": [
        {
            "height": 575,
            "width": 640,
            "id": 1,
            "file_name": "1.jpg"
        },
        ...
    ],
    "categories": [
        {
            "supercategory": "Cancer",
            "id": 1,
            "name": "person"
        },
        ...
    ],
    "annotations": [
        {   
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "iscrowd": 0,
            "bbox": [
                48.0,
                109.0,
                263.0,
                358.0
            ],
            "segmentation": [
                [
                    236.52941176470586,
                    112.25490196078431,
                    224.76470588235293,
                    120.58823529411764,
                    ...
                ]
            ],
            "area": 94154.0
        },
        ...
    ]
}
```
### for detection
same as the json style in **segmentation** except for without "segmentation".
