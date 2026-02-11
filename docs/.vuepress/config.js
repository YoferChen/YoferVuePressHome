module.exports = {
  base: '/YoferVuePressHome/',
  title: 'Yofer\'s Blog',
  description: 'Yofer\'s personal blog and notes',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Blog', link: '/blog/' },
    ],
    sidebar: {
      '/blog/': genBlogSidebarConfig(),
    }
  },
  plugins: [
    '@vuepress/back-to-top',
  ]
};

function genBlogSidebarConfig () {
  return [
    {
      title: '博客首页',
      path: '/blog/',
      collapsable: false,
      children: [
        '/blog/',
        '/blog/OpenClawInstallationAndFeishuIntegration'
      ],
      sidebarDepth: 3
    }
  ];
}
