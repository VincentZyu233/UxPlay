# 构建工作流

> **[📖 English](build.md)**
> **[📖 简体中文](build.zh-cn.md)**

## 📋 概述

CI 流水线由 **commit 信息中的关键词** 驱动。推送到 `master`/`main` 分支时，只需在 commit message 中包含对应关键词，GitHub Actions 就会自动开始构建。

## 🔑 关键词

| Commit 信息中的关键词 | 构建 (Windows & Linux) | 说明 |
|----------------------|:---:|:---:|
| `build action` | ✅ | 基础构建测试 |
| `build release` | ✅ | 目前功能与 build action 相同 |

> **说明:** Pull Request 始终会触发构建。PR 中 commit message 的关键词会被**忽略**。

## 🚀 用法示例

```bash
# 仅构建，验证编译
git commit --allow-empty -m "ci: test cross-compile (build action)"

# 构建（例如准备发布）
git commit -m "release: v1.7.2 (build release)"
```
