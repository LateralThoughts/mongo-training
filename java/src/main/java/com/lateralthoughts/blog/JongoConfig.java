package com.lateralthoughts.blog;

import com.mongodb.DB;
import com.mongodb.Mongo;
import com.mongodb.MongoClient;
import org.jongo.Jongo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@Configuration
public class JongoConfig {

    @Bean
    public Jongo jongo(DB db) {
        return new Jongo(db);
    }

    @Bean
    public DB db() {
        return new DB(mongo(), "blog");
    }

    @Bean
    public Mongo mongo() {
        return new MongoClient();
    }
}
