CREATE_FULL_EPISODE = """
CREATE VIEW full_episode AS 
SELECT
    episode.id id,
    episode.url url,
    episode.thumbnail thumbnail,
    episode.description description,
    episode.title title,
    level.name level,
    teacher.name teacher,
    category.name category,
    series.name series,
    duration.name duration,
    group_concat(bodypart.name, ",") body_parts
FROM episode
LEFT JOIN level ON level.id = episode.level_id
LEFT JOIN teacher ON teacher.id = episode.teacher_id
LEFT JOIN category ON category.id = episode.category_id
LEFT JOIN series ON series.id = episode.series_id
LEFT JOIN duration ON duration.id = episode.duration_id
LEFT JOIN bodypart_episode ON bodypart_episode.episode_id = episode.id
LEFT JOIN bodypart ON bodypart.id = bodypart_episode.bodypart_id
GROUP BY episode.id
"""
