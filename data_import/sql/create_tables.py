CREATE_TEACHERS = """
CREATE TABLE IF NOT EXISTS teacher
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""


CREATE_LEVELS = """
CREATE TABLE IF NOT EXISTS level
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""

CREATE_CATEGORIES = """
CREATE TABLE IF NOT EXISTS category
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""

CREATE_SERIES = """
CREATE TABLE IF NOT EXISTS series
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""

CREATE_DURATIONS = """
CREATE TABLE IF NOT EXISTS duration
(
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL
)
"""

CREATE_BODYPART = """
CREATE TABLE IF NOT EXISTS bodypart
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""
CREATE_TAG = """
CREATE TABLE IF NOT EXISTS tag
(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL
)
"""

CREATE_EPISODES = """
CREATE TABLE IF NOT EXISTS episode
(
    category_id     INTEGER REFERENCES category (id),
    description     TEXT,
    duration_id     INTEGER REFERENCES duration (id),
    id              INTEGER PRIMARY KEY,
    level_id        INTEGER REFERENCES level (id),
    series_id       INTEGER REFERENCES series (id),
    series_index    INTEGER,
    tag_id          INTEGER,
    teacher_id      INTEGER REFERENCES teacher (id),
    thumbnail       TEXT,
    title           TEXT,
    url             TEXT NOT NULL
)
"""

CREATE_BODYPART_EPISODE_M2M = """
CREATE TABLE IF NOT EXISTS bodypart_episode
(
    id          INTEGER PRIMARY KEY,
    bodypart_id INTEGER REFERENCES bodypart (id),
    episode_id  INTEGER REFERENCES episode (id)
)
"""

statements = [
    CREATE_TEACHERS,
    CREATE_LEVELS,
    CREATE_CATEGORIES,
    CREATE_SERIES,
    CREATE_DURATIONS,
    CREATE_BODYPART,
    CREATE_TAG,
    CREATE_EPISODES,
    CREATE_BODYPART_EPISODE_M2M,
]
