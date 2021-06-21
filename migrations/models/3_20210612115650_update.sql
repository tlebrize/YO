-- upgrade --
ALTER TABLE "episode" ADD "tag_id" INT;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_tag_63c7d612" FOREIGN KEY ("tag_id") REFERENCES "tag" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_tag_63c7d612";
ALTER TABLE "episode" DROP COLUMN "tag_id";
