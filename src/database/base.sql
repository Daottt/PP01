create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);

create table Animals(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table Diseases(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);

create table Requests(
    id integer PRIMARY KEY autoincrement,
    add_date DATE,
    animal_id integer,
    user_id integer,
    treatment_type varchar(250),
    disease_id integer,
    treatment_status varchar(250),
    end_date DATE,
    foreign key (user_id) references Users(id),
    foreign key (animal_id) references Animals(id),
    foreign key (disease_id) references Diseases(id)
);
