##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil


def moveFile(fileDir,picknumber,tarDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    # filenumber = len(pathDir)
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + '/' + name, tarDir + '/' + name)
    return

if __name__ == '__main__':


    target_root_Dir = './split_3ci'
    pos_fileDir = "./COVID_raw_image/CT_COVID"  # 源图片文件夹路径
    neg_fileDir = "./COVID_raw_image/CT_NonCOVID"  # 源图片文件夹路径
    pos_picknumber = 84
    neg_picknumber = 98
    test_pos_picknumber = 97
    test_neg_picknumber = 103

    pos = 'CT_COVID'
    neg = 'CT_NonCOVID'

    subset = ['data_covid00','data_covid01','data_covid02','data_covid-test']
    pos_neg = ['CT_COVID','CT_NonCOVID']

    for name in subset:
        if os.path.exists(target_root_Dir + '/' + name):
            continue
        else:
            os.mkdir( target_root_Dir + '/' + name )

    for root, dirs, files in os.walk(target_root_Dir):
        print(root)
        print(dirs)
        for dir in dirs:
            os.mkdir(target_root_Dir + '/' + dir + '/' + pos)
            os.mkdir(target_root_Dir + '/' + dir + '/' + neg)
        break


    for subname in subset:
        for name in pos_neg:
            dir = os.path.join(target_root_Dir, subname, name)
            print(dir)
            if 'test' in dir:
                if 'Non' in dir:
                    moveFile(neg_fileDir, test_neg_picknumber, dir)
                else:
                    moveFile(pos_fileDir, test_pos_picknumber, dir)
            elif '0' in dir:
                if 'Non' in dir:
                    moveFile(neg_fileDir, neg_picknumber, dir)
                else:
                    moveFile(pos_fileDir, pos_picknumber, dir)
            else:
                print('ERROR!')






















