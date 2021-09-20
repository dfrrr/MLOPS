FROM centos
RUN yum install python36 -y
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install scikit-learn
COPY SalaryData.csv /
COPY salaryapp.py /
CMD python3 salaryapp.py
