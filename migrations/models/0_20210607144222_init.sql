-- upgrade --
CREATE TABLE IF NOT EXISTS "episode" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url" VARCHAR(511) NOT NULL,
    "thumbnail" VARCHAR(511) NOT NULL,
    "title" VARCHAR(511) NOT NULL,
    "description" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
