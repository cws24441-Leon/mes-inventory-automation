# 🚀 快速开始指南

## ⚡ 一键自动配置（推荐）

### Windows 用户

1. **打开命令提示符或PowerShell**
   - 按 `Win + R`
   - 输入 `cmd` 或 `powershell`
   - 按 Enter

2. **导航到项目目录**
   ```bash
   cd C:\Users\你的用户名\Projects\mes-inventory-automation
   ```

3. **运行自动配置脚本**
   ```bash
   python setup.py
   ```
   
   或者
   
   ```bash
   setup_windows.bat
   ```

**脚本会自动：**
- ✅ 检查Python环境
- ✅ 创建虚拟环境
- ✅ 安装所有依赖
- ✅ 创建必要目录
- ✅ 配置.env文件

---

### Linux/Mac 用户

1. **打开终端**

2. **导航到项目目录**
   ```bash
   cd ~/mes-inventory-automation
   ```

3. **给脚本执行权限**
   ```bash
   chmod +x setup_linux.sh
   chmod +x check_python_linux.sh
   ```

4. **运行自动配置脚本**
   ```bash
   python3 setup.py
   ```
   
   或者
   
   ```bash
   bash setup_linux.sh
   ```

---

## ✅ 配置完成后

### 1. 配置 MES 账号信息

编辑 `.env` 文件：

```env
MES_USERNAME=205484
MES_PASSWORD=scw316620
```

### 2. 激活虚拟环境

**Windows：**
```bash
venv\Scripts\activate
```

**Linux/Mac：**
```bash
source venv/bin/activate
```

### 3. 测试运行

```bash
# 测试MES系统
python main.py

# 测试笑话生成器
cd joke_generator
python cli.py random
```

---

## 🔍 检查Python环境

### 快速检查（一键诊断）

**Windows：**
```bash
check_python_windows.bat
```

**Linux/Mac：**
```bash
bash check_python_linux.sh
```

### 手动检查

```bash
# 检查Python版本
python --version

# 检查pip版本
pip --version

# 检查Python路径
python -c "import sys; print(sys.executable)"

# 列出已安装的包
pip list
```

---

## 📋 配置脚本详解

### setup.py （推荐使用）
- ✅ 跨平台（Windows/Linux/Mac）
- ✅ Python编写，可视化进度
- ✅ 错误处理完善
- ✅ 自动升级pip

**使用：**
```bash
python setup.py
```

### setup_windows.bat
- ✅ Windows原生批处理脚本
- ✅ 无需Python即可运行
- ✅ 简单快速

**使用：**
```bash
setup_windows.bat
```

### setup_linux.sh
- ✅ Linux/Mac Shell脚本
- ✅ 自动权限处理
- ✅ 标准bash语法

**使用：**
```bash
bash setup_linux.sh
```

---

## ⚠️ 常见问题

### Q: 脚本运行失败？
A: 检查以下几点：
1. 确认Python已安装
2. Python在PATH中
3. 网络连接正常
4. 有项目目录写入权限

### Q: 如何手动安装依赖？
A: 
```bash
# 激活虚拟环境后
pip install -r requirements.txt
cd joke_generator
pip install -r requirements.txt
```

### Q: 如何使用国内镜像？
A:
```bash
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
```

### Q: 如何重新配置？
A:
```bash
# 删除虚拟环境
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# 重新运行配置脚本
python setup.py
```

---

## 📁 配置后的文件结构

```
mes-inventory-automation/
├── venv/                      # ✅ 虚拟环境
├── logs/                      # ✅ 日志目录
├── reports/                   # ✅ 报告目录
├── .env                       # ✅ 配置文件（需填写）
├── setup.py                   # 配置脚本
├── setup_windows.bat          # Windows配置脚本
├── setup_linux.sh             # Linux/Mac配置脚本
├── check_python_windows.bat   # Windows检查脚本
├── check_python_linux.sh      # Linux/Mac检查脚本
└── ...其他文件
```

---

## 🎯 接下来做什么？

1. ✅ 运行配置脚本（选择上述任一方法）
2. ✅ 编辑 `.env` 填入MES账号
3. ✅ 运行 `python main.py` 测试
4. ✅ 设置定时任务（可选）
5. ✅ 享受自动化！

---

## 📞 需要帮助？

查看完整文档：
- `README.md` - 项目文档
- `SETUP_GUIDE.md` - 详细设置指南
- `joke_generator/README.md` - 笑话生成器文档

---

**现在就开始吧！** 🚀
