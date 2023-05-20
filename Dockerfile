FROM python:3.8.6

MAINTAINER lintong

# mkdir project path
RUN mkdir project
WORKDIR project

COPY . .
RUN ls
# 安装python依赖项
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# 对urllib3的模块进行降级，解决ssl错误
RUN pip install -U pyopenssl -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -U "urllib3<1.25" -i https://mirrors.aliyun.com/pypi/simple
# cat python soft version
RUN python -V
# cat pip list
RUN pip list show
RUN ping selenium.sucheon.com -c 4
# "-u" parameter passes at docker run
# ENTRYPOINT cd run_case && python test_run_case.py
ENTRYPOINT python test_generate_report.py -t 2