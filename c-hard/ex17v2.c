#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>



struct Address {
	// id gives the index of the row of one address?
	int id;
	//set is a boolean so we know if a given address is set or not
	int set;

	char *name;
	char *email;

};

struct Database {
	struct Address **rows;
	int MAX_DATA;
	int MAX_ROWS;
	};

struct Connection {

	FILE *file;
	struct Database *db;
};


void Database_close(struct Connection *conn);

void die(const char *message, struct Connection *conn)
{
	if (conn){
		Database_close(conn);
	}
	if (errno) {
		perror(message);
	} else {
		printf("ERROR: %s\n", message);
	}
	exit(1);
}

void Address_print(struct Address *addr)
{
	printf("%d %s %s\n", addr->id, addr->name, addr->email);
}

void Database_load(struct Connection *conn)
{
	int rc = fread(conn->db, sizeof(struct Database), 1, conn->file);
	  if(rc != 1)
		die("Failed to load database.", conn);
}

struct Connection *Database_open(const char *filename, char mode)
{
	struct Connection *conn = malloc(sizeof(struct Connection));
	if(!conn)
		die("Memory error", conn);

	conn->db = malloc(sizeof(struct Database));




	if (!conn->db)
		die("Memory error", conn);

	if (mode == 'c') {
		conn->file = fopen(filename, "w");
	} else {
		conn->file = fopen(filename, "r+");

		if (conn->file) {
			Database_load(conn);
		}
	}

	if (!conn->file)
		die("Failed to open the file", conn);

	return conn;
}

void Database_close(struct Connection *conn)
{
	if (conn) {
		if (conn->file)
			fclose(conn->file);
		if (conn->db)
			free(conn->db);
		free(conn);
	}
}

void Database_write(struct Connection *conn)
{
	rewind(conn->file);

	int rc = fwrite(conn->db, sizeof(struct Database), 1, conn->file);
	if (rc != 1)
		die("Failed to write database.", conn);

	rc = fflush(conn->file);
	if (rc == -1)
		die("Cannot flush database.", conn);
}

void Database_create(struct Connection *conn, int max_data, int max_rows)
{
	conn->db->MAX_DATA = max_data;
	conn->db->MAX_ROWS = max_rows;
	int i =0;

	for (i=0; i<conn->db->MAX_ROWS; i++) {
		//make a prototyoe to initialize it
		struct Address *addr = malloc(sizeof(struct Address));
		conn->db->rows[i] = malloc(sizeof(addr));

		addr->id =  i;
		addr->set = 0;
		//then just assign it

		conn->db->rows[i] = addr;
	}
}

void Database_set(struct Connection *conn, int id, const char *name, const char *email)
{
	struct Address *addr = conn->db->rows[id];
	if (addr->set)
		die("Already set, delete it first", conn);

	addr->set = 1;
	addr->name[conn->db->MAX_DATA-1]='\0';
	// WARNING: bug, read the "HOW TO BREAK IT" and fix this
	char *res = strncpy(addr->name, name,conn->db->MAX_DATA-1);
	//demonstrate strncpy bug
	if (!res)
		die("Name copy failed", conn);
	addr->email[conn->db->MAX_DATA-1]='\0';
	res = strncpy(addr->email, email,conn->db->MAX_DATA-1);

	if (!res)
		die("Email copy failed", conn);
}

void Database_get(struct Connection *conn, int id)
{
	struct Address *addr = conn->db->rows[id];

	if (addr->set) {
		Address_print(addr);
	} else {
		die("ID is not set", conn);
	}
}

void Database_delete(struct Connection *conn, int id)
{
	struct Address addr = {.id = id, .set = 0};
	conn->db->rows[id] = &addr;
}

void Database_list(struct Connection *conn)
{
	int i = 0;
	struct Database *db = conn->db;

	for (i=0; i<conn->db->MAX_ROWS; i++) {
		struct Address *cur = db->rows[i];

		if (cur->set) {
			Address_print(cur);
		}
	}
}

int main(int argc, char *argv[])
{
	int max_data = 0;
	int max_rows =0;
	if (argc < 3)
		die("USAGE: ex17 <dbfile> <action> [action params]", NULL);

	char *filename = argv[1];
	char action = argv[2][0];
	struct Connection *conn = Database_open(filename, action);
	int id = 0;

	if (argc > 3) id = atoi(argv[3]);
	/* if (id >=conn->db->MAX_ROWS) die("There's not that many records.", conn); */

	switch (action) {
		case 'c':
			if (argc != 5)
				die("Need max data and max rows", NULL);

			max_data = atoi(argv[3]);
			max_rows = atoi(argv[4]);
			Database_create(conn, max_data, max_rows);
			Database_write(conn);
			break;

		case 'g':
			if (argc != 4)
				die("Need an id to get", conn);

			Database_get(conn, id);
			break;

		case 's':
			if (argc != 6)
				die("Need id, name, email to set", conn);

			Database_set(conn, id, argv[4], argv[5]);
			Database_write(conn);
			break;

		case 'd':
			if (argc != 4)
				die("Need id to delete", conn);

			Database_delete(conn, id);
			Database_write(conn);
			break;

		case 'l':
			Database_list(conn);
			break;
		default:
			die("Invalid action: c=create, g=get, s=set, d=del. l=list", conn);
	}

	Database_close(conn);

	return 0;
}


