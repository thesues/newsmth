#coding:utf8
bookTemplate = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
    <title>水木十大热点话题</title>
    <style type="text/css">
    body{
        font-size: 1.1em;
        margin:0 5px;
    }

    h1{
        font-size:4em;
        font-weight:bold;
    }

    h2 {
        font-size: 1.2em;
        font-weight: bold;
        margin:0;
    }
    a {
        color: inherit;
        text-decoration: inherit;
        cursor: default
    }
    a[href] {
        color: blue;
        text-decoration: underline;
        cursor: pointer
    }
    p{
        text-indent:1.5em;
        line-height:1.3em;
        margin-top:0;
        margin-bottom:0;
    }
    .italic {
        font-style: italic
    }
    .do_article_title{
        line-height:1.5em;
        page-break-before: always;
    }
    #cover{
        text-align:center;
    }
    #toc{
        page-break-before: always;
    }
    #content{
        margin-top:10px;
        page-break-after: always;
    }
    </style>
</head>
<body>
    <div id="cover">
        <h1 id="title">水木十大热点话题</h1><br>
        <a href="#content">jump to the first item</a><br />
    </div>

<div id="toc">
<ol>
{%for feed in sumaryFeeds%}
<li>
<a href="#sectionlist_{{forloop.counter}}">{{feed.title}}</a>
<br />
{{feed.numOfPosts}}items
</li>
{%endfor%}
</ol>
</div>

<mbp:pagebreak></mbp:pagebreak>


</div>
    
<div id="content">

{% for feed in sumaryFeeds %}
<div id="sectionlist_{{forloop.counter}}" class=section">
 <h2 class="do_article_title">{{feed.title}}</h2>
{%for post in feed.list%}
         <div class="article">
<!--             <a href="#sectionlist_{{forloop.parentloop.counter}}">back to lz</a> -->
             <br />
             {{post.content|linebreaksbr}}
         </div>
{%endfor%}
</div>
{%endfor%}
</div>
</body>
</html>
"""
