#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/28
# file: _os.py
# Email:
# Author: TSZ

import os

count = 0
for item in dir(os):
    if not item.startswith("_") and not item.startswith("__"):
        # print("os.{}()".format(item))
        count += 1
# print(count)

######################################################################  权限相关

# 检验权限模式 os.access(path, mode);
# os.F_OK 测试path是否存在。
# os.R_OK 测试path是否可读。
# os.W_OK 测试path是否可写。
# os.X_OK 测试path是否可执行。
# os_access = os.access(__file__, os.F_OK)
# 如果允许访问返回 True , 否则返回 False。
# print(os_access)

# 更改文件或目录的权限 os.chmod(path, mode);
# os.chmod("", 0O0000)
# https://www.runoob.com/python/os-chmod.html

# 更改当前进程的根目录为指定的目录
# os.chroot()
# https://www.runoob.com/python/os-chroot.html

# 关闭指定的文件描述符fd
# os.close()
# https://www.runoob.com/python/os-close.html

# 关闭所有文件描述符，从fd_low(包含)到fd_high(不包含)
# os.closerange()
# https://www.runoob.com/python/os-closerange.html

######################################################################  环境变量相关

# win->'nt' Linux->'posix'
# print("输出字符串指示当前使用平台", os.name)
# win下为"\\" Linux下为"/"
# print("输出操作系统特定的路径分隔符", os.sep)
# win下为"\t\n" Linux下为"\n"
# print("输出当前平台使用的行终止符", os.linesep)
# win下为； Linux下为:
# print("输出用于分割文件路径的字符串", os.pathsep)

# print("返回当前目录 .", os.curdir)
# print("获取当前目录的父目录字符串名 ..", os.pardir)

# print("获取系统环境变量", dict(os.environ))
# print("获取一个环境变量", os.getenv(""))

# 设置一个环境变量值
# os.putenv("key", "value")

######################################################################  环境变量相关

# 运行shell命令，直接显示 返回值0
flag = os.system("dasdsad")
print("运行shell命令，直接显示", type(flag), flag)

####################################################################### 增
# 可生成多层递归目录
os.makedirs('dirname1/dirname2')
# 生成单级目录；相当于shell中mkdirdirname
os.mkdir('dirname')

####################################################################### 删
# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.removedirs('dirname1')
# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdirdirname
os.rmdir('dirname')

# 删除一个文件
os.remove()

####################################################################### 改
# --改变当前脚本工作目录
os.chdir()

# 重命名文件/目录
os.rename("oldname", "newname")

####################################################################### 查
# --获取当前工作目录
os.getcwd()

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.listdir('dirname')

# 获取文件/目录信息
os.stat('path/filename')

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

# os.defpath()
# os.cpu_count()

# os.error()
# os.execl()
# os.execle()
# os.execlp()
# os.execlpe()
# os.execv()
# os.execve()
# os.execvp()
# os.execvpe()
# os.extsep()
# os.fdopen()
# os.fsdecode()
# os.fsencode()
# os.fspath()
# os.fstat()
# os.fsync()
# os.get_exec_path()
# os.getcwdb()
# os.getlogin()
# os.getpid()
# os.getppid()
# os.isatty()
# os.kill()
# os.link()
# os.lseek()
# os.lstat()
# os.open()
# os.path()
# os.pipe()
# os.popen()
# os.read()
# os.readlink()
# os.renames()
# os.replace()
# os.times()
# os.times_result()
# os.sys()
# os.walk()
# os.write()
# os.waitpid()
# os.urandom()
# os.umask()
# os.uname_result()
# os.unlink()
# os.utime()


# os.DirEntry()
#
# os.MutableMapping()
# os.O_APPEND()
# os.O_BINARY()
# os.O_CREAT()
# os.O_EXCL()
# os.O_NOINHERIT()
# os.O_RANDOM()
# os.O_RDONLY()
# os.O_RDWR()
# os.O_SEQUENTIAL()
# os.O_SHORT_LIVED()
# os.O_TEMPORARY()
# os.O_TEXT()
# os.O_TRUNC()
# os.O_WRONLY()
# os.P_DETACH()
# os.P_NOWAIT()
# os.P_NOWAITO()
# os.P_OVERLAY()
# os.P_WAIT()
# os.PathLike()
#
# os.SEEK_CUR()
# os.SEEK_END()
# os.SEEK_SET()
# os.TMP_MAX()
#
# os._Environ()
# os._check_methods()
# os._execvpe()
# os._exists()
# os._exit()
# os._fspath()
# os._get_exports_list()
# os._putenv()
# os._unsetenv()
# os._wrap_close()
# os.abc()
# os.abort()
#
# os.altsep()
#
# os.curdir()
# os.device_encoding()
# os.devNone()
# os.dup()
# os.dup2()

# os.ftruncate()
# os.get_handle_inheritable()
# os.get_inheritable()
# os.get_terminal_size()

# os.scandir()
# os.set_handle_inheritable()
# os.set_inheritable()
# os.spawnl()
# os.spawnle()
# os.spawnv()
# os.spawnve()
# os.st()
# os.startfile()
# os.stat_result()
# os.statvfs_result()
# os.strerror()
# os.supports_bytes_environ()
# os.supports_dir_fd()
# os.supports_effective_ids()
# os.supports_fd()
# os.supports_follow_symlinks()
# os.symlink()

# os.terminal_size()

# os.truncate()



