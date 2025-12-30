create database library;
use library;

create table members(
    id int auto_increment primary key,
    name varchar(255) not null,
    surname varchar(255) not null,
    email varchar(255) not null unique,
    membership_type enum('basic', 'premium') not null,
    active boolean not null,
    created_at datetime not null
);

create table books(
    id int auto_increment primary key,
    title varchar(255) not null,
    isbn varchar(20) unique,
    genre enum('fiction', 'nonfiction', 'sci-fi', 'fantasy', 'other') not null,
    published_year int
);

create table authors(
    id int auto_increment primary key,
    name varchar(255) not null,
    surname varchar(255) not null
);

create table book_author(
    id int auto_increment primary key,
    book_id int not null,
    author_id int not null,
    unique (book_id, author_id),
    foreign key (book_id) references books (id) on delete cascade on update cascade,
    foreign key (author_id) references authors (id) on delete cascade on update cascade
);

create table copies(
    id int auto_increment primary key,
    book_id int not null,
    inventory_code varchar(50) unique,
    status enum('borrowed', 'available', 'damaged') not null,
    price float not null,
    foreign key (book_id) references books (id) on delete cascade on update cascade
);

create table loans(
    id int auto_increment primary key,
    member_id int not null,
    copy_id int not null,
    loan_date date not null,
    due_date date not null,
    return_date date,
    penalty_amount float default 0,
    penalty_paid boolean not null,
    foreign key (member_id) references members (id),
    foreign key (copy_id) references copies (id)
);