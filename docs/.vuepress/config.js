module.exports = {
  title: "Yofer\'s Home",
  description: "This is a vuepress website of YoferChen",
  // base: "/yofervuepresshome/",
  base: "/YoferVuePressHome/",
  head: [["link", { rel: "icon", href: `/yofer_favicon.ico` }]],
  dest: "./dist",

  themeConfig: {
    search: false,
    nav: [
      { text: "Home", link: "/" },
      { text: "About", link: "/about/" },
      { text: "Projects", link: "/projects/" },
      { text: "Experiences", link: "/experiences/" },
      { text: "Blog", link: "/blog/" },
      { text: "Guide", link: "/guide/" },
      { text: "GitHub", link: "https://github.com/YoferChen" }
    ],
    sidebar: {
      '/guide/': genSidebarConfig('Guide'),
      '/blog/': genBlogSidebarConfig(),
      '/daily/': genDailySidebarConfig()
    },
    lastUpdated: 'Last Updated'
  },

  markdown: {
    // options for markdown-it-anchor
    anchor: { permalink: false },
    extendMarkdown: md => {
      md.use(require("markdown-it-katex"));
    }
  }
};

function genSidebarConfig (title) {
  return [
    {
      title,
      collapsable: false,
      children: [
        '',
        'getting-started',
        'customize',
        'advanced',
      ]
    }
  ]
}


function genBlogSidebarConfig () {
  return [
    {
      title: '介绍',
      path: '/blog/',
      collapsable: true,
      children: [
        '',
      ]
    },
    {
      title: 'OpenClaw AI Agent',
      path: '/blog/OpenClawGuide/',
      collapsable: false,
      children: [
        '/blog/OpenClawGuide/',
        '/blog/OpenClawGuide/installation',
        '/blog/OpenClawGuide/quick-start',
        '/blog/OpenClawGuide/core-features',
        '/blog/OpenClawGuide/advanced-configuration',
        '/blog/OpenClawGuide/best-practices',
      ],
      sidebarDepth: 3  //左侧导航展开级数
    },
    {
      title: 'PyQt5',
      path: '/blog/PyqtLearning/',
      collapsable: false,
      children: [
        '/blog/PyqtLearning/',
        '/blog/PyqtLearning/pyQt万能功能模板',
        '/blog/PyqtLearning/QSS万能样式模板',
        '/blog/PyqtLearning/QT美化之QSS笔记',
      ],
      sidebarDepth: 3  //左侧导航展开级数
    },
    {
      title: '系统维护手册',
      path: '/blog/SystemMaintenance/',
      collapsable: false,
      children: [
        '/blog/SystemMaintenance/',
        '/blog/SystemMaintenance/Linux',
        '/blog/SystemMaintenance/Windows',
        '/blog/SystemMaintenance/Termux',
      ]
    },    
    {
      title: '资源集合',
      path: '/blog/Resources/',
      collapsable: false,
      children: [
        '/blog/Resources/',
        '/blog/Resources/Software',
        '/blog/Resources/Study',
      ],
      sidebarDepth: 3  //左侧导航展开级数
    },
    // {
    //   title: '论文笔记',
    //   path: '/blog/PaperNotes/',
    //   collapsable: true,
    //   children: [
    //     '/blog/PaperNotes/',
    //   ]
    // },
  ]
}


function genDailySidebarConfig () {
  return [
    {
      title: '记录生活',
      path: '/daily/',
      collapsable: true,
      children: [
        '',
      ]
    },
    {
      title: '电影墙',
      path: '/daily/movie/',
      collapsable: true,
      children: [
        '/daily/movie/',
        '/daily/movie/2024',
      ],
      sidebarDepth: 3  //左侧导航展开级数
    },
    {
      title: '照片墙',
      path: '/daily/photo/',
      collapsable: true,
      children: [
        '/daily/photo/',
        '/daily/photo/2024',
      ],
      sidebarDepth: 3  //左侧导航展开级数
    },
  ]
}