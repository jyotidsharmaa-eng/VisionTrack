-- Views for Power BI
CREATE OR REPLACE VIEW vw_project_costs AS
SELECT p.id AS project_id, p.name, SUM(c.amount) AS total_cost
FROM projects p
LEFT JOIN costs c ON c.project_id = p.id
GROUP BY p.id, p.name;

CREATE OR REPLACE VIEW vw_project_hours AS
SELECT p.id AS project_id, p.name,
       COALESCE(SUM(t.planned_hours),0) AS planned_hours,
       COALESCE(SUM(t.actual_hours),0)  AS actual_hours
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
GROUP BY p.id, p.name;

CREATE OR REPLACE VIEW vw_scope_versions AS
SELECT p.id AS project_id, p.name, MAX(s.version) AS latest_scope_version, COUNT(s.id) AS total_changes
FROM projects p
LEFT JOIN scope_changes s ON s.project_id = p.id
GROUP BY p.id, p.name;
