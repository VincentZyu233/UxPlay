# Build Workflow

> **[📖 English](build.md)**
> **[📖 简体中文](build.zh-cn.md)**

## 📋 Overview

The CI pipeline is driven by **commit message keywords**. Push to `master`/`main` with the right keyword and GitHub Actions will start the build process.

## 🔑 Keywords

| Keyword in commit message | Build (Windows & Linux) | Note |
|---------------------------|:---:|:---:|
| `build action` | ✅ | Basic build test |
| `build release` | ✅ | Currently same as build action |

> **Note:** Pull Requests always trigger a build. Commit message keywords are **ignored** for PRs.

## 🚀 Usage Examples

```bash
# Just build, verify compilation
git commit --allow-empty -m "ci: test cross-compile (build action)"

# Build (e.g. for a release)
git commit -m "release: v1.7.2 (build release)"
```
