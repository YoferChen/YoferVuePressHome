# OpenClaw 安装与飞书集成指南

## 🦞 什么是 OpenClaw？

OpenClaw 是一个开源的 AI 主动智能体，连接 AI 模型与本地文件和消息传递平台。它是一种自我驱动、多任务协作的 AI 系统，可以自主完成复杂的数字任务。

**前身项目**：MoltBot → Clawdbot → OpenClaw

### 核心特性
- 🔗 多平台消息集成（Telegram, WhatsApp, Discord, 飞书、微信等）
- 🧠 本地持久化记忆（任务、笔记、偏好设置）
- 🛠️ 专业技能扩展（浏览器自动化、文件操作、命令执行）
- 📦 Docker 隔离运行（安全沙箱环境）
- 🚀 支持自定义技能开发

---

## 📋 安装要求

### 系统要求
| 组件 | 最低版本 | 推荐版本 |
|------|---------|---------|
| Python | 3.13+ | 3.13.x |
| Node.js | 22+ | 24+ |
| 操作系统 | Linux/macOS/WSL2 | Ubuntu 24.04 LTS |
| pip | 最新 | 最新 |
| npm | 最新 | 最新 |

### 检查环境
```bash
# 检查 Python 版本
python3 --version  # 应该 >= 3.13

# 检查 Node.js 版本
node --version  # 应该 >= 22

# 检查 pip
pip --version

# 检查 npm
npm --version
```


---

## 🛠️ 系统准备

### 1. 安装 Python 3.13

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

# 配置 pip 使用清华大学镜像源（国内推荐）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```


### 2. 安装 Node.js

```bash
# 下载 Node.js (v24.13.0)
wget https://nodejs.org/dist/v24.13.0/node-v24.13.0-linux-x64.tar.xz

# 解压 Node.js 到指定目录
sudo mkdir -p /usr/local/nodejs
sudo tar -xJf node-v24.13.0-linux-x64.tar.xz -C /usr/local/nodejs

# 配置 Node.js 和 npm/npx 为全局可访问
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/node /usr/local/bin/node
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/npm /usr/local/bin/npm
sudo ln -s /usr/local/nodejs/node-v24.13.0-linux-x64/bin/npx /usr/local/bin/npx

# 配置 npm 使用淘宝镜像源（国内推荐）
npm config set registry https://registry.npmmirror.com

# 设置 npm 全局安装目录为用户可写
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=$HOME/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```


---

## 💻 WSL 配置 (Windows 用户可选)

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


---

## 🚀 安装 OpenClaw CLI

在完成系统准备后，安装 OpenClaw CLI：

```bash
# 安装最新版 OpenClaw CLI
npm install -g openclaw@latest

# 执行交互式引导设置 Gateway、工作区和技能
openclaw onboard --install-daemon
```

**执行 `openclaw onboard` 后会进行以下配置：**
1. Gateway 设置（消息代理）
2. 工作区配置（项目目录）
3. 技能安装（AI Agent 技能包）


---

## ⚙️ 配置与集成

### 1. 配置 Gateway

Gateway 是 OpenClaw 的消息代理服务，负责处理消息和任务分发。

```bash
# 查看 Gateway 状态
openclaw gateway status

# 重启 Gateway
openclaw gateway restart

# 访问 Gateway UI（示例）
# http://127.0.0.1:18789/?token=82eeb31b551bdbeb771e125f360549d3906610a11c20e6b0
```

### 2. 验证配置

```bash
# 查看 OpenClaw 状态、健康信息和安全审计
openclaw status
openclaw health
openclaw security audit --deep
```


---

## 📱 飞书集成

以下步骤用于将 OpenClaw 与飞书 (Feishu) 进行集成，主要用于消息通道功能。

### 安装飞书插件

```bash
# 方法1：使用 npm（推荐）
npm install @m1heng-clawd/feishu

# 方法2：使用 openclaw plugins 命令
openclaw plugins install @m1heng-clawd/feishu

# 方法3：使用 clawdbot（旧方式）
clawdbot plugins install @m1heng-clawd/feishu
```

### 配置飞书通道

```bash
# 配置飞书通道的 App ID 和 App Secret
# 替换以下内容为你的实际值
openclaw config set channels.feishu.appId "cli_xxxxx"
openclaw config set channels.feishu.appSecret "your_app_secret"

# 启用飞书通道
openclaw config set channels.feishu.enabled true
```

**获取飞书 App ID 和 App Secret：**
1. 登录 [飞书开放平台](https://open.feishu.cn/)
2. 创建应用并获取 `App ID` 和 `App Secret`
3. 配置应用权限：选择消息相关权限（如 `消息发送`、`会话消息` 等）


---

## 🔑 SSH 密钥生成 (可选)

```bash
# 生成 SSH 密钥对
ssh-keygen -t ed25519 -C "your_email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub

# 测试 SSH 连接到 GitHub
ssh -T git@github.com
```


---

## ✅ 验证与排障

### 常用命令

```bash
# 查看 OpenClaw 状态
openclaw status

# 查看 Gateway 健康状态
openclaw health

# 运行深度安全审计
openclaw security audit --deep

# 重启 Gateway 服务
openclaw gateway restart
```

### 常见问题

#### 1. 配置无效

**错误信息：**
```
Invalid config at /home/yofer/.openclaw/openclaw.json: - gateway.bind: Invalid input
```

**解决方案：**
检查并修正 OpenClaw 配置文件 `~/.openclaw/openclaw.json`，确保所有配置项格式正确。

#### 2. Gateway 无法启动

**解决方案：**
```bash
# 检查端口是否被占用
sudo netstat -tulnp | grep 18789

# 重启 Gateway
openclaw gateway restart
```

#### 3. 飞书消息推送失败

**解决方案：**
1. 检查 App ID 和 App Secret 是否正确
2. 确认飞书应用权限已配置
3. 查看日志：
   ```bash
   openclaw logs
   ```


---

## 📝 总结

### 安装步骤回顾

1. ✅ **系统准备**：安装 Python 3.13 和 Node.js 24
2. ✅ **安装 OpenClaw CLI**：使用 npm 安装
3. ✅ **配置 Gateway**：运行 `openclaw onboard`
4. ✅ **飞书集成**：安装飞书插件并配置
5. ✅ **验证**：运行 `openclaw status` 和 `openclaw health`

### 下一步

安装完成后，你可以：
- 📖 查看更多 [OpenClaw 使用指南](./OpenClawGuide.md)
- 🎓 学习 [AI Agent 技能开发](https://docs.openclaw.ai/)
- 💬 加入 [社区讨论](https://discord.gg/openclaw)


---

**文档更新日期**：2026年2月13日
**适用版本**：OpenClaw v2026.1.29+
**作者**：陈湧锋