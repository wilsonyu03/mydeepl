# -*- coding: utf-8 -*-
import shutil


def objFileName():
    """
    生成文件名列表
    """
    # 1.存有 需要复制的文件的文件名的txt文件路径
    local_file_name_list = r'D:/2022FallDisciplineDocs/02456 Deep Learning/project/mydeepl/03-02_15.52.46/labelsandimages/labelname.txt'
    obj_name_list = []
    for i in open(local_file_name_list, 'r'):
        obj_name_list.append(i.replace('\n', ''))
    return obj_name_list


def copy_img():
    """
    复制、重命名、粘贴文件
    """
    # 2.指定含有全部文件的文件夹路径
    local_img_name = r'D:/2022FallDisciplineDocs/02456 Deep Learning/project/mydeepl/03-02_15.52.46/labelsandimages'
    # 3.指定存放复制的文件的文件夹路径
    path = r'D:/2022FallDisciplineDocs/02456 Deep Learning/project/mydeepl/03-02_15.52.46/segimages'
    for i in objFileName():
        new_obj_name = i  # 4.改成文件的格式。如图片用.jpg
        shutil.copy(local_img_name  +'/'+ new_obj_name, path + '/' + new_obj_name)


if __name__ == '__main__':
    copy_img()

