---
pageClass: about-page
description: 'The biography and information about me.'
avatar: /profile.jpg
head: 'YoferChen'
info: 'Students majoring in computer science and technology'
interests: 'Interests: AI/CV/DL/ML/Python/Web.'
socials:
- title: github
  link: https://github.com/YoferChen
- title: gitee
  link: https://gitee.com/yoferchen
- title: csdn
  link: https://blog.csdn.net/weixin_44002829
- title: bilibili
  link: https://space.bilibili.com/385581781
- title: email
  link: 'mailto:1732562137@qq.com'
actions:
- text: Projects
  link: /projects/
- text: Blog
  link: https://blog.csdn.net/weixin_44002829
- text: Article
  link: /article/
footer: Made with ♥ by Yofer. Powered by VuePress
---

<AboutCard :frontmatter="$page.frontmatter" >

本科毕业于广州大学，现为北京科技大学在读研究生。热爱计算机专业，对各个领域都保持好奇心，技术面广泛并希望能不断扩展，目前主要在学习并专注于“人工智能”、“深度学习”、“计算机视觉”领域，对PyQt、前后端开发有所涉猎，不断探索如何将技术应用到日常~

**自述：** 程序员一枚，热爱生活、热爱技术，努力探寻更加广袤的天空~

</AboutCard>

<style lang="stylus">

.theme-container.about-page .page
  background-color #e6ecf0
  min-height calc(100vh)
  
  .last-updated
    display none

</style>