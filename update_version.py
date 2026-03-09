import re
import argparse
import datetime
from pathlib import Path

def update_file_content(file_path, replacements):
    """
    读取文件，应用正则替换，如果有变化则写回。
    replacements: list of (regex_pattern, replacement_string_or_func)
    """
    path = Path(file_path)
    if not path.exists():
        print(f"⚠️  Skipping {file_path} (not found)")
        return

    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            content = path.read_text(encoding='latin-1') # fallback for some man pages if needed
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return

    original_content = content
    updated = False

    for pattern, repl in replacements:
        new_content = re.sub(pattern, repl, content)
        if new_content != content:
            content = new_content
            updated = True

    if updated:
        path.write_text(content, encoding='utf-8')
        print(f"✅ Updated {file_path}")
    else:
        print(f"   No changes for {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Update UxPlay version strings across the codebase.")
    parser.add_argument("version", help="The full version string (e.g., '1.72-zyufork.1+20260310')")
    args = parser.parse_args()

    full_version = args.version.strip()
    
    # 提取 CMake 所需的数字版本 (例如: 1.72.1 或 1.72)
    # 匹配开头的一段数字和点
    numeric_match = re.match(r'^(\d+(\.\d+)+)', full_version)
    if numeric_match:
        numeric_version = numeric_match.group(1)
    else:
        print(f"❌ Could not extract numeric version from '{full_version}'. Using 0.0.0 for CMake project().")
        numeric_version = "0.0.0"

    today_str = datetime.date.today().strftime("%Y-%m-%d")

    print(f"🚀 Updating version to: {full_version}")
    print(f"   (CMake Numeric Version: {numeric_version})")
    print(f"   (Date: {today_str})")
    print("-" * 40)

    # 1. Update CMakeLists.txt
    cmake_patterns = [
        # project( uxplay VERSION 1.72 )
        (r'(project\(\s*uxplay\s+VERSION\s+)[\d\.]+(\s*\))', fr'\g<1>{numeric_version}\g<2>'),
        # set( UXPLAY_VERSION_STRING "..." )
        (r'(set\(\s*UXPLAY_VERSION_STRING\s+")[^"]+("\s*\))', fr'\g<1>{full_version}\g<2>')
    ]
    update_file_content("CMakeLists.txt", cmake_patterns)

    # 2. Update READMES
    # # UxPlay 1.72: ... -> # UxPlay <new_ver>: ...
    readme_pattern = (r'(^# UxPlay\s+)[^\s:]+(:)', fr'\g<1>{full_version}\g<2>')
    update_file_content("README.md", [readme_pattern])
    update_file_content("README.txt", [readme_pattern])

    # 3. Update Man Pages
    # .TH UXPLAY "1" "2025-10-26" "UxPlay 1.72" "User Commands"
    # 需要更新日期和版本
    man_th_pattern = (r'(\.TH\s+\S+\s+"\d+"\s+)"[^"]*"\s+"([^"]*)"', fr'\g<1>"{today_str}" "UxPlay {full_version}"')
    
    # Description line: "UxPlay 1.72: An open-source..."
    man_desc_pattern = (r'(UxPlay\s+)[^\s:]+(:)', fr'\g<1>{full_version}\g<2>')

    man_files = [
        "uxplay.1",
        "Bluetooth_LE_beacon/dbus/uxplay-beacon.1",
        "Bluetooth_LE_beacon/winrt/uxplay-beacon.1"
    ]
    
    for mf in man_files:
        update_file_content(mf, [man_th_pattern, man_desc_pattern])

    print("-" * 40)
    print("🎉 Version update complete!")

if __name__ == "__main__":
    main()
