drop table if exists people;
create table people (
  id integer primary key autoincrement,
  iscurrent integer not null,
  name text not null,
  title text not null,
  bio text not null,
  email text,
  imagefile text,
  webpage text
);

drop table if exists publications;
create table publications (
  id integer primary key autoincrement,
  ishightlight integer,
  year integer not null,
  title text not null,
  authors text not null,
  journal text not null,
  journal2 text,
  doi text,
  doi2 text,
  authors_first text,
  authors_corresponding text,
  journal_url text,
  journal_url2 text,
  notes text
);

drop table if exists press;
create table press (
  id integer primary key autoincrement,
  year integer not null,
  mytext text not null,
  title text,
  journal_url text
);
