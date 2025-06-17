-- Database: APPL_TO_DO

-- DROP DATABASE IF EXISTS "APPL_TO_DO";

CREATE DATABASE "APPL_TO_DO"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en-GB'
    LC_CTYPE = 'en-GB'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE "APPL_TO_DO"
    IS 'Database for a to-do Application';
	
-- SCHEMA: SCH_TASKS

-- DROP SCHEMA IF EXISTS "SCH_TASKS" ;

CREATE SCHEMA IF NOT EXISTS "SCH_TASKS"
    AUTHORIZATION postgres;

COMMENT ON SCHEMA "SCH_TASKS"
    IS 'Schema to hold all the tables';

-- Table: SCH_TASKS.T_TDO_TASKS

-- DROP TABLE IF EXISTS "SCH_TASKS"."T_TDO_TASKS";

CREATE TABLE IF NOT EXISTS "SCH_TASKS"."T_TDO_TASKS"
(
    "ID" numeric NOT NULL,
    "TASK_DESC" text COLLATE pg_catalog."default" NOT NULL,
    "IS_COMPLETED" boolean NOT NULL,
    CONSTRAINT "T_TDO_TASKS_pkey" PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "SCH_TASKS"."T_TDO_TASKS"
    OWNER to postgres;

COMMENT ON TABLE "SCH_TASKS"."T_TDO_TASKS"
    IS 'To store the tasks';
	
	
INSERT INTO "SCH_TASKS"."T_TDO_TASKS" (
"ID", "TASK_DESC", "IS_COMPLETED") VALUES 
(1,	'walk daily',false),
(2,	'Doodle',false),
(3,	'Journal',false),
(4,	'Meditation',false),
(5,	'Write Gratitude Journal',	false),
(6, 'Read books', false),
(7, 'Breathing Exercises', false)
;
	
	
	