import json
import numpy as np
class CoordinateSystem:
    def __init__(self,basic_vector):
        self.basic=np.array(basic_vector)  #基向量
        self.dim=len(self.basic)             #维度

    #坐标系转移（坐标转移公式）
    def transfer(self,origin_vec,origin_basic,target_basic):
        B1=np.array(origin_basic)
        B2=np.array(target_basic)
        B1_inv = np.linalg.inv(B1)      #求逆矩阵
        P = B1_inv @ B2
        p_inv = np.linalg.inv(P)
        new_vec = p_inv @ np.array(origin_vec)
        return new_vec

    #坐标投影
    def project(self,now_vec):
        B1=np.array(now_vec)
        list_projection=[]
        for i in self.basic:
            i = np.array(i)
            projection=np.dot(i,now_vec)/np.linalg.norm(i)
            list_projection.append(projection)
        return np.array(list_projection)

    #坐标夹角
    def angle(self,now_vec):
        B1=np.array(now_vec)
        len=np.linalg.norm(now_vec)
        list_angle=[]
        for i in self.basic:
            i = np.array(i)
            cos_theta = np.clip(np.dot(i,now_vec)/(np.linalg.norm(i)*len),-1.0, 1.0)
            angle=np.arccos(cos_theta)
            list_angle.append(angle)
        return np.array(list_angle)

    #坐标面积
    def scale(self):
        return abs(np.linalg.det(self.basic))

def jsonfile():
    with open("data(1).json","r",encoding="utf-8") as fp:
        task_groups = json.load(fp)      #定义一个列表存放文件数据
    for group in task_groups:
        group_name = group["group_name"]        #组名
        print(f"\n==================== {group_name} ====================")
        vectors = group["vectors"]              #需处理的向量
        ori_axis = group["ori_axis"]            #原先的维度
        tasks = group["tasks"]                  #需要完成的任务（类型为列表）
        cs=CoordinateSystem(ori_axis)           #初始化定义类（坐标系）
        current_cs = cs
        for task in tasks:
            if task["type"] == "axis_angle":
                res = [cs.angle(v) for v in vectors]
                print("向量与坐标轴夹角：")
                for i, vec_res in enumerate(res):
                    print(f"  向量{i + 1}：{vec_res}")

            elif task["type"] == "change_axis":
                target_axis = task["obj_axis"]
                res = [cs.transfer(v,cs.basic,target_axis) for v in vectors]
                current_cs=CoordinateSystem(target_axis)
                print("向量变换后坐标：")
                for i, vec_res in enumerate(res):
                    print(f"  向量{i + 1}：{np.round(vec_res, 4)}")

            elif task["type"] == "area":
                res = current_cs.scale()
                print(f"坐标系面积：{res}")

            elif task["type"] == "axis_projection" :
                res = [current_cs.project(v) for v in vectors]
                print("向量在坐标轴上的投影：")
                for i, vec_res in enumerate(res):
                    print(f"  向量{i + 1}：{vec_res}")

jsonfile()