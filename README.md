# 知识宝库

个人网站：<https://ruguo0119.github.io/>。GitHub Pages 从 `main` 分支根目录发布。

## 页面职责

- `index.html`：个人介绍、研究兴趣、精选项目、荣誉。首页不展示博客文章正文或摘要。
- `archives/index.html`：博客列表，仅标题、日期和原文章入口。
- `about/index.html`：教育与实习时间线、站点说明、公开联系邮箱。
- `2025/07/26/*/index.html`：原有文章全文，原 URL 与正文保留。
- `archives/2025/`、`tags/`、`categories/`：保留的旧归档和分类入口。
- `css/site.css`：小型共享样式；主导航固定为首页、博客、关于，当前栏目使用 `aria-current="page"`。

## 维护与预览

这是包含 Hexo/NexT 静态产物的发布仓库；仓库内没有 Hexo 源模板、配置或构建工作流。三个主页面直接维护 HTML，不需要引入新框架。文章页继续使用既有主题与资产。

在仓库根目录运行 `python -m http.server 8765 --bind 127.0.0.1`，然后打开 <http://127.0.0.1:8765/>。修改后核对导航、旧文章链接、手机布局以及公开联系信息，再提交至 `main`。

`python tools/update_navigation.py` 可重复执行，为现有 Hexo 页面补上相同导航、共享样式和本站 canonical URL；脚本不修改文章正文，不覆盖手写的三个主页面。新增文章后，在博客列表添加一行标题、日期与链接即可。

**外部 Hexo 重建可能覆盖本仓库的手写页面与导航。** 如重新使用 Hexo 发布，应先保留三个主页面、`css/site.css` 与本脚本，再将对应内容迁入真正的 Hexo 源模板；发布前重新检查完整 diff，不要直接覆盖远端未知改动。

公开联系邮箱仅使用 `jialiangli25@stu.pku.edu.cn`。本站不包含完整简历 PDF、电话、学号、私人邮箱或未公开实习技术细节。
