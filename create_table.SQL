create table if not exists countries (
    country_id serial primary key,
    country_name varchar(100) unique  not null
);

create table if not exists cities (
    city_id serial primary key,
    city_name varchar(100) unique not null,
    country_id int not null,
    latitude decimal,
    longitude decimal,
    foreign key (country_id) references countries(country_id)
);

create table if not exists target_types (
    target_type_id serial primary key,
    target_type_name varchar(255) unique not null
);


create table if not exists targets (
    target_id serial primary key,
    target_industry varchar(255) not null,
    city_id int not null,
    target_type_id int,
	target_priority int,
    foreign key (city_id) references cities(city_id),
    foreign key (target_type_id) references target_types (target_type_id)
);