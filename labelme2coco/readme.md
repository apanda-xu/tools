# Run as follows
(1) download [labelme2coco](https://github.com/apanda-xu/Tools/tree/main/labelme2coco) directory by [DownGit](https://www.itsvse.com/downgit/#/home)<br>
(2) 
```bash
cd labelme2coco
python labelme2coco.py
```
# COCO style
## for detection and segmentation
```json
{
    "images": [
        {
            "height": 575,
            "width": 640,
            "id": 1,
            "file_name": "1.jpg"
        }
    ],
    "categories": [
        {
            "supercategory": "Cancer",
            "id": 1,
            "name": "person"
        }
    ],
    "annotations": [
        {   
            "id": 1,
            "image_id": 1,
            "category_id": 1,
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
<!--                     ... -->
                ]
            ],
            "area": 94154.0,
            "iscrowd": 0
        }
    ]
}
```





**references**: <br>
[COCO数据集的标注格式](https://zhuanlan.zhihu.com/p/29393415)
