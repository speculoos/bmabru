BEGIN;
TRUNCATE "bmabru_project_partners", "bmabru_projectimage", "bmabru_action", "bmabru_partnertype", "bmabru_function", "bmabru_project_image", "bmabru_partner", "bmabru_project", "bmabru_mission", "bmabru_project_functions", "bmabru_city", "bmabru_project_steps", "bmabru_step", "bmabru_program", "bmabru_projectstatus", "bmabru_project_programs",  "bmabru_procedure", "bmabru_project_actions";

SELECT setval(pg_get_serial_sequence('"bmabru_partnertype"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_partner"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_program"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_procedure"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_projectimage"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_function"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_mission"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_projectstatus"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_action"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_step"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_city"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_project"','id'), 1, false);

COMMIT;
