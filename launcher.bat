@echo off
REM =====================================================
REM 自动启动脚本 - Windows 专用
REM 一键启动 MES 系统或笑话生成器
REM =====================================================

setlocal enabledelayedexpansion

REM 获取脚本所在目录
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

cls

echo.
echo =====================================================
echo   启动菜单
echo =====================================================
echo.
echo 请选择要执行的操作：
echo.
echo [1] 运行 MES 库存自动化系统
echo [2] 获取笑话
echo [3] 启动笑话 Web API 服务
echo [4] 快速测试环境
echo [5] 查看运行日志
echo [6] 打开报告目录
echo [7] 退出
echo.

set /p choice=请输入选择 (1-7): 

if "%choice%"=="1" (
    call :run_mes
) else if "%choice%"=="2" (
    call :get_joke
) else if "%choice%"=="3" (
    call :start_api
) else if "%choice%"=="4" (
    call :quick_test
) else if "%choice%"=="5" (
    call :view_logs
) else if "%choice%"=="6" (
    call :open_reports
) else if "%choice%"=="7" (
    echo 再见！
    exit /b 0
) else (
    echo 无效的选择
    pause
    exit /b 1
)

goto end

REM =============== 运行 MES 系统 ===============
:run_mes
echo.
echo 激活虚拟环境并运行 MES 系统...
echo.
call venv\Scripts\activate.bat
python main.py
if errorlevel 1 (
    echo.
    echo ❌ MES 系统执行出错
    echo 请检查：
    echo 1. .env 文件是否配置了账号密码
    echo 2. 网络连接是否正常
    echo 3. logs/mes_automation.log 中的错误信息
)
pause
exit /b 0

REM =============== 获取笑话 ===============
:get_joke
echo.
echo 激活虚拟环境并启动笑话生成器...
echo.
call venv\Scripts\activate.bat
cd joke_generator
python cli.py random
cd ..
pause
exit /b 0

REM =============== 启动 API 服务 ===============
:start_api
echo.
echo 激活虚拟环境并启动 Web API 服务...
echo.
call venv\Scripts\activate.bat
cd joke_generator
echo.
echo ✓ API 服务即将启动...
echo 访问地址：http://localhost:5000
echo.
python api.py
cd ..
exit /b 0

REM =============== 快速测试 ===============
:quick_test
echo.
echo 运行快速测试脚本...
echo.
call quick_test.bat
exit /b 0

REM =============== 查看日志 ===============
:view_logs
echo.
echo 正在打开日志文件...
echo.
if exist "logs\mes_automation.log" (
    notepad logs\mes_automation.log
) else (
    echo ❌ 日志文件不存在
    echo 请先运行 MES 系统
    pause
)
exit /b 0

REM =============== 打开报告目录 ===============
:open_reports
echo.
echo 正在打开报告目录...
echo.
if exist "reports\" (
    start explorer.exe reports\
) else (
    echo ❌ 报告目录不存在
    pause
)
exit /b 0

:end
pause
