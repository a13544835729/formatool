import json
import os
from shutil import copy2


def cocomerge(src,dst,json_name):
    resdict = dict()
    imglist = list()
    annlist = list()
    catlist = list()

    namelist = os.listdir(src)
    for i,name in enumerate(namelist):
        srcpth=os.path.join(src,name)
        print(srcpth)
        with open(srcpth,'r') as f:
            datajson = json.load(f)
            print(datajson)

        imglist += datajson['images']
        annlist += datajson['annotations']
        catlist += datajson['categories']

    resdict['images'] = imglist
    resdict['annotations'] = annlist
    resdict['categories'] = catlist

    # print(resdict)
    dstpth=os.path.join(dst,json_name)
    print(dstpth)
    json.dump(resdict, open(dstpth, 'w'))


def imgsplit(imgsrc,imgdst,jsonpth):

    with open(jsonpth, 'r') as f:
        datajson = json.load(f)
    for item in datajson['images']:
        filename=item['file_name']
        print(filename)
        srcpth=os.path.join(imgsrc,filename)
        dstpth=os.path.join(imgdst,filename)
        copy2(srcpth,dstpth)




if __name__ == '__main__':
    # src='/home/jasonwang/Documents/worktable/XAG/dataset/rice/coco/all'
    # dst='/home/jasonwang/Documents/worktable/XAG/dataset/rice/coco'
    # cocomerge(src=src,dst=dst,json_name='rice.json')

    jsonpth = '/home/jasonwang/Documents/worktable/XAG/dataset/rice/coco/annotations/test.json'
    imgsrc = '/home/jasonwang/Documents/worktable/XAG/dataset/rice/coco/JPEGImages'
    imgdst = '/home/jasonwang/Documents/worktable/XAG/dataset/rice/coco/test'
    imgsplit(imgsrc,imgdst,jsonpth)


