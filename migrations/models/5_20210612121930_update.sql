-- upgrade --
ALTER TABLE "episode" ADD "level_id" INT;
ALTER TABLE "episode" ADD "series_id" INT;
ALTER TABLE "episode" ADD "duration_id" INT;
ALTER TABLE "episode" ADD "teacher_id" INT;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_series_661e04ce" FOREIGN KEY ("series_id") REFERENCES "series" ("id") ON DELETE CASCADE;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_duration_3dc04663" FOREIGN KEY ("duration_id") REFERENCES "duration" ("id") ON DELETE CASCADE;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_teacher_d58d6f6c" FOREIGN KEY ("teacher_id") REFERENCES "teacher" ("id") ON DELETE CASCADE;
ALTER TABLE "episode" ADD CONSTRAINT "fk_episode_level_98b53349" FOREIGN KEY ("level_id") REFERENCES "level" ("id") ON DELETE CASCADE;
-- downgrade --
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_level_98b53349";
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_teacher_d58d6f6c";
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_duration_3dc04663";
ALTER TABLE "episode" DROP CONSTRAINT "fk_episode_series_661e04ce";
ALTER TABLE "episode" DROP COLUMN "level_id";
ALTER TABLE "episode" DROP COLUMN "series_id";
ALTER TABLE "episode" DROP COLUMN "duration_id";
ALTER TABLE "episode" DROP COLUMN "teacher_id";
