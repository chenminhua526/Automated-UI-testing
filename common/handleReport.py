import os
import time
from datetime import datetime, timedelta

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
reports_dir = os.path.join(base_path, 'reports')


def get_all_reports():
    report_files = os.listdir(reports_dir)  # 获取所有报告名称
    return report_files


def delete_report():
    report_files = get_all_reports()
    time_list = []
    target_date = datetime.today().date() - timedelta(days=7)  # 获取7天前的日期
    target_date = target_date.strftime("%Y-%m-%d %H:%M:%S")   # 格式化时间
    target_time = time.strptime(target_date, "%Y-%m-%d %H:%M:%S")  # 转换为时间元组
    # print("target_time", target_time)
    timestamp = time.mktime(target_time)  # 转换为时间戳
    for i in report_files:
        file = os.path.join(reports_dir, i)
        ctime = os.path.getctime(file)
        time_list.append(ctime)
        # 如果创建时间小于目标时间，则删除该文件
        if ctime < timestamp:
            os.remove(file)


def get_new_report():
    report_files = get_all_reports()
    time_list = []
    for i in report_files:
        file = os.path.join(reports_dir, i)
        ctime = os.path.getctime(file)
        time_list.append(ctime)
    max_time = max(time_list)  # 获得最近的时间
    # print(max_time)
    index = time_list.index(max_time)
    new_report = report_files[index]  # 根据最新的创建时间得到对应的最新报告文件
    report_path = os.path.join(reports_dir, new_report)
    return report_path
