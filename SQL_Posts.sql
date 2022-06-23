-- =========================================
SELECT * FROM public.alembic_version
ORDER BY version_num ASC
-- SELECT * FROM posts;
-- SELECT posts.id as Post_No,posts.title,posts.content,
-- posts.owner_id,
-- split_part (users.email,'@',1) as User_name,
-- users.email
-- FROM posts left join users 
-- on owner_id = users.id
-- WHERE owner_id = 13
-- order by Post_No;
-- =========================================
SELECT users.id,
split_part (users.email,'@',1) as User_name,
count(posts.id) as Count_Post
FROM posts RIGHT join users 
on owner_id = users.id
group by users.id
order by users.id;
-- =========================================