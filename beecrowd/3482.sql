SELECT u1_name, u2_name
FROM (
    SELECT DISTINCT
        CASE
            WHEN c.posts < d.posts THEN c.user_name
            WHEN c.posts > d.posts THEN d.user_name
            ELSE c.user_name
        END AS u1_name,
        CASE
            WHEN c.posts > d.posts THEN c.user_name
            WHEN c.posts < d.posts THEN d.user_name
            ELSE c.user_name
        END AS u2_name,
        CASE
            WHEN c.posts < d.posts THEN c.user_id
            WHEN c.posts > d.posts THEN d.user_id
            ELSE c.user_id
        END AS ordenacao
    FROM followers a
    LEFT JOIN followers b ON b.following_user_id_fk = a.user_id_fk
    LEFT JOIN users c ON c.user_id = a.user_id_fk
    LEFT JOIN users d ON d.user_id = b.user_id_fk
    WHERE a.user_id_fk = b.following_user_id_fk
      AND a.following_user_id_fk = b.user_id_fk
) t
ORDER BY ordenacao;