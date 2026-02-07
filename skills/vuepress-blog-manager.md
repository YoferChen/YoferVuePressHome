---
name: vuepress-blog-manager
description: 管理 VuePress 个人主页博客的专业技能。用于创建新博客板块、新增博客文章、管理资源文件、更新 projects/experiences/about/daily 等模块内容，以及本地编译验证和 GitHub 发布。触发关键词：博客、blog、文章、板块、VuePress、发布、更新博客、新增文章、侧边栏配置、config.js、genBlogSidebarConfig。适用文件类型：.md、config.js、README.md。
---

# VuePress 个人主页博客管理 Skill

这是一个用于管理 VuePress 个人主页博客的专业指导文档，帮助 AI 助手正确地更新、新增和发布博客内容。

## 项目架构概览

### 目录结构
```
docs/
├── .vuepress/
│   ├── config.js           # VuePress 配置文件（侧边栏配置）
│   ├── components/         # Vue 组件
│   ├── public/             # 静态资源（图片、图标等）
│   └── styles/             # 样式文件
├── blog/                   # 博客模块
│   ├── README.md           # 博客首页
│   ├── PyqtLearning/       # PyQt5 学习笔记
│   ├── SystemMaintenance/  # 系统维护手册
│   ├── Resources/          # 资源集合
│   └── AILearning/         # AI 学习笔记
├── about/                  # 关于页面
├── projects/               # 项目展示
├── experiences/            # 经历展示
├── article/                # 文章模块
├── daily/                  # 日常记录
│   ├── movie/              # 电影墙
│   └── photo/              # 照片墙
└── README.md               # 首页
```

### 配置文件说明
- **config.js**: 包含导航栏配置和侧边栏配置函数
  - `genBlogSidebarConfig()`: 博客侧边栏配置
  - `genDailySidebarConfig()`: 日常记录侧边栏配置
  - `genSidebarConfig()`: 通用侧边栏配置

## 功能 1: 创建新的博客板块

### 操作步骤

1. **在 `docs/blog/` 下创建新的板块文件夹**
   ```
   docs/blog/[新板块名称]/
   ```

2. **创建板块首页 README.md**
   - 参考现有板块的 README.md 格式
   - 包含板块介绍和目录链接
   - **每个文章链接后添加日期标记**，格式：`` `[YYYY-MM-DD]` ``
   - 示例格式：
   ```markdown
   # 板块标题
   
   板块简介...
   
   ## 📖 目录
   - [文章1](./文章1.md) `[2026-02-07]`
   - [文章2](./文章2.md) `[2026-02-07]`
   ```

3. **更新 `docs/.vuepress/config.js` 中的 `genBlogSidebarConfig()` 函数**
   - 在返回数组中添加新的配置对象：
   ```javascript
   {
     title: '板块标题',
     path: '/blog/[新板块名称]/',
     collapsable: false,
     children: [
       '/blog/[新板块名称]/',
       '/blog/[新板块名称]/文章1',
       '/blog/[新板块名称]/文章2',
     ],
     sidebarDepth: 3
   }
   ```

4. **更新 `docs/blog/README.md` 博客首页**
   - 在目录部分添加新板块的链接
   - 格式：`- 【日期】 :point_right:[板块名称](/YoferVuePressHome/blog/[新板块名称]):point_left: 板块描述`

## 功能 2: 新增博客文章到现有板块

### 操作步骤

1. **创建 Markdown 文件**
   - 在对应板块目录下创建 `.md` 文件
   - 文件名使用有意义的英文或拼音（避免中文）
   - 示例：`docs/blog/PyqtLearning/新文章.md`

2. **更新板块的 README.md**
   - 在目录部分添加新文章链接
   - **添加日期标记**，格式：`` `[YYYY-MM-DD]` ``
   - 格式：`- [文章标题](./文章文件名.md) \`[2026-02-07]\``
   - 日期使用文章创建日期或首次提交日期

3. **更新 `config.js` 中的侧边栏配置**
   - 找到对应板块的配置对象
   - 在 `children` 数组中添加新文章路径（不含 `.md` 扩展名）
   - 示例：
   ```javascript
   {
     title: 'PyQt5',
     path: '/blog/PyqtLearning/',
     collapsable: false,
     children: [
       '/blog/PyqtLearning/',
       '/blog/PyqtLearning/pyQt万能功能模板',
       '/blog/PyqtLearning/QSS万能样式模板',
       '/blog/PyqtLearning/新文章',  // 新增
     ],
     sidebarDepth: 3
   }
   ```

## 功能 3: 博客资源文件管理

### 资源文件存储规则

根据现有项目结构，资源文件统一使用公共资源目录：

#### 公共资源目录（标准方式）
- 使用 `docs/.vuepress/public/` 目录
- 按模块分类：
  - `docs/.vuepress/public/blog/[板块名]/` - 博客资源
  - `docs/.vuepress/public/projects/` - 项目图片
  - `docs/.vuepress/public/experiences/` - 经历图片
  - `docs/.vuepress/public/icons/` - 图标文件
- 在 Markdown 中引用：`![描述](/YoferVuePressHome/blog/[板块名]/图片名.png)`

### 资源引用格式
- **图片**: `![图片描述](/YoferVuePressHome/路径/图片名.png)`
- **注意**: 路径必须以 `/YoferVuePressHome/` 开头（对应 config.js 中的 base 配置）

## 功能 4: 更新其他模块内容

### Article 模块
- 文件：`docs/article/README.md`
- 用途：Markdown 示例和技术文档
- 更新：直接编辑 README.md 文件，保持原有格式

### Projects 模块
- 文件：`docs/projects/README.md`
- 内容：使用 `<ProjectCard>` 组件展示项目
- 更新格式：
```markdown
<ProjectCard image="/projects/项目图片.png">  
  
  **项目标题**（年份）
  
  - 项目描述1
  - 项目描述2
  
  [[网站名](链接)] [[下载](链接)] [[文档](链接)]

</ProjectCard>
```

### Experiences 模块
- 文件：`docs/experiences/README.md`
- 内容：使用 `<ExperienceCard>` 组件展示经历
- 更新格式：
```markdown
<ExperienceCard image="/experiences/图片.png">

  **标题**
  
  详细描述...
  
  [[链接1](url)] [[链接2](url)]

</ExperienceCard>
```

### About 模块
- 文件：`docs/about/README.md`
- 包含 Front Matter 配置和 `<AboutCard>` 组件
- 更新时保持 Front Matter 格式不变

### Daily 模块
- 目录：`docs/daily/`
- 子模块：`movie/`（电影墙）、`photo/`（照片墙）
- 侧边栏配置：在 `config.js` 的 `genDailySidebarConfig()` 中管理
- 更新步骤：
  1. 在对应子目录创建或更新 Markdown 文件
  2. 更新 `genDailySidebarConfig()` 函数中的 children 数组

## 功能 5: 本地编译验证与发布

### 本地编译验证

1. **安装依赖**（首次或依赖更新时）
   ```bash
   yarn install
   ```

2. **本地开发服务器**
   ```bash
   yarn docs:dev
   ```
   - 访问 `http://localhost:8080/YoferVuePressHome/`
   - 支持热重载，修改后自动刷新

3. **本地构建测试**
   ```bash
   set NODE_OPTIONS=--openssl-legacy-provider
   yarn vuepress build docs
   ```
   - 构建产物在 `dist/` 目录
   - 验证构建是否成功

### 提交代码到 GitHub

1. **查看修改状态**
   ```bash
   git status
   ```

2. **添加修改文件**
   ```bash
   git add .
   ```
   或指定文件：
   ```bash
   git add docs/blog/新板块/新文章.md
   git add docs/.vuepress/config.js
   ```

3. **提交修改**
   ```bash
   git commit -m "描述性提交信息"
   ```
   提交信息示例：
   - `feat: 新增 AI 学习笔记板块`
   - `docs: 更新 PyQt5 学习笔记`
   - `fix: 修复侧边栏配置错误`

4. **推送到 GitHub master 分支**
   ```bash
   git push origin master
   ```

### GitHub Actions 自动部署

- **工作流文件**: `.github/workflows/deploy-to-current-repo-gh_pages.yml`
- **触发条件**: 推送到 master 分支
- **部署流程**:
  1. 检出代码
  2. 安装依赖（yarn）
  3. 构建项目（`yarn vuepress build docs`）
  4. 部署到 `blog-pages` 分支
- **访问地址**: GitHub Pages 会自动从 `blog-pages` 分支发布

### 查看部署状态

1. 访问 GitHub 仓库的 Actions 标签页
2. 查看最新的工作流运行状态
3. 如果失败，查看日志排查问题

## 重要注意事项

### 路径规范
- 所有资源路径必须以 `/YoferVuePressHome/` 开头
- Markdown 文件名避免使用中文（可能导致路由问题）
- 侧边栏配置中的路径不包含 `.md` 扩展名
- **文章链接必须添加日期标记**，格式：`` `[YYYY-MM-DD]` ``

### 配置文件修改
- 修改 `config.js` 后必须重启开发服务器
- 侧边栏配置的 `children` 数组顺序决定显示顺序
- `collapsable: false` 表示侧边栏默认展开

### Markdown 编写
- 支持 KaTeX 数学公式
- 支持代码高亮
- 可以使用 Vue 组件（如 `<ProjectCard>`、`<ExperienceCard>`）

### Git 操作
- 推送前确保本地构建成功
- 提交信息要清晰描述修改内容
- 大文件（如图片）建议压缩后再提交

### 资源优化
- 图片建议压缩后上传（减小仓库体积）
- 避免上传过大的文件（> 1MB）
- 使用 WebP 格式可以获得更好的压缩比

## 常见问题排查

### 侧边栏不显示新文章
- 检查 `config.js` 中是否添加了对应路径
- 确认路径格式正确（不含 `.md` 扩展名）
- 重启开发服务器

### 图片无法显示
- 检查图片路径是否以 `/YoferVuePressHome/` 开头
- 确认图片文件已正确上传到对应目录
- 检查文件名大小写是否匹配

### 构建失败
- 查看错误日志定位问题
- 常见原因：Markdown 语法错误、路径错误、依赖缺失
- 使用 `set NODE_OPTIONS=--openssl-legacy-provider` 解决 OpenSSL 兼容性问题

### GitHub Actions 部署失败
- 检查 `ACCESS_TOKEN` 是否配置正确
- 查看 Actions 日志获取详细错误信息
- 确认 `blog-pages` 分支存在且有写入权限

## 工作流程总结

### 新增博客文章完整流程
1. 在对应板块目录创建 `.md` 文件
2. 编写文章内容，添加必要的图片资源
3. 更新板块 `README.md` 添加文章链接（**包含日期标记** `` `[YYYY-MM-DD]` ``）
4. 更新 `config.js` 侧边栏配置
5. 本地运行 `yarn docs:dev` 验证
6. 提交代码：`git add .` → `git commit -m "..."` → `git push origin master`
7. 等待 GitHub Actions 自动部署完成

### 创建新板块完整流程
1. 创建板块目录：`docs/blog/[新板块]/`
2. 创建板块首页：`docs/blog/[新板块]/README.md`（**文章链接包含日期标记**）
3. 更新 `config.js` 添加侧边栏配置
4. 更新 `docs/blog/README.md` 添加板块入口
5. 本地验证 → 提交代码 → 自动部署

## 日期管理规范

### 日期格式
- 统一使用格式：`` `[YYYY-MM-DD]` ``
- 示例：`` `[2026-02-07]` ``

### 日期获取方法

#### 新增文章
- 使用当前日期

#### 历史文章
- 通过 git 提交记录查询首次提交日期：
```bash
# PowerShell 命令
git log --follow --format="%ai" -- "文件路径" | Select-Object -Last 1
```

#### 日期标记位置
- 在 README.md 的文章链接后添加
- 格式：`- [文章标题](./文章.md) \`[2026-02-07]\``

---

**最后更新**: 2026-02-07
**维护者**: YoferChen
