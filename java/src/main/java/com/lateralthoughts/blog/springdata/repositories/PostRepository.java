package com.lateralthoughts.blog.springdata.repositories;

import com.lateralthoughts.blog.model.Post;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import java.util.List;

@RepositoryRestResource(collectionResourceRel = "post", path = "post")
public interface PostRepository extends MongoRepository<Post, String>, PostRepositoryCustom {

    List<Post> findByAuthor(String author);

    Post findByPermalink(String permalink);

    List<Post> findByTags(String tag);
}
