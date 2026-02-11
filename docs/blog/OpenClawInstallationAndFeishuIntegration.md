---
title: OpenClaw Installation and Feishu Integration Guide
date: 2026-02-11
---

# OpenClaw 安装与飞书集成指南

本指南将总结 OpenClaw 的安装步骤以及如何将其与飞书进行集成。

## 1. OpenClaw CLI 安装步骤

### 1.1 系统准备 (Python & Node.js)

以下是安装 Python 和 Node.js 的步骤，为 OpenClaw 运行提供基础环境。

```bash
# 更新系统包列表
sudo apt update

# 安装通用软件属性工具
sudo apt install -y software-properties-common

# 添加 deadsnakes PPA 以获取最新 Python 版本
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# 安装 Python 3.13 及其开发工具和 pip
sudo apt install -y python3.13 python3.13-venv python3.13-dev python3-pip

# 配置 pip 使用清华大学镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 下载 Node.js (v24.13.0)
wget https://nodejs.org/dist/v24.13.0/node-v24.13.0-linux-x64.tar.xz

# 解压 Node.js 到指定目录
sudo mkdir -p /usr/local/nodejs
sudo tar -xJf node-v24.13.0-linux-x64.tar.xz -C /usr/local/nodejs

# 配置 Node.js 和 npm/npx 为全局可访问
# 方法1：软连接
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/node /usr/local/bin/node
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/npm /usr/local/bin/npm
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/npx /usr/local/bin/npx

# 方法2：添加到 PATH 环境变量 (选择其中一种方法即可)
# export PATH=/usr/local/nodejs/node-v24.13.0-linux-x64/bin:$PATH
# source ~/.bashrc

# 配置 npm 使用淘宝镜像源
npm config set registry https://registry.npmmirror.com

# 设置 npm 全局安装目录为用户可写
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 1.2 WSL (Windows Subsystem for Linux) 配置 (可选)

如果您在使用 WSL 环境，以下命令用于管理 Ubuntu 发行版：

```bash
# 查看 WSL 发行版列表
wsl --list --verbose

# 终止特定的 WSL 发行版
wsl --terminate Ubuntu-24.04

# 导出 WSL 发行版
wsl --export Ubuntu-24.04 D:\backup\ubuntu2404.tar

# 注销 WSL 发行版
wsl --unregister Ubuntu-24.04

# 创建导入目录
mkdir E:\WSL\Ubuntu2404

# 导入 WSL 发行版
wsl --import Ubuntu-24.04 E:\WSL\Ubuntu2404 E:\backup\ubuntu2404.tar --version 2

# 设置默认 WSL 发行版
wsl --setdefault Ubuntu-24.04

# 配置默认用户 (替换 <用户名>)
ubuntu2404.exe config --default-user <用户名>

# 启动/关闭 WSL
wsl --shutdown
wsl -d Ubuntu-24.04
```

### 1.3 OpenClaw CLI 安装

在完成系统准备后，可以安装 OpenClaw CLI：

```bash
# 安装最新版 OpenClaw CLI
npm install -g openclaw@latest

# 执行交互式引导设置 Gateway、工作区和技能
openclaw onboard --install-daemon
```

### 1.4 OpenClaw 验证与排障

```bash
# 查看 OpenClaw 状态、健康信息和安全审计
openclaw status
openclaw health
openclaw security audit --deep

# 重启 Gateway
openclaw gateway restart

# 访问 Gateway UI
# http://127.0.0.1:18789/?token=82eeb31b551bdbeb771e125f360549d3906610a11c20e6b0 (示例链接)

# 常见问题：配置无效
# 例如：Invalid config at /home/yofer/.openclaw/openclaw.json: - gateway.bind: Invalid input
# 此时需要检查并修正 OpenClaw 配置文件 ~/.openclaw/openclaw.json
```

## 2. OpenClaw 飞书集成

以下步骤用于将 OpenClaw 与飞书 (Feishu) 进行集成，主要用于消息通道功能。

```bash
# 安装飞书插件
# 方法1：使用 clawdbot
clawdbot plugins install @m1heng-clawd/feishu

# 方法2：使用 npm
npm install @m1heng-clawd/feishu

# 方法3：使用 openclaw plugins 命令
openclaw plugins install @m1heng-clawd/feishu

# 配置飞书通道的 App ID 和 App Secret
openclaw config set channels.feishu.appId "cli_xxxxx"
openclaw config set channels.feishu.appSecret "your_app_secret"

# 启用飞书通道
openclaw config set channels.feishu.enabled true
```

## 3. SSH 密钥生成 (可选)

```bash
# 生成 SSH 密钥对
ssh-keygen -t ed25519 -C "your_email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub

# 测试 SSH 连接到 GitHub
ssh -T git@github.com
```
