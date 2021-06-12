-- upgrade --
ALTER TABLE "episode" ADD "category_id" INT;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_category_f18620af" FOREIGN KEY ("category_id") REFERENCES "category" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_category_f18620af";
ALTER TABLE "episode" DROP COLUMN "category_id";
