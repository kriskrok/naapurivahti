# Incantations for schema, invoke at your own risk. 
###################################################

CREATE TABLE [IF NOT EXISTS] Account {
  user_id SERIAL PRIMARY KEY,
  email VARCHAR ( 255 ) UNIQUE NOT NULL,
  username VARCHAR ( 63 ) UNIQUE NOT NULL,
  password VARCHAR (255 ) NOT NULL,
  role SMALLINT NOT NULL,
  created_on TIMESTAMP NOT NULL,
  last_login TIMESTAMP
};

CREATE TABLE [IF NOT EXISTS] Guardshift {
  shift_id SERIAL PRIMARY KEY,
  date DATE NOT NULL,
  start_time TIMESTAMPZ,
  end_time TIMESTAMPZ
};

CREATE TABLE [IF NOT EXISTS] Report {
  report_id SERIAL PRIMARY KEY,
  shift_id INT,
  creator_id INT NOT NULL,
  comments TEXT,
  finished BOOLEAN,
  FOREIGN KEY (shift_id)
      REFERENCES Guardshift (shift_id),
  FOREIGN KEY (creator_id)
      REFERENCES Account (user_id)
};

CREATE TABLE [IF NOT EXISTS] Picture {
  picture_id SERIAL PRIMARY KEY,
  observation_id INT,
  user_id INT,
  name TEXT,
  data BYTEA,
  FOREIGN KEY (observation_id)
      REFERENCES Observation (observation_id),
  FOREIGN KEY (user_id)
      REFERENCES Account (user_id)
};


CREATE TABLE [IF NOT EXISTS] Observation {
  observation_id SERIAL PRIMARY KEY,
  report_id INT,
  author_id INT,
  timing TIMESTAMPZ,
  comment TEXT,
  requires_action BOOLEAN,
  FOREIGN KEY (report_id)
      REFERENCES Report (report_id),
  FOREIGN KEY (author_id)
      REFERENCES Account (user_id)
};

CREATE TABLE [IF NOT EXISTS] shiftMembers {
  member_id INT NOT NULL,
  shift_id INT NOT NULL,
  FOREIGN KEY (member_id)
      REFERENCES Account (user_id),
  FOREIGN KEY (shift_id)
      REFERENCES Guardshift (shift_id)
};
