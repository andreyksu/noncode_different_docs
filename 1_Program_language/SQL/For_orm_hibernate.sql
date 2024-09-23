CREATE TABLE public.matrix_message_room
(
  uuid_room character(255),
  uuid_message character(255),
  CONSTRAINT uuid_message_constr_first FOREIGN KEY (uuid_message)
      REFERENCES public.messages (uuid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT uuid_room_constr_second FOREIGN KEY (uuid_room)
      REFERENCES public.room (uuidroom) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.matrix_message_room
  OWNER TO testov;

Пустая

-----------------------------------------
CREATE TABLE public.matrix_message_user
(
  email_recipient character(255),
  uuid_message character(255),
  CONSTRAINT messageuuid_messages FOREIGN KEY (uuid_message)
      REFERENCES public.messages (uuid) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT recipient_principal FOREIGN KEY (email_recipient)
      REFERENCES public.principal (email) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.matrix_message_user
  OWNER TO testov;


-----------------------------------------
CREATE TABLE public.message_as_file
(
  author character(255) NOT NULL,
  uuid character(255) NOT NULL,
  nameoffile text,
  contentoffile bytea,
  messagedate timestamp without time zone DEFAULT now(),
  delited boolean DEFAULT false,
  CONSTRAINT author_principal FOREIGN KEY (author)
      REFERENCES public.principal (email) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT messages_uuid_for_message_as_file UNIQUE (uuid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.message_as_file
  OWNER TO testov;

-----------------------------------------
CREATE TABLE public.messages
(
  author character(255) NOT NULL,
  uuid character(255) NOT NULL,
  message text,
  messagedate timestamp without time zone DEFAULT now(),
  delited boolean DEFAULT false,
  is_file boolean DEFAULT false,
  CONSTRAINT author_principal FOREIGN KEY (author)
      REFERENCES public.principal (email) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT messages_uuid UNIQUE (uuid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.messages
  OWNER TO testov;

-----------------------------------------
CREATE TABLE public.person
(
  id bigint NOT NULL,
  person_name character(255) NOT NULL,
  person_old bigint NOT NULL,
  CONSTRAINT person_pkey PRIMARY KEY (id),
  CONSTRAINT pets_constr FOREIGN KEY (id)
      REFERENCES public.person (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.person
  OWNER TO testov;



-----------------------------------------

CREATE TABLE public.pets
(
  person_id bigint NOT NULL,
  pets_name character(255) NOT NULL,
  pets_old bigint NOT NULL,
  id bigint NOT NULL,
  CONSTRAINT pets_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.pets
  OWNER TO testov;


-----------------------------------------

CREATE TABLE public.principal
(
  email character(255) NOT NULL,
  password character(255) NOT NULL,
  name character(255) NOT NULL,
  regdata timestamp without time zone DEFAULT now(),
  isactive boolean DEFAULT true,
  isadmin boolean DEFAULT false,
  CONSTRAINT principal_pkey PRIMARY KEY (email)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.principal
  OWNER TO testov;



-----------------------------------------

CREATE TABLE public.room
(
  name character(255) NOT NULL,
  regdata timestamp without time zone DEFAULT now(),
  isactive boolean DEFAULT true,
  uuidroom character(255) NOT NULL,
  CONSTRAINT room_pkey PRIMARY KEY (name),
  CONSTRAINT room_uuidroom_key UNIQUE (uuidroom)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.room
  OWNER TO testov;


-----------------------------------------