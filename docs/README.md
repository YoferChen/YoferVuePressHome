---
pageClass: home-page
# some data for the components

name: YoferChen
profile: /profile.jpg

socials:
  - title: gitee
    icon: "/icons/gitee.svg"
    link: https://gitee.com/yoferchen
  - title: github
    icon: "/icons/github.svg"
    link: https://github.com/YoferChen
  - title: csdn
    icon: "/icons/csdn.svg"
    link: https://blog.csdn.net/weixin_44002829
  - title: bilibili
    icon: "/icons/bilibili.svg"
    link: https://space.bilibili.com/385581781

blog: https://blog.csdn.net/weixin_44002829
bio: Students majoring in computer science and technology
email: 1732562137@qq.com
---

<ProfileSection :frontmatter="$page.frontmatter" />

## About Me

I graduated from Guangzhou University with an undergraduate degree . And I am currently studying graduate students in Beijing University of Science and Technology. Computer science is my interest. I am studying and focusing on Artificial Intelligence, Computer Vision, PYQT and Web Development. It is my ideal to explore how to apply technology to daily life.

**Summary:** One programmer, loves life, loves technology, and strives to explore a  wider world.

## News

- [July 2022] Graduated from Guangzhou University
- [Nov 1999] Born in Shantou, Guangdong Province, China


## Education

- **University of Science and Technology Beijing** <br/>
Sept 2022.09 - ~

- **Guangzhou University** <br/>
Sept 2018.09 - 2022.07
## Experiences
[→ Full list](/experiences/)

<ExperienceCard image="/experiences/GZHU.jpg">

  2018.09 - 2022.07
  
  **Grangzhou University**
  
  广州大学（Guangzhou University），简称广大（GU）  ，位于广东省广州市，是经教育部批准成立的综合性大学，实行省市共建、以市为主的办学体制，是广东省高水平大学重点建设高校、国家“111计划”建设高校、广东省双一流重点建设高校、广州市高水平大学建设高校。
  
  [[GZHU](http://www.gzhu.edu.cn/)] [[SC](https://jsj.gzhu.edu.cn/)]

</ExperienceCard>

<ExperienceCard image="/experiences/USTB.png">

  2022.09 - ~

  **Beijing University of Science and Technology**
  
  北京科技大学（University of Science and Technology Beijing），简称北科大，位于北京市，是中华人民共和国教育部直属的全国重点大学，是“双一流”建设高校、国家“211工程”和“985工程优势学科创新平台”建设高校、教育部首批“三全育人”综合改革试点高校、首批北京市深化创新创业教育改革示范高校，入选卓越工程师教育培养计划、高等学校学科创新引智计划、高等学校创新能力提升计划、国家大学生创新性实验计划、国家建设高水平大学公派研究生项目、新工科研究与实践项目、教育部来华留学示范基地、中国政府奖学金来华留学生接收院校，是北京高科大学联盟、中欧工程教育平台、中俄工科大学联盟、CDIO工程教育联盟成员单位和中国人工智能教育联席会理事单位

  [[USTB](https://www.ustb.edu.cn/)] [[SC](http://scce.ustb.edu.cn/)] [[SD](https://sd.ustb.edu.cn/)] 

</ExperienceCard>


## Awards & Honors
- XXX
- XXX

### Contests
- XXX

## Notice
This website conducts secondary development based on [vuepress-homepage](https://github.com/imfing/vuepress-homepage)

<!-- Custom style for this page -->

<style lang="stylus">

.theme-container.home-page .page
  font-size 14px
  font-family "lucida grande", "lucida sans unicode", lucida, "Helvetica Neue", Helvetica, Arial, sans-serif;
  p
    margin 0 0 0.5rem
  p, ul, ol
    line-height normal
  a
    font-weight normal
  .theme-default-content:not(.custom) > h2
    margin-bottom 0.5rem
  .theme-default-content:not(.custom) > h2:first-child + p
    margin-top 0.5rem
  .theme-default-content:not(.custom) > h3
    padding-top 4rem

  /* Override */
  .md-card
    margin-top 0.5em
    .card-image
      padding 0.2rem
      img
        max-width 120px
        max-height 120px
    .card-content p
      -webkit-margin-after 0.2em

@media (max-width: 419px)
  .theme-container.home-page .page
    p, ul, ol
      line-height 1.5

    .md-card
      .card-image
        img 
          width 100%
          max-width 400px

</style>
