1:  install git and git clone to get some install package
yum install git.x86_64　
su - clouder
cd /home/clouder
git clone clouder@192.168.0.170:/home/clouder/git/robot.git


2: install python3.6

precondition: 
安装zlib　以解决安装Python3.6.3时出错问题
yum install zlib.x86_64 zlib-devel.x86_64

解决方向键乱码问题：
yum install readline-devel 
tar jxvf python-3.6.3.tar.bz2


get Python-3.6.3.tar first(A or B)
A: get it from other mathine
cd /home/clouder
mkdir tool
cd tool
scp clouder@192.168.x.x/home/clouder/tool/Python-3.6.3.tar .

B: get it from robot/files/Python-3.6.3.tar.bz2 
tar -jxvf Python-3.6.3.tar.bz2


cd Python-3.6.3
./configure --prefix=/opt/python36 --enable-shared --enable-loadable-sqlite-extensions 


vi Modules/Setup
取消167行注释：readline readline.c -lreadline -ltermcap

安装：
make
sudo make install

vi /etc/bashrc
export PATH=/opt/python36/bin:$PATH

完成后才会有pip3 or pip3.6

centos系统默认加载/usr/lib,/lib下面库文件，python默认安装到非此类文件夹。不过可以通过添加库配置信息,才能正常运行pip3

cd /etc/ld.so.conf.d
vi python3.conf
编辑 添加库文件路径 /opt/python36/lib
退出保存
ldconfig


2、安装selenium
source /etc/bashrc
pip3 install selenium

或者从本地源码进行安装：
tar xzvf selenium-3.6.0.tar.gz
cd selenium-3.6.0
sudo python3 setup.py install

