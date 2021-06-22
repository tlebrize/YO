-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(511) NOT NULL,
    "password" VARCHAR(511) NOT NULL
);
CREATE TABLE IF NOT EXISTS "category" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "duration" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "level" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "series" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "teacher" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "tag" (
    "name" VARCHAR(255) NOT NULL,
    "id" SERIAL NOT NULL PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS "episode" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url" VARCHAR(511) NOT NULL,
    "thumbnail" VARCHAR(511) NOT NULL,
    "title" VARCHAR(511) NOT NULL,
    "description" TEXT NOT NULL,
    "category_id" INT REFERENCES "category" ("id") ON DELETE CASCADE,
    "duration_id" INT REFERENCES "duration" ("id") ON DELETE CASCADE,
    "level_id" INT REFERENCES "level" ("id") ON DELETE CASCADE,
    "series_id" INT REFERENCES "series" ("id") ON DELETE CASCADE,
    "tag_id" INT REFERENCES "tag" ("id") ON DELETE CASCADE,
    "teacher_id" INT REFERENCES "teacher" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "episode_user" (
    "episode_id" INT NOT NULL REFERENCES "episode" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
