module.exports = {
  title: "Yofer's Home", // From remote
  description: "This is a vuepress website of YoferChen", // From remote
  base: "/YoferVuePressHome/", // From remote (matches mine)
  head: [["link", { rel: "icon", href: `/yofer_favicon.ico` }]], // From remote
  dest: "./dist", // From remote

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Blog', link: '/blog/' },
      // ... keep any other nav items from remote if they existed outside the conflict block
    ],
    sidebar: {
      '/blog/': genBlogSidebarConfig(),
      // ... keep any other sidebar configurations from remote if they existed outside the conflict block
    }
  },
  plugins: [
    '@vuepress/back-to-top',
    // ... keep any other plugins from remote if they existed outside the conflict block
  ]
};

function genBlogSidebarConfig () {
  return [
    {
      title: '博客首页',
      path: '/blog/',
      collapsable: false,
      children: [
        '', // This was in remote, I'll keep it for the root of the blog section
        '/blog/OpenClawInstallationAndFeishuIntegration', // My new article
      ]
    },
    // Remote's existing blog categories
    {
      title: 'AI World',
      path: '/blog/AILearning/',
      collapsable: false,
      children: [
        '/blog/AILearning/',
        '/blog/AILearning/OpenClawGuide',
      ],
      sidebarDepth: 3
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
      sidebarDepth: 3
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
      sidebarDepth: 3
    },
    // Remote's commented out section, I'll keep it commented
    // {
    //   title: '论文笔记',
    //   path: '/blog/PaperNotes/',
    //   collapsable: true,
    //   children: [
    //     '/blog/PaperNotes/',
    //   ]
    // },
  ];
}

// Keep the remote's genDailySidebarConfig
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
      sidebarDepth: 3
    },
    {
      title: '照片墙',
      path: '/daily/photo/',
      collapsable: true,
      children: [
        '/daily/photo/',
        '/daily/photo/2024',
      ],
      sidebarDepth: 3
    },
  ];
}
