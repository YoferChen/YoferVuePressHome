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
- text: Home
  link: /YoferVuePressHome/
- text: Projects
  link: /YoferVuePressHome/projects/
- text: Blog
  # link: https://blog.csdn.net/weixin_44002829
  link: /YoferVuePressHome/blog/
# - text: Article
#   link: /article/
footer: Made with ♥ by Yofer. Powered by VuePress
---

<AboutCard :frontmatter="$page.frontmatter" >

<!-- 本科毕业于广州大学，现为北京科技大学在读研究生。热爱计算机专业，对各个领域都保持好奇心，技术面广泛并希望能不断扩展，目前主要在学习并专注于“人工智能”、“深度学习”、“计算机视觉”领域，对PyQt、前后端开发有所涉猎，不断探索如何将技术应用到日常~ -->
欢迎访问Yofer's Home！

- 本人是一名计算机科学科学与技术专业**程序员**。目前是**北京科技大学**在读硕士研究生。

- 选择计算机专业源于对计算机世界的好奇、兴趣与热爱，初心是希望通过编程，创造出许多有价值的工具，为人们的生活带来便利，服务大众。

- 本人主要涉略的技术包括：”人工智能“、”计算机视觉“、”Web开发“、”客户端开发（PyQt）“等。

- 如果您有任何问题想要交流或者想要了解更多关于我的信息，欢迎随时联系我~


**编者说：** 编程不仅仅是一种技术，更是一种创造世界的艺术

</AboutCard>

<style lang="stylus">

.theme-container.about-page .page
  background-color #e6ecf0
  min-height calc(100vh)
  
  .last-updated
    display none

</style>