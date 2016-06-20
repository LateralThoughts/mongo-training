<!DOCTYPE html>
<html>
<head>
<title>My Blog</title>
<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">

</head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
%if (username != None):
          <a class="brand" href="/">Welcome {{username}} </a>
%end
          <div class="nav-collapse collapse">
%if (username != None):
            <ul class="nav">
              <li class="active"><a href="/">Home</a></li>
              <li><a href="/logout">Logout</a></li>
              <li><a href="/newpost">New Post</a><p></li>
            </ul>
%end
%if (username == None):
           <a class="brand" href="/login">Se connecter</a>
%end
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
         
<div class="container"  style="margin-top:60px">
<h1>My Blog</h1>

%for post in myposts:
<h2><a href="/post/{{post['permalink']}}">{{post['title']}}</a></h2>
Posted {{post['post_date']}} <i>By {{post['author']}}</i><br>
Comments: 
%if ('comments' in post):
%numComments = len(post['comments'])
%else:
%numComments = 0
%end
<a href="/post/{{post['permalink']}}">{{numComments}}</a>
<hr>
{{!post['body']}}
<p>
<p>
<em>Filed Under</em>: 
%if ('tags' in post):
%for tag in post['tags'][0:1]:
<a href="/tag/{{tag}}">{{tag}}</a>
%for tag in post['tags'][1:]:
, <a href="/tag/{{tag}}">{{tag}}</a>
%end
%end

<p>
%end
</div>
<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
</body>
</html>


