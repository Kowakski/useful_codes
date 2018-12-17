import xml.etree.ElementTree as ET
import pickle
import string
import os
import shutil
from os import listdir, getcwd
from os.path import join

sets=[('2012', 'train')]

classes = ["cat"]  #分类集，我这里是识别猫，所以是一个cat


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0        #中心点的x位置
    y = (box[2] + box[3])/2.0        #中心点的y位置
    w = box[1] - box[0]              #图片中物体的宽度
    h = box[3] - box[2]              #图片中物体的高度
    x = x*dw                         #中心点x/整个图片的宽度
    w = w*dw                         #图中物体宽度w/整个图片的宽度
    y = y*dh                         #图中物体y/整个图片的高度
    h = h*dh                         #图中高度h/整个图片的高度
    return (x,y,w,h)

def convert_annotation(image_id,flag,savepath):
    #s = '\xef\xbb\xbf'
    #nPos = image_id.index(s)
    #if nPos >= 0:
     #   image_id = image_id[3:]
    if flag == 0:
        in_file = open(savepath+'/trainImageXML/%s.xml' % (image_id))
        labeltxt = savepath+'/trainImageLabelTxt';
        if os.path.exists(labeltxt) == False:
            os.mkdir(labeltxt);
        out_file = open(savepath+'/trainImageLabelTxt/%s.txt' % (image_id), 'w')
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
    elif flag == 1:
        in_file = open(savepath+'/validateImageXML/%s.xml' % (image_id))
        labeltxt = savepath + '/validateImageLabelTxt';
        if os.path.exists(labeltxt) == False:
            os.mkdir(labeltxt);
        out_file = open(savepath+'/validateImageLabelTxt/%s.txt' % (image_id), 'w')
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)        #整张图片的宽度
        h = int(size.find('height').text)       #整张图片的高度



    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for year, image_set in sets:
    #savepath = "/home/wurui/CAR/wrz/pillar";
    savepath = os.getcwd();
    idtxt = savepath + "/validateImageId.txt";
    pathtxt = savepath + "/validateImagePath.txt";
    image_ids = open(idtxt).read().strip().split()
    list_file = open(pathtxt, 'w')
    s = '\xef\xbb\xbf'
    for image_id in image_ids:
        nPos = image_id.find(s)
        if nPos >= 0:
            image_id = image_id[3:]
        list_file.write('%s/validateImage/%s.jpg\n' % (wd, image_id))
        print(image_id)
        convert_annotation(image_id, 1, savepath)    #中间这个参数1表示是测试数据集，image_id是图片的名字-图片名
    list_file.close()

    idtxt = savepath + "/trainImageId.txt";
    pathtxt = savepath + "/trainImagePath.txt" ;
    image_ids = open(idtxt).read().strip().split()
    list_file = open(pathtxt, 'w')
    s = '\xef\xbb\xbf'
    for image_id in image_ids:
        nPos = image_id.find(s)
        if nPos >= 0:
           image_id = image_id[3:]
        list_file.write('%s/trainImage/%s.jpg\n'%(wd,image_id))
        print(image_id)
        convert_annotation(image_id,0,savepath)     #中间这个参数0表示是训练数据集
    list_file.close()

