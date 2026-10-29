WITH latest AS (
    SELECT DISTINCT ON (player_id) *
    FROM pace
    WHERE season = 2026
    ORDER BY player_id, game_num DESC
),
leaders AS (
    SELECT * FROM latest
    ORDER BY cum_yards DESC
    LIMIT 10
),
matches AS (
    SELECT DISTINCT ON (l.player_id)
           l.player_name, l.game_num, l.cum_yards,
           h.player_name AS hof_player, h.season AS hof_season,
           h.cum_yards AS hof_yards,
           ABS(l.cum_yards - h.cum_yards) AS yard_diff
    FROM leaders l
    JOIN pace h ON h.game_num = l.game_num
    WHERE h.player_name IN ('Randy Moss', 'Terrell Owens', 'Marvin Harrison', 'Calvin Johnson')
      AND h.season < 2026
    ORDER BY l.player_id, yard_diff
)
SELECT * FROM matches
ORDER BY cum_yards DESC;