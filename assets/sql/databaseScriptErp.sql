create database erp_resolution_speed;

use erp_resolution_speed;

create table usuario(
	userMatricula int(5) unique not null auto_increment,
    userNome varchar(50) not null,
    genero char(1) not null,
    senha int(8) not null,
    userHierarquia varchar(3) not null,
);