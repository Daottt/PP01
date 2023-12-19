insert into Users (login, password, power_level)
	values ("user1", "1", "0"), ("user1", "1", "1");

insert into Animals (name)
    values ("animal1"), ("animal2");

insert into Diseases (name)
    values ("disease1"), ("disease2");

insert into Requests (add_date, animal_id, user_id, treatment_type, disease_id, treatment_status, end_date)
    values("01.12.2023","1","2","treatment1","1","status1","07.12.2023"),("01.12.2023","2","2","treatment2","2","status2","");