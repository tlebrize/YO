def SIMPLE_INSERT(table):
    return f"INSERT INTO {table} (name) VALUES (:name)"


GET_LAST_ID = "SELECT last_insert_rowid()"


EPISODE_INSERT = """
INSERT INTO episode (
    category_id,
    description,
    duration_id,
    id,
    level_id,
    series_id,
    series_index,
    tag,
    teacher_id,
    thumbnail,
    title,
    url)
VALUES (
    :category,
    :description,
    :duration,
    :id,
    :level,
    :series,
    :series_index,
    :tag,
    :teacher,
    :thumbnail,
    :title,
    :url)
"""

INSERT_BODYPART_EPISODE_M2M = """
INSERT INTO bodypart_episode (bodypart_id, episode_id)
VALUES (
    :bodypart_id,
    :episode_id
)
"""
