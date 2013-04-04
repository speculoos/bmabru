BEGIN;
TRUNCATE "bmabru_projectimage", "bmabru_action",  "bmabru_project_worth",
"bmabru_partnertype", "bmabru_function", "bmabru_project_image",
"bmabru_partner", "bmabru_projectworth", "bmabru_projectstatus", 
"bmabru_mission", "bmabru_project_functions", "bmabru_partnership",
"bmabru_tradeobject", "bmabru_city", "bmabru_project_steps", "bmabru_step",
"bmabru_program", "bmabru_partnershiptype", "bmabru_project",
"bmabru_project_programs", "bmabru_procedure", "bmabru_project_actions" ,  
"bmabru_budgetrange", "bmabru_surfacerange" CASCADE;

SELECT setval(pg_get_serial_sequence('"bmabru_partnertype"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_partner"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_partnershiptype"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_partnership"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_tradeobject"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_program"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_procedure"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_projectimage"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_function"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_mission"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_projectstatus"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_action"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_step"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_city"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_projectworth"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"bmabru_project"','id'), 1, false);


COMMIT;
