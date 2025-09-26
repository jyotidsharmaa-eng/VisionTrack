-- Total burn vs budget
SELECT p.id, p.name, p.budget, COALESCE(SUM(c.amount),0) AS burn, 
       (p.budget - COALESCE(SUM(c.amount),0)) AS remaining
FROM projects p
LEFT JOIN costs c ON c.project_id = p.id
GROUP BY p.id, p.name, p.budget
ORDER BY remaining ASC;
