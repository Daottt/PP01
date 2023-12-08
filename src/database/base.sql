create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);

create table Requests(
    id integer PRIMARY KEY autoincrement,
    add_date DATE,
    animal varchar(50),
    user_id integer,
    treatment_type varchar(250),
    disease_description varchar(250),
    treatment_status varchar(250),
    end_date DATE,
    foreign key (user_id) references Users(id)
);
