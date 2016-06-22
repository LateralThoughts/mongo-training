<!doctype HTML>
<html>
<head>
<title>Create a new post</title>
<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">
</head>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
%if (username != None):
          <a class="brand" href="#">Welcome {{username}} </a>
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

<div class="container" style="margin-top:60px">
<form action="/newpost" method="POST" class="form-horizontal">
{{errors}}
<h2>Title<h2>
<input type="text" id="subject" name="subject" class="input-xxlarge" value="{{subject}}">
<h2>Blog Entry<h2>
<textarea name="body" class="input-xxlarge" rows="20">{{body}}</textarea><br>
<h2>Tags</h2>
Comma separated, please<br>
<input type="text" name="tags" class="input-xxlarge" value="{{tags}}"><br>
<p>
<input type="submit" value="Submit" class="btn btn-primary">
</div>
<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
</body>
</html>

