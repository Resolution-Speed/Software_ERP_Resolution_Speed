create database erp_resolution_speed;

use erp_resolution_speed;

create table usuario(
	userMatricula int unique not null auto_increment ,
    userNome varchar(50) not null,
    genero char(1) not null,
    senha varchar(8) not null,
    userHierarquia varchar(3) not null,
    primary key(userMatricula)
);

create table produto(
	codigoProduto int primary key unique not null auto_increment,
    ncm_nbm int not null,
    nomeProduto varchar(80) not null,
    unidade int not null,
    pesoLiquido float not null,
    pesoBruto float not null,
    alturaProduto float not null,
    larguraProduto float not null,
    comprimentoProduto float,
    fornecedorProduto varchar(50) not null,
    preco float not null
);

create table pedidoVenda(
	numPedido int primary key unique not null auto_increment,
    clientePedido varchar(50) not null,
    tipoVenda varchar(10) not null,
    prazoPedido date not null,
    vendedorPedido varchar(50) not null,
    ordemCompra int not null
);

create table produto_venda(
	codProd int not null,
    nPed int not null,
    foreign key (codProd) references produto (codigoProduto),
    foreign key (nPed) references pedidoVenda (numPedido)
);

insert into usuario values(0, "Wildovisk", "M", 123456, "USC");
select * from usuario;
insert into usuario values(0, "João", "M", 123456, "USC");

update usuario set senha = 123456 where userMatricula = 1;

drop database erp_resolution_speed;  /*Excluir banco de dados*/