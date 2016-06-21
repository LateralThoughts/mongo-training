package com.lateralthoughts.blog.springdata.repositories;

import com.lateralthoughts.blog.model.Comment;

public interface PostRepositoryCustom {

    void addComment(String permalink, Comment comment);
}
