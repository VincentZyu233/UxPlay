# 开发指南 (Chinese)

## 如何修改版本号

本项目采用 `CMakeLists.txt` 作为版本号的主要定义源，但为了保持文档的一致性，发布新版本时建议同时更新以下文件。

假设我们要将版本号修改为 `1.72-zyufork.1+20260310`：

### 1. 核心构建文件 (必须修改)
这是最重要的地方，CI/CD 和 C++ 源代码都会读取这里的定义。

*   **`CMakeLists.txt`**
    *   **numeric version**: `project( uxplay VERSION 1.72 )`
        *   这里必须保持纯数字格式 (X.Y.Z)，用于 CMake 内部兼容性。
    *   **display version**: `set( UXPLAY_VERSION_STRING "1.72-zyufork.1+20260310" )`
        *   这里是实际显示的完整版本字符串。GitHub Actions 会读取这个变量来命名构建产物。

### 2. 文档与说明 (建议修改)
为了让用户看到正确的版本信息，请同步更新以下文档：

*   **`README.md`**
    *   第一行标题: `# UxPlay 1.72-zyufork...`
*   **`README.txt`**
    *   第一行标题: `# UxPlay 1.72-zyufork...`
*   **`uxplay.1` (Man Page)**
    *   `.TH UXPLAY ... "UxPlay 1.72-zyufork..."`
    *   描述部分: `UxPlay 1.72-zyufork...: An open-source...`

### 3. 辅助工具文档 (可选)
如果修改比较大，也建议更新蓝牙 Beacon 脚本相关的文档版本：

*   `Bluetooth_LE_beacon/dbus/uxplay-beacon.1`
*   `Bluetooth_LE_beacon/winrt/uxplay-beacon.1`

## 构建流程

修改完 `CMakeLists.txt` 后，提交推送到 GitHub，GitHub Actions 会自动：
1.  读取 `UXPLAY_VERSION_STRING`。
2.  构建 Windows 和 Linux 版本。
3.  生成带有版本号的 Artifact，例如: `UxPlay-Windows-x64-v1.72-zyufork.1+20260310.exe`。
