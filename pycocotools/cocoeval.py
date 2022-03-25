'''
before using, you should install pycocotools by this command:
pip install pycocotools
'''

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

if __name__ == "__main__":
    gt = 'gt.json'
    dt = 'dt.json'
    
    cocoGt = COCO(gt)
    cocoDt = cocoGt.loadRes(dt)
    cocoEval = COCOeval(cocoGt, cocoDt, 'bbox')   # 'bbox', 'segm', 'keypoints'
    
    # if you want to change the maxDets, user the following code:
    # cocoEval.params.maxDets = [1,10,10000]

    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()
