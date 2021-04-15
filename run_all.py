import pytest
import os
from seleniumAutoTest.conftest import REPORT_DIR
from config import RunConfig
import time


def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")

# 获取当前时间转化为固定格式
now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

# 给RunConfig.NEW_REPORT赋值
RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)

# 初始化测试报告目录
init_env(RunConfig.NEW_REPORT)

# 生成 报告路径 + 报告文件名
html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")

if __name__ =="__main__":
    print("测试已完成...等待输出测试报告")
    # 此时开始调用conftest.py文件
    # 测试用例所在路径及指定文件名
    # ‘-s’：关闭捕捉，输出打印信息
    # ‘-v’:丰富信息模式, 输出更详细的用例执行信息
    # ‘q’:减少测试的运行冗长，安静模式
    # ‘-x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例
    # ‘--html=’:生成pytest_html到指定路径下并指定文件名
    # '--maxfail':当达到最大失败数，停止执行
    # '--reruns':失败重跑次数
    pytest.main([RunConfig.cases_path,"-s","-v",
                 "--html=" + html_report,
                 "--junit-xml=" + xml_report,
                 "--self-contained-html",
                 "--maxfail", RunConfig.max_fail,
                 "--reruns", RunConfig.rerun
                 ])
