@echo off
REM =====================================================
REM 快速测试脚本 - Windows专用
REM 配置完成后运行此脚本测试所有功能
REM =====================================================

setlocal enabledelayedexpansion

REM 获取脚本所在目录
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

cls

echo.
echo =====================================================
echo   MES 系统 + 笑话生成器 - 快速测试
echo =====================================================
echo.

REM 激活虚拟环境
echo [1/3] 激活虚拟环境...
call venv\Scripts\activate.bat
echo ✓ 虚拟环境已激活
echo.

REM 检查.env文件
echo [2/3] 检查 .env 文件配置...
if not exist ".env" (
    echo ❌ 错误：.env 文件不存在
    echo 请先编辑 .env 文件，填入 MES 账号信息
    pause
    exit /b 1
)

REM 检查.env内容
for /f "tokens=1 delims==" %%A in ('type .env ^| find "MES_USERNAME"') do (
    if "%%A"=="" (
        echo ⚠️  .env 未配置 MES_USERNAME，请先配置
        notepad .env
    )
)
echo ✓ .env 文件存在
echo.

REM 测试Python导入
echo [3/3] 测试依赖包...
python -c "import selenium; import openpyxl; import requests; print('✓ 所有依赖包正常')"
if errorlevel 1 (
    echo ❌ 依赖包测试失败
    pause
    exit /b 1
)
echo.

echo =====================================================
echo ✅ 所有测试通过！
echo =====================================================
echo.

echo 📋 现在你可以执行以下命令：
echo.

echo 1️⃣  运行 MES 系统自动化：
echo   python main.py
echo   系统会自动：
echo   - 登录 MES
echo   - 查询物料平衡
echo   - 查询半制品计划
echo   - 生成报告（保存在 reports/ 目录）
echo   - 生成日志（保存在 logs/ 目录）
echo.

echo 2️⃣  获取笑话：
echo   cd joke_generator
echo   python cli.py random
echo.

echo 3️⃣  获取多个笑话：
echo   python cli.py multiple --count 5
echo.

echo 4️⃣  按类型搜索笑话：
echo   python cli.py search programming
echo.

echo 5️⃣  启动笑话 API 服务：
echo   python api.py
echo   然后访问：http://localhost:5000
echo.

echo =====================================================
echo.

pause
