# check if the two bboxes are overlap 
def is_overlap(boxa, boxb):
    ax1, ay1, ax2, ay2 = boxa
    bx1, by1, bx2, by2 = boxb

    rx = abs((ax1+ax2)/2 - (bx1+bx2)/2)
    ry = abs((ay1+ay2)/2 - (by1+by2)/2)
    wa, ha = ax2-ax1, ay2-ay1
    wb, hb = bx2-bx1, by2-by1

    if rx <= (wa+wb)/2 and ry <= (ha+hb)/2:
        return True
    else:
        return False


# calculate IoU
def iou(boxa, boxb):
    ax1, ay1, ax2, ay2 = boxa
    bx1, by1, bx2, by2 = boxb
    sa = (ax2-ax1) * (ay2-ay1)
    sb = (bx2-bx1) * (by2-by1)
    X = min(ax2, bx2) - max(ax1, bx1)
    Y = min(ay2, by2) - max(ay1, by1)
    S = X * Y
    iou = S / (sa+sb-S)
    return iou


# im: cv2 image; det: objects in one image
def show_bbox(im, det, color):
    for obj in det:
        label = obj['label']
        x1, y1, x2, y2 = obj['bbox']
        im = cv2.rectangle(im, (x1, y1), (x2, y2), color, 2)
        cv2.putText(im, label, (x1, y1-6), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, color)
    return im
