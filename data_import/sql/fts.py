SETUP_EPISODE_FTS = """
CREATE VIRTUAL TABLE episode_fts
USING fts5(
	id, title, url, thumbnail, description, level,
	teacher, category, duration, series, body_parts,
	content=full_episode,
	content_rowid=id
)
"""

REBUILD_FTS = "INSERT INTO episode_fts(episode_fts) VALUES('rebuild')"
