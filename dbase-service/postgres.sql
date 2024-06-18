CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

INSERT INTO users (id, name)
VALUES
    (1, 'Record1'),
    (2, 'Record2'),
    (3, 'Record3'),
    (4, 'Record4'),
    (5, 'Record5'),
    (6, 'Record6'),
    (7, 'Record7'),
    (8, 'Record8'),
    (9, 'Record9'),
    (10, 'Record10'),
    (31, 'Record31'),
    (32, 'Record32'),
    (33, 'Record33'),
    (34, 'Record34'),
    (35, 'Record35'),
    (36, 'Record36'),
    (37, 'Record37'),
    (38, 'Record38'),
    (39, 'Record39'),
    (40, 'Record40');

INSERT INTO clients (id, name)
VALUES
    (11, 'Record11'),
    (12, 'Record12'),
    (13, 'Record13'),
    (14, 'Record14'),
    (15, 'Record15'),
    (16, 'Record16'),
    (17, 'Record17'),
    (18, 'Record18'),
    (19, 'Record19'),
    (20, 'Record20'),
    (41, 'Record41'),
    (42, 'Record42'),
    (43, 'Record43'),
    (44, 'Record44'),
    (45, 'Record45'),
    (46, 'Record46'),
    (47, 'Record47'),
    (48, 'Record48'),
    (49, 'Record49'),
    (50, 'Record50');

INSERT INTO customers (id, name)
VALUES
    (21, 'Record21'),
    (22, 'Record22'),
    (23, 'Record23'),
    (24, 'Record24'),
    (25, 'Record25'),
    (26, 'Record26'),
    (27, 'Record27'),
    (28, 'Record28'),
    (29, 'Record29'),
    (30, 'Record30'),
    (51, 'Record51'),
    (52, 'Record52'),
    (53, 'Record53'),
    (54, 'Record54'),
    (55, 'Record55'),
    (56, 'Record56'),
    (57, 'Record57'),
    (58, 'Record58'),
    (59, 'Record59'),
    (60, 'Record60');

