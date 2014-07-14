drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null,
  time string not null
);

drop table if exists members;
create table members (
  id integer primary key autoinremenet,
  picture string not null,
  name string not null,
  bio string not null,
  directory string not null
);

drop table if exists events;
create table events (
  name string not null,
  description string not null,
  location string not null,
  link string not null,
  edate string not null,
  time string not null,
  till integer primary key
);
