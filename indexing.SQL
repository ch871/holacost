CREATE INDEX idx_target_industryl ON targets (target_industry);
EXPLAIN ANALYZE SELECT * from targets WHERE target_industry = 'BRIDGES';
DROP INDEX IF EXISTS idx_user_email;