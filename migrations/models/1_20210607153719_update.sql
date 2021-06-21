-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(511) NOT NULL,
    "password" VARCHAR(511) NOT NULL
);
-- downgrade --
DROP TABLE IF EXISTS "user";
