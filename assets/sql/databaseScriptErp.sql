create database erp_resolution_speed;

use erp_resolution_speed;

create table usuario(
	userMatricula int(5) unique not null auto_increment ,
    userNome varchar(50) not null,
    genero char(1) not null,
    senha int(8) not null,
    userHierarquia varchar(3) not null
);



create table produto(
	codigoProduto int(12) primary key unique not null auto_increment,
    ncm_nbm int(10) not null,
    nomeProduto varchar(80) not null,
    unidade int(3) not null,
    pesoLiquido float(10, 2) not null,
    pesoBruto float (10, 2) not null,
    alturaProduto float(4,2) not null,
    larguraProduto float(4,2) not null,
    comprimentoProduto float(4, 2),
    fornecedorProduto varchar(50) not null,
    preco float(8, 2) not null
    
);

create table pedidoVenda(
	numPedido int(10) primary key unique not null auto_increment,
    clientePedido varchar(50) not null,
    tipoVenda varchar(10) not null,
    prazoPedido date not null,
    vendedorPedido varchar(50) null,
    ordemCompra int(10) null
);

create table produto_venda(
	codProd int(12) not null,
    nPed int(10) not null,
    foreign key (codProd) references produto (codigoProduto),
    foreign key (nPed) references pedidoVenda (numPedido)
);

insert into usuario values(0, "Wildovisk", "M", 12345, "USC");
select * from usuario;
insert into usuario values(0, "João", "M", 123456, "USC");

drop database erp_resolution_speed;  /*Excluir banco de dados*/