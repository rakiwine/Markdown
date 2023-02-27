#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/28
# file: _os.py
# Email:
# Author: TSZ

import sys
import os

count = 0
for item in dir(os):
    if not item.startswith("_") and not item.startswith("__"):
        # print("os.{}()".format(item))
        count += 1
# print(count)

# 基本信号

##################################################
# os.O_APPEND
# os.O_BINARY
# os.O_CREAT
# os.O_EXCL
# os.O_NOINHERIT
# os.O_RANDOM
# os.O_RDONLY
# os.O_RDWR
# os.O_SEQUENTIAL
# os.O_SHORT_LIVED
# os.O_TEMPORARY
# os.O_TEXT
# os.O_TRUNC
# os.O_WRONLY

# os.SEEK_CUR
# os.SEEK_END
# os.SEEK_SET

# os.F_OK 测试path是否存在。
# os.R_OK 测试path是否可读。
# os.W_OK 测试path是否可写。
# os.X_OK 测试path是否可执行。
##################################################

# 权限相关

##################################################
# 设置当前数值权限掩码umask值并获取以前的权限掩码umask值。
# os.umask()
# os.uname_result()

# 检验权限模式
# os.access(__file__, os.F_OK)
# 如果允许访问返回 True , 否则返回 False。

# 用于路径的标记为数字标记（只支持在 Unix 下使用）
# os.chflags(path, flags)

# 更改文件所有者（只支持在 Unix 下使用）
# os.chown(path, uid, gid)

# 更改文件或目录的权限 path, mode
# os.chmod("", 0O0000)

# 更改当前进程的根目录为指定的目录
# os.chroot()
##################################################

# 系统信息相关

##################################################
# win->'nt' Linux->'posix' 输出字符串指示当前使用平台
os.name

# 检查环境的本地操作系统类型是否为字节
# os.supports_bytes_environ

# 获取系统环境变量
os.environ

# 作用 用于获取当前全局进程时间。
# 返回 nt.times_result(
#   user=0.015625,              表示用户时间。
#   system=0.0,                 表示系统时间
#   children_user=0.0,          表示所有子进程的用户时间。
#   children_system=0.0,        它表示所有子进程的系统时间。
#   elapsed=0.0                 表示从过去某个定点开始的真实时间。
# )
# os.times()

# win下为"\\" Linux下为"/" 输出操作系统特定的路径分隔符
os.sep

# 可替代的路径分隔符，在Windows中为‘/’
os.altsep

# 文件名和文件扩展名之间分隔的符号，在Windows下为‘.’
os.extsep

# win下为; Linux下为: 输出用于分割文件路径的字符串
os.pathsep

# win下为"\t\n" Linux下为"\n" 输出当前平台使用的行终止符
os.linesep

# 在Windows下为 nul，在POSIX下为‘/dev/null’。
os.devnull

# 当使用exec函数族的时候，如果没有指定PATH环境变量，则默认会查找os.defpath中的值作为子进程PATH的值。
# .;C:\bin
os.defpath

# 该方法返回一个整数值，表示系统中cpu的数量。如果cpu数量不确定，则返回None。
os.cpu_count()

# 获取一个环境变量，如果没有返回none
os.getenv("")

# 设置一个环境变量值
os.putenv("key", "value")
##################################################

# 操作相关

##################################################
# 获取当前工作目录
os.getcwd()
# 字节版本 返回当前工作目录(CWD)。
# os.getcwdb()

# 返回当前目录
os.curdir

# 获取当前目录的父目录字符串名
os.pardir

# 打开新程序 等待新程序结束 恢复进程
# os.system()

# 打开新程序 不等待新程序结束 直接进程
# os.startfile()

# 运行shell命令，直接显示 返回值0
# 分配进程
# cmd str
os.system("{} {}".format(sys.executable, r"D:\Work\Markdown\Study\pythonReview\test.py"))
# 使用的是当前进程
# python路径 任意非空字符串 py文件 参数 参数
# os.execl(path, arg0, arg1, ...)
# os.execle(path, arg0, arg1, ..., env)
# os.execlp(file, arg0, arg1, ...)
# os.execlpe(file, arg0, arg1, ..., env)
os.execl(sys.executable, "func", r"D:\Work\Markdown\Study\pythonReview\test.py", "", "")

# ‘l’和‘v\'代表传入命令行的参数设置情况，\'l\'代表固定个数的命令行参数，传入时，分别以arg0,arg1...的形式
# ’v\'代表不定个数的命令行参数，传入时，以args(列表或者元组）的形式。

# 执行程序 | 元素必须为字符串得列表 [不为空函数名, 参数1,...]
os.execv(sys.executable, ["func", "param"])
# os.execve(path, ["","",...], env)
# os.execvp(file, ["","",...])
# os.execvpe(file, ["","",...], env)

# 在新进程中执行新程序。
# mode os.P_DETACH os.P_NOWAIT os.P_NOWAITO os.P_OVERLAY os.P_WAIT
# os.spawnl(mode, path, ...)
# os.spawnle(mode, path, ..., env)
# os.spawnlp(mode, file, ...)
# os.spawnlpe(mode, file, ..., env)
##################################################

# 进程相关

##################################################
# 获取在进程的控制终端上登录的用户的名称。
# os.getlogin()

# fd(可选):文件描述符。它指定应该查询哪个文件描述符。
# fd参数的默认值为STDOUT_FILENO或标准输出。
# 返回 os.terminal_size对象
# os.get_terminal_size(fd)

# 获取启动进程时将搜索命名可执行文件的目录列表
# os.get_exec_path()

# 获取当前进程的进程ID。
# os.getpid()

# 获取当前进程的父进程ID。
# os.getppid()

# 检查指定的文件描述符是否打开并连接到tty设备
# os.isatty(fd)

# 向具有指定进程id的进程发送指定的信号
# os.kill(pid, sig)

# 创建管道。管道是将信息从一个进程传递到另一个进程的方法。它只提供单向通信，传递的信息由系统保存，直到接收进程读取。
# os.pipe()

# 从一个命令打开一个管道。
# 命令 模式默认r 缓存不设置，默认值
# os.popen(command[, mode[, bufsize]])
##################################################

# 路径相关

##################################################
# 通过自顶向下或自底向上遍历目录树生成文件名。
for (dirpath, dirnames, filename) in os.walk(r'C:\Users\hp\Desktop\apimemos', topdown=True):
    print(dirpath)
    print(dirnames)
    print(filename)

# 设置指定路径的访问和修改时间。
# os.utime(path, times =None，*，[ns，]dir_fd =None，follow_symlinks = True)

# 返回path规范化的绝对路径
os.path.abspath("")

# 将path分割成目录和文件名二元组返回
os.path.split("")
# 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.dirname("")
# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.basename("")

# 如果path存在，返回True；如果path不存在，返回False
os.path.exists("")

# 如果path是绝对路径，返回True
os.path.isabs("")

# 如果path是一个存在的文件，返回True。否则返回False
os.path.isfile("")

# 如果path是一个存在的目录，则返回True。否则返回False
os.path.isdir("")

# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.join("", "")

# 返回path所指向的文件或者目录的最后存取时间
os.path.getatime("")

# 返回path所指向的文件或者目录的最后修改时间
os.path.getmtime("")

# 返回path的大小
os.path.getsize("")

# 表示返回当前文件的上上上层目录
os.path.normpath(os.path.join(os.path.abspath(__file__), '..', '..', '..'))
##################################################

# 目录文件相关

##################################################
# src:创建硬链接的源文件路径
# dst:表示文件系统路径的类路径对象。这是创建硬链接的目标文件路径。
# src_dir_fd(可选):引用目录.的文件描述符。该参数的默认值为None。
# 如果指定的src路径是绝对路径，则忽略此参数。如果指定的src路径是相对的，而src_dir_fd不是None，那么指定的src路径相对于与src_dir_fd关联的目录。
# dst_dir_fd(可选):指向目录的文件描述符。
# follow_symlinks(可选):一个布尔值。
# os.link(src, dst, *, src_dir_fd = None, dst_dir_fd = None, follow_symlinks = True)

# 解析符号链接 symbolic link
# os.readlink(symbolic link，*，dir_fd =None)

# 创建符号链接
# os.symlink(src, dst, target_is_directory = False， *， dir_fd =None)
##################################################

# 目录相关

##################################################
# 可生成多层递归目录
os.makedirs('dirname1/dirname2')
# 生成单级目录；相当于shell中mkdirdirname
os.mkdir('dirname')

# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.removedirs('dirname1')
# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdirdirname
os.rmdir('dirname')

# 改变当前脚本工作目录
os.chdir()

# 重命名文件/目录
os.rename("oldname", "newname")
# 递归的目录或文件重命名函数
# os.renames("oldname", "die/newname")

# 重命名文件或目录。留下dst文件名 src文件内容
# os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

# 目录相关
# 获取文件/目录信息
os.stat('path/filename')

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.listdir('dirname')

# 作用 默认当前工作目录 返回对应目录的迭代器对象
# 参数 int None Union
# 返回 nt.ScandirIterator类型 迭代内容 DirEntry条目
os.scandir()

# os.DirEntry() 不能创建实例
def _DirEntry():
    DirEntry = os.DirEntry()

    # 作用 该方法返回一个整数值，表示条目的索引节点号。
    # 返回 5066549580801789
    DirEntry.inode()

    # 返回 False
    DirEntry.is_dir()

    # 返回 True
    DirEntry.is_file()

    # 作用 如果条目是符号链接，该方法返回True(即使断开)，否则返回False。
    # 返回 False
    DirEntry.is_symlink()

    # test.py
    DirEntry.name

    # .\test.py
    DirEntry.path

    # os.stat_result(
    #     st_mode=33206,                表示文件类型和文件模式位(权限)。
    #     st_ino=0,                     它表示Unix上的inode编号和Windows平台上的文件索引。
    #     st_dev=0,                     它表示该文件所在设备的标识符。
    #     st_nlink=0,                   表示硬链接的数量。
    #     st_uid=0,                     表示文件所有者的用户标识符。
    #     st_gid=0,                     表示文件所有者的组标识符。
    #     st_size=923,                  以字节为单位表示文件的大小。
    #     st_atime=1677404073,          表示最近访问的时间。它的单位是秒。
    #     st_mtime=1677404073,          表示最近的内容修改时间。它的单位是秒。
    #     st_ctime=1675674988           表示Unix上最近一次元数据更改的时间，以及Windows上的创建时间。它的单位是秒。
    # )
    # st_atime_ns: 与st_atime相同，但时间以整数形式表示，单位为纳秒。
    # st_mtime_ns: 与st_mtime相同，但时间是整数形式，以纳秒为单位。
    # st_ctime_ns: 与st_ctime相同，但时间是以纳秒为单位的整数。
    # st_blocks: 它表示为文件分配的512字节块的数量。
    # st_rdev: 如果是inode设备，则表示设备的类型。
    # st_flags: 表示用户定义的文件标志。
    DirEntry.stat()

##################################################

# 文件相关

##################################################
# 删除指定路径的文件。
os.remove()
# 删除或删除文件路径。
# os.unlink()

# 将一个字节串写入给定的文件描述符
# os.write(fd, str)

# 强制写入与给定文件描述符相关的文件。
# 写入比特字符串
# os.fsync(fd)

# 写入字符串
# fd.flush()
# os.fsync(fd.fileno())

# 从与给定文件描述符关联的文件中读取最多n个字节。
# os.read(fd, n)

# fd = os.open()
# fo = os.fdopen(fd, "w+")

# 关闭指定的文件描述符fd
# os.close()

# 关闭所有文件描述符，从fd_low(包含)到fd_high(不包含)
# os.closerange()

# 此方法返回一个字符串值，该值表示与指定文件描述符相关联的设备的编码(如果该设备连接到终端，则为None)。
# os.device_encoding(fd)

# 标准输入通常是值为0的文件描述符，标准输出通常是值为1的文件描述符，标准错误通常是值为2的文件描述符。
# 这个方法返回复制的文件描述符，它是一个整数值。
# os.dup(fd)
# fd:要复制的文件描述符。 fd2:这是文件描述符的重复值。 默认值是True 可以被子进程继承
# os.dup2(fd, fd2, inheritable = True)

# 该方法返回一个表示解码文件名的字符串。
# 文件名 = os.fsdecode("编码文件名")

# 该方法返回一个字节串，表示编码后的文件名。
# 编码文件名 = os.fsencode("文件名")

# 返回路径的文件系统表示 系统文件名
# os.fspath()

# 作用 获取文件描述符的状态。
# 返回 os.stat_result
# os.fstat(fd)
# 在某些平台上，这是fstat的别名，例如 Windows。
# os.lstat(path)

# 截断与文件描述符fd对应的文件，使其在大小上最多为长度字节。
# os.ftruncate(fd, length)
# 截断与path对应的文件，使其大小不超过长度字节。
# os.truncate(path, length)

# 获取指定文件描述符的可继承标志的值
# os.get_inheritable(fd)

# 设置指定文件描述符的可继承标志的值。
# os.set_inheritable(fd， true)

# 将文件描述符fd的当前位置设置为给定的位置pos，并通过how修改该位置。
# os.SEEK_SET或0来设置相对于文件开头的位置
# os.SEEK_CUR或1来设置相对于当前位置的位置
# os.SEEK_END或2来设置相对于文件末尾的位置
# os.lseek(fd, pos, how)
##################################################

# 其他

##################################################

# 生成一个大小为随机字节的字符串字节，适合密码学使用
# os.urandom(size)

# (1, 2, 3, 4, 5, 6)
# [WinError 4] 2: 3 -> 5
# [WinError 4] 2: 3
# [Errno 1] 2: 3
# [Errno 1] 2
# 1
# os.error()

# 获取与错误代码对应的错误消息。 code:表示错误码的整数值
# os.strerror(code)

# Python中的方法用于生成到当前进程的SIGABRT信号。
# 在Unix上，此方法产生一个核心转储，而在Windows上，该过程立即返回退出代码3
# os.abort()

# 获取有关包含给定路径的已挂载文件系统的信息
# 返回os.statvfs_result()
# os.statvfs()

# 检查一个特定的方法是否允许使用其dir_fd参数
# os.stat in os.supports_dir_fd

# 检查一个特定的方法effective_ids是否可用
# os.access in os.supports_effective_ids

# 检查是否允许将其路径参数指定为打开的文件描述符
# os.stat in os.supports_fd

# 检查os.stat()方法在本地平台上调用时是否允许使用其follow_symlinks参数
# os.stat in os.supports_follow_symlinks

# 只能在主线程中使用signal.signal
# signal.SIGCHLD表示遇到子进程退出时触发信号
# signal.signal(signal.SIGCHLD, handle_func)

# 处理僵死进程 释放进程号
def handle_func():
    # id > 0时，只等待进程ID等于pid的子进程，不管其它已经有多少子进程运行结束退出了，只要指定的子进程还没有结束, waitpid就会一直等下去；
    # pid = 0时，则获取当前进程所在进程组中的所有子进程的状态，如果子进程已经加入了别的进程组，waitpid不会对它做任何理睬。
    # pid = -1时，等待任何一个子进程退出，没有任何限制，此时waitpid和wait的作用一模一样。
    # pid < 0时，表示回收指定进程组内的任意子进程，比如 - 8888 表示回收进程组id为8888的任意子进程
    # 附：一次wait或waitpid调用只能清理掉一个子进程，清理多个子进程应该使用循环调用多次

    # os.WNOHANG，表示如果没有立即可用的子进程状态，则立即返回。在这种情况下，函数返回(0, 0)。
    # os.WUNTRACED，已停止的子进程，如果自停止以来尚未报告其当前状态，则此选项将报告这些子进程。
    cpid, status = os.waitpid(-1, os.WNOHANG)

# abc.ABCMeta类型
# os.MutableMapping

# abc.ABCMeta类型
# os.PathLike

# int类型 2147483647
# os.TMP_MAX()

# os.abc
##################################################

