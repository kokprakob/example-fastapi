-- SELECT * FROM votes 
-- order by user_id, post_id;
-- =========================================
SELECT * FROM posts 
LEFT JOIN votes on posts.id = votes.post_id
order by posts.id, votes.user_id;
-- =========================================
SELECT posts.id as Post_ID, count(votes.user_id) as Vote_count 
FROM posts 
LEFT JOIN votes on posts.id = votes.post_id
group by posts.id 
order by 1;
-- =========================================