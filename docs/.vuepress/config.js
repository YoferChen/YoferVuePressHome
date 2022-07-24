module.exports = {
  title: "Yofer\'s Home",
  description: "This is a vuepress website of YoferChen",
  head: [["link", { rel: "icon", href: `/favicon.ico` }]],
  base: "/YoferVuePressHome/",
  dest: "./website",

  themeConfig: {
    search: false,
    nav: [
      { text: "Home", link: "/" },
      { text: "About", link: "/about/" },
      // { text: "Projects", link: "/projects/" },
      { text: "Experiences", link: "/experiences/" },
      { text: "Blog", link: "/blog/" },
      { text: "Guide", link: "/guide/" },
      { text: "GitHub", link: "https://github.com/YoferChen" }
    ],
    sidebar: {
      '/guide/': genSidebarConfig('Guide'),
      '/blog/': genBlogSidebarConfig()
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
      collapsable: false,
      children: [
        '',
      ]
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
      title: '论文笔记',
      path: '/blog/PaperNotes/',
      collapsable: false,
      children: [
        '/blog/PaperNotes/',
      ]
    },
  ]
}

