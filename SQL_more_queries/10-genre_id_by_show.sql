-- commment
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
LEFT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
