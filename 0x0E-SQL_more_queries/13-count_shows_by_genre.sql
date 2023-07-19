-- a script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows
-- linked to this genre>
SELECT tv_genres.genre AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
