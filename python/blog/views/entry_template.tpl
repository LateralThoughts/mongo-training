<!doctype HTML>
<html>
<head>
    <title>
        Blog Post
    </title>
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
            <a class="brand" href="/">Welcome {{username}} </a>
            %end
            <div class="nav-collapse collapse">
                %if (username != None):
                <ul class="nav">
                    <li class="active"><a href="/">Home</a></li>
                    <li><a href="/logout">Logout</a></li>
                    <li><a href="/newpost">New Post</a>
                        <p></li>
                </ul>
                %end
                %if (username == None):
                <a class="brand" href="/login">Se connecter</a>
                %end
            </div><!--/.nav-collapse -->
        </div>
    </div>
</div>

<div class="container" style="margin-top: 60px">
    <h1>{{post['title']}}</h1>
    Posted {{post['date']}}<i> By {{post['author']}}</i><br>
    <hr>
    {{!post['body']}}
    <p>
        <em>Filed Under</em>:
        %if ('tags' in post):
        %for tag in post['tags'][0:1]:
        <a href="/tag/{{tag}}">{{tag}}</a>
        %for tag in post['tags'][1:]:
        , <a href="/tag/{{tag}}">{{tag}}</a>
        %end
        %end
        %end
    <p>
        Comments:
        %if ('comments' in post):
        %numComments = len(post['comments'])
        %else:
        %numComments = 0
        %end
        %for i in range(0, numComments):
    <form action="/like" method="POST">
        <input type="hidden" name="permalink" , value="{{post['permalink']}}">
        <input type="hidden" name="comment_ordinal" , value="{{i}}">
        Author: {{post['comments'][i]['author']}}<br>
        {{post['comments'][i]['body']}}<br>
        <hr>
        %end
        <h3>Add a comment</h3>
        <form action="/newcomment" method="POST">
            <input type="hidden" name="permalink" , value="{{post['permalink']}}">
            {{errors}}
            <b>Name</b> (required)<br>
            <input type="text" name="commentName" size="60" value="{{comment['name']}}"><br>
            <b>Email</b> (optional)<br>
            <input type="text" name="commentEmail" size="60" value="{{comment['email']}}"><br>
            <b>Comment</b><br>
            <textarea name="commentBody" cols="60" rows="10">{{comment['body']}}</textarea><br>
            <input type="submit" value="Submit">
        </form>
    </form>
</div>
<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
</body>
</html>


