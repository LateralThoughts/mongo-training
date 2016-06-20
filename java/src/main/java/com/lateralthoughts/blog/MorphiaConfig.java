package com.lateralthoughts.blog;

import com.lateralthoughts.blog.model.Post;
import com.mongodb.DB;
import com.mongodb.Mongo;
import com.mongodb.MongoClient;
import org.jongo.Jongo;
import org.mongodb.morphia.Datastore;
import org.mongodb.morphia.Morphia;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MorphiaConfig {

    @Bean
    public Morphia morphia() {
        final Morphia morphia = new Morphia();
        morphia.mapPackageFromClass(Post.class);
        return morphia;
    }

    @Bean
    public Datastore datastore(Morphia morphia) {
        return morphia.createDatastore(new MongoClient(), "blog");
    }

}
