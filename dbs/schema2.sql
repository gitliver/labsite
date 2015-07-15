drop table if exists motor;
create table motor (
  id integer primary key autoincrement,
  Gene text not null,
  Cells integer not null,
  Mean real not null,
  Min real not null,
  Max real not null,
  Connectivity real not null,
  p_value real not null,
  BH_p_value real not null,
  Centroid real not null,
  Dispersion real not null,
  RNA_binding text not null,
  Splicing text not null,
  Surface text not null,
  Transcription text not null
);
