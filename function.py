import subprocess , multiprocessing , os
from PySide6.QtGui import QStandardItemModel , QStandardItem 
from PySide6.QtCore import Signal 
from PySide6.QtWidgets import QTableView , QHeaderView , QWidget , QVBoxLayout


file_name = ''
file_path = ''
表格数据 = ''
def start(self):
    命令列表 = 命令生成(self)
    # print(f'命令列表以创建：{命令列表}\n')
    数据 = 进程池(self,命令列表)
    
    for i in range(len(数据)):
        if type(数据[i]) == list:
            数据输出(self,数据[i])
            self.ui.echo.append(f'正在输出数据{数据[i][0]}')
        else:
            错误位置 = 数据[i].split(' ')[-1].split('.')[-1]
            self.ui.echo.append(f'{错误位置}模块执行失败')

def 命令生成(self):
    命令列表 = []
    os_name = self.ui.os_list.currentText()
    #output = f'-l {file_path}内存分析信息/'
    if os_name == 'windows':
        fun = ['windows.info','windows.hashdump','windows.cmdline','windows.pslist','windows.netscan','windows.filescan',
               'windows.mftscan','windows.sessions','windows.envars','windows.registry.hivelist','windows.registry.printkey'
               "windows.registry.printkey.PrintKey --key 'Microsoft\\Windows\\CurrentVersion\\Run --offset 0x8a8b6c9d9000'",
               "windows.registry.printkey.PrintKey --key 'Microsoft\\Windows\\CurrentVersion\\App Paths",
               "windows.registry.printkey.PrintKey --key 'Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU'",
               "windows.registry.printkey.PrintKey --key 'Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSavePidlMRU'"
               ]

        #fun = ['windows.info.Info','windows.netscan.NetScan']
    elif os_name == 'linux':
        fun = ['linux.bash','linux.pslist','linux.capabilities','linux.check_afinfo','linux.check_creds','linux.check_idt',
               'linux.check_syscall','linux.elfs','linux.envars','linux.iomem','linux.keyboard_notifiers',
               'linux.kmsg','linux.lsof','linux.mountinfo','linux.proc.Maps','linux.psaux','linux.tty_check'
               ]
    elif os_name == 'macos':
        fun = ['mac.bash','mac.check_syscall','mac.check_sysctl','mac.check_trap_table','mac.ifconfig',
               'mac.kauth_listeners','mac.kauth_scopes','mac.kevents','mac.list_files','mac.lsmod',
               'mac.lsof','mac.malfind','mac.mount','mac.netstat','mac.proc_maps.Maps','mac.psaux','mac.pslist.',
               'mac.socket_filters.','mac.timers','mac.trustedbsd','mac.vfsevents']
    for i in fun:
        命令 = f'python ./volatility3/vol.py -f "{file_name}" {i}'
        命令列表.append(命令)
    return 命令列表

def 进程池(self,命令列表):
    self.ui.echo.append('进程池已准备')
    with multiprocessing.Pool(processes=10) as pool:
        输出 = pool.map(命令执行, 命令列表)  # 使用map方法将命令列表映射到execute_command函数上，并收集结果
    return 输出 

def 命令执行(命令):
    try:
        输出 = subprocess.check_output(命令)
        标签头 = 命令.split(' ')[-1].split('.')[-1]
        数据=[标签头]
        字符串 = 输出.decode()
        分段 = 字符串.split('\r\n')
        for line in 分段:
            字段 = line.split('\t')
            if len(字段)>=2:
                数据.append(字段)
        return 数据
    except:
        return 命令
    
def 数据输出(self,数据):

    标签头 = 数据[0]
    if "OpenSavePidlMRU" in 标签头:
        标签头 = "最近使用的文件"
    elif "RunMRU" in 标签头:
        标签头 = "最近使用的程序"
    elif "App" in 标签头:
        标签头 = "已装程序"
    elif "8a8b6c9d9000" in 标签头:
        标签头 = "开机启动"

    # 创建一个tab标签页
    self.tab = QWidget()
    self.tab.setObjectName("tab")
    self.ui.tabWidget.addTab(self.tab, 标签头)
    # 在标签页里创建一个表格
    数据表 = QTableView()
    数据表.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
    数据表.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows) # 选中整行
    数据表.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)  # 列宽自适应
    tab_layout = QVBoxLayout(self.tab)
    tab_layout.addWidget(数据表)
    # 表格数据

    行数 = len(数据)-2
    列数 = len(数据[1])
    model = QStandardItemModel()   
    model.setRowCount(行数)        # 设置行数
    model.setColumnCount(列数)     # 设置列数
    model.setHorizontalHeaderLabels(数据[1])
    for row in range(行数):
        for column in range(列数):
            item = QStandardItem(数据[2:][row][column])
            model.setItem(row, column, item)
    数据表.setModel(model)

def 转储文件():
    命令 = f'python ./volatility3/vol.py -f "{file_name}" -o "{file_path}" windows.dumpfiles'
    数据提取(命令)
    
def 进程导出(self):
    try :
        pid = int(self.ui.pid_input.text())
        命令 = f'python ./volatility3/vol.py -f "{file_name}" -o "{file_path}" windows.pslist.PsList --pid {pid} --dump'
        数据提取(命令)
    except:
        self.ui.pid_input.setText('请输入正确的pid')

def 内存导出(self):
    try :
        pid = int(self.ui.pid_input.text())
        命令 = f'python ./volatility3/vol.py -f "{file_name}" -o "{file_path}" windows.menmap.Memmap --pid {pid} --dump'
        数据提取(命令)
    except:
        self.ui.pid_input.setText('请输入正确的pid')

def 数据提取(命令):
    try:
        os.system(命令)
    except:
        print('无法输出')

def 手动分析():
    os.startfile(os.path.relpath('./volatility3/使用说明.txt'))
    os.startfile(os.path.relpath('./手动分析.bat'))
    #subprocess.call('cmd /K python ./volatility3/vol.py -h',shell=True)
    # os.system("cmd /K python ./volatility3/vol.py -h")

if __name__ == "__main__":
    multiprocessing.freeze_support()
