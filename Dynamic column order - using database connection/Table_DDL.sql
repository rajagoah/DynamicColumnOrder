begin;
create table aakarsh_db.target_table
( Therapeutic_area varchar(100)
, RFP_id varchar(5)
, age integer
, Load_date date
, program_start_date date
);
commit;

insert into aakarsh_db.target_table
(therapeutic_area, rfp_id, age)
values
('IMM', '101', '21');

insert into aakarsh_db.target_table
(therapeutic_area, rfp_id, age, load_date, program_start_date)
values
('CVM', '101', '19', '2020-07-21','1999-01-01');

insert into aakarsh_db.target_table
(therapeutic_area, rfp_id, age, load_date, program_start_date)
values
('ID', '103', '19','2020-06-22', '2000-01-01');
