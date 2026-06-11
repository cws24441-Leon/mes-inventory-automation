# MES自动化脚本 - 完整配置指南

## 前置准备

### 1. 安装Python
- 下载 [Python 3.8+](https://www.python.org/downloads/)
- **重要**: 安装时勾选 "Add Python to PATH"
- 验证安装：
  ```bash
  python --version
  ```

### 2. 安装Chrome浏览器
- 下载 [Google Chrome](https://www.google.com/chrome/)
- 记住Chrome的安装位置（通常在 `C:\Program Files\Google\Chrome\Application\chrome.exe`）

### 3. 克隆项目
```bash
git clone https://github.com/cws24441-Leon/mes-inventory-automation.git
cd mes-inventory-automation
```

---

## 详细安装步骤

### 第1步：创建虚拟环境

虚拟环境用于隔离项目依赖，避免与系统其他项目冲突。

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

你会看到命令行前面出现 `(venv)` 标识。

### 第2步：安装依赖

```bash
pip install -r requirements.txt
```

等待安装完成。主要依赖包括：
- `selenium`: 浏览器自动化
- `openpyxl`: Excel文件操作
- `python-dotenv`: 环境变量管理

### 第3步：配置账号信息

#### 3.1 创建 `.env` 文件

在项目根目录复制 `.env.example` 为 `.env`：

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

#### 3.2 编辑 `.env` 文件

用任何文本编辑器打开 `.env`（推荐VS Code或记事本），输入你的MES账号：

```env
MES_USERNAME=205484
MES_PASSWORD=scw316620
```

> ⚠️ **重要**: 不要将 `.env` 文件上传到Git或分享给他人，因为它包含你的登录凭证！

---

## 测试运行

### 第1步：手动运行脚本

确保虚拟环境已激活，然后运行：

```bash
python main.py
```

### 第2步：检查输出

脚本会输出：
```
============================================================
MES库存自动化脚本启动
执行时间: 2024-01-15 09:30:45
============================================================
第1步: 加载配置...
✓ 配置加载成功
  - 部门: PCR1
  - 区域: PCR1
  - 产线: PL_Molding
第2步: 启动浏览器...
✓ 浏览器启动成功
...
```

### 第3步：查看报告

报告会保存在 `reports/` 目录：
```
reports/
├── MES库存短缺报告_20240115_093045.xlsx
└── MES库存短缺报告_20240115_093045.csv
```

### 第4步：查看日志

详细的执行日志在 `logs/mes_automation.log`：
```bash
# 查看日志（Windows）
type logs\mes_automation.log

# 查看日志（Linux/Mac）
cat logs/mes_automation.log
```

---

## 配置定时任务（Windows）

### 使用Windows任务计划程序

这样可以让脚本在指定时间自动运行，无需手动执行。

#### 步骤1：编辑 `run_daily.bat`

打开 `run_daily.bat`，将第8行改为你的项目实际路径：

```batch
set PROJECT_DIR=D:\path\to\mes-inventory-automation
```

例如，如果你的项目在 `C:\Users\YourName\Projects\mes-inventory-automation`，改为：

```batch
set PROJECT_DIR=C:\Users\YourName\Projects\mes-inventory-automation
```

#### 步骤2：打开任务计划程序

1. 按 `Win + R` 打开运行对话框
2. 输入 `taskschd.msc`
3. 按 Enter 打开任务计划程序

#### 步骤3：创建新任务

1. 在左侧"操作"面板中点击"创建任务..."
2. 在"常规"选项卡：
   - **名称**: `MES库存自动查询`
   - **描述**: `每日自动查询MES系统库存，生成短缺报告`
   - **勾选**: "使用最高权限运行"
   - **配置**: "Windows 10"（或你的系统版本）

#### 步骤4：设置触发器

1. 点击"触发器"选项卡
2. 点击"新建..."按钮
3. 配置触发器：
   - **开始任务**: 按计划
   - **重复执行**: 每天
   - **开始日期**: 今天
   - **开始时间**: 09:00:00（改成你想要的时间）
   - 点击"确定"

#### 步骤5：设置操作

1. 点击"操作"选项卡
2. 点击"新建..."按钮
3. 配置操作：
   - **操作**: 启动程序
   - **程序/脚本**: `cmd.exe`
   - **添加参数**: `/c C:\Users\YourName\Projects\mes-inventory-automation\run_daily.bat`
   - **起始于**: `C:\Users\YourName\Projects\mes-inventory-automation`
   - 点击"确定"

#### 步骤6：设置条件和设置

1. **条件**选项卡：
   - 取消勾选"仅在计算机使用交流电源时启动任务"
   - 取消勾选"只有在计算机空闲时才启动此任务"

2. **设置**选项卡：
   - ☑️ "允许按需运行任务"
   - ☑️ "如果任务已在运行，则强制停止"
   - 点击"确定"

#### 步骤7：保存并测试

1. 在任务列表中找到"MES库存自动查询"
2. 右键选择"运行"来测试
3. 打开 `reports/` 目录检查是否生成了报告

### 使用Windows计划任务的Python脚本方式

或者，你也可以不用批处理文件，直接在任务计划程序中配置Python：

**程序/脚本**:
```
C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe
```

**添加参数**:
```
C:\Users\YourName\Projects\mes-inventory-automation\main.py
```

**起始于**:
```
C:\Users\YourName\Projects\mes-inventory-automation
```

---

## 配置定时任务（Linux/Mac）

### 使用 Crontab

1. **编辑crontab**:
   ```bash
   crontab -e
   ```

2. **添加定时任务**（每天9:00执行）:
   ```bash
   0 9 * * * cd /home/user/mes-inventory-automation && /home/user/mes-inventory-automation/venv/bin/python main.py >> /home/user/mes-inventory-automation/logs/cron.log 2>&1
   ```

3. **查看已添加的任务**:
   ```bash
   crontab -l
   ```

### Crontab 时间表说明

```
分  小时  日  月  周
0   9    *   *   *
|   |    |   |   └─── 周几 (0-6, 0=周日)
|   |    |   └─────── 月份 (1-12)
|   |    └──────────── 日期 (1-31)
|   └───────────────── 小时 (0-23)
└────────────────────── 分钟 (0-59)
```

常见示例：
- `0 9 * * *` - 每天 9:00
- `0 9 * * 1-5` - 工作日 9:00
- `0 9,14 * * *` - 每天 9:00 和 14:00
- `*/30 * * * *` - 每30分钟

---

## 故障排查

### 问题1：模块未找到错误
```
ModuleNotFoundError: No module named 'selenium'
```

**解决方案**:
- 确保虚拟环境已激活
- 重新安装依赖：`pip install -r requirements.txt`

### 问题2：Chrome浏览器未找到
```
WebDriverException: unknown error: cannot find Chrome binary
```

**解决方案**:
- 确保已安装Google Chrome
- 编辑 `config.py`，自定义Chrome路径

### 问题3：登录失败
```
MES登录失败
```

**解决方案**:
- 检查 `.env` 文件中的账号密码是否正确
- 确保账号没有被锁定
- 检查网络连接

### 问题4：找不到表格元素
```
NoSuchElementException
```

**解决方案**:
- MES系统的HTML结构可能已更新
- 打开浏览器开发者工具（F12）查看实际的HTML
- 联系维护者更新爬虫脚本

### 问题5：任务计划程序无法找到项目目录
**解决方案**:
- 使用完整的绝对路径
- 检查路径是否包含中文或特殊字符（改为英文路径）
- 确保项目目录存在且有写入权限

---

## 提示与最佳实践

### 1. 路径问题
- 始终使用完整的绝对路径，避免使用相对路径
- 避免在路径中使用中文或特殊字符
- Windows路径示例：`C:\Users\YourName\Projects\mes-inventory-automation`

### 2. 账号安全
- 不要把 `.env` 文件提交到Git
- 不要在代码中硬编码密码
- 定期检查报告，发现异常立即更改密码

### 3. 任务调度
- 设置合理的执行时间，避免与其他任务冲突
- 定期检查日志，及时发现问题
- 备份重要的报告文件

### 4. 浏览器配置
- 如果需要后台运行（无窗口），编辑 `config.py`：
  ```python
  HEADLESS = True
  ```
- 如果需要调试，设置：
  ```python
  HEADLESS = False
  ```

### 5. 环境变量备份
- 妥善保管 `.env` 文件
- 建议在多台电脑上都配置一份
- 定期检查账号密码是否需要更新

---

## 获取帮助

1. **查看日志**: `logs/mes_automation.log`
2. **阅读README**: `README.md`
3. **检查代码注释**: 各个 `.py` 文件中有详细注释
4. **测试单个模块**:
   ```bash
   python mes_scraper.py
   python report_generator.py
   ```

---

## 下一步

- ✅ 完成安装和配置
- ✅ 手动测试脚本
- ✅ 设置定时任务
- ⏭️ 定期检查报告和日志
- ⏭️ 根据实际需求调整配置
- ⏭️ 考虑添加邮件通知功能

---

**祝安装顺利！** 如有问题，请查阅README.md或联系技术支持。
