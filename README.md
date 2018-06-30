

# A simple web application combining Django framework and MySQL database

The purpose of this project is to create a database with three tables and fetching the data from the table with the connections.With this action someone can understand which user has which occupation.
You can see the tables below:
*  **User** table
* **occupations** table
* **userhasoccupation** table

## SQL commands for db structure
```sql

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (`user_id`, `name`) VALUES
(1, 'Maria'),
(2, 'Giorgos'),
(3, 'Thodoris'),
(4, 'Dafni');

ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);
  
  -----------------------------------------------------------------------------------------
  
  CREATE TABLE `occupations` (
  `occup_id` int(11) NOT NULL,
  `occupation` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `occupations` (`occup_id`, `occupation`) VALUES
(1, 'Programmer'),
(2, 'Marketing Executive'),
(3, 'Pharmacist'),
(4, 'Lead Developer');

ALTER TABLE `occupations`
  ADD PRIMARY KEY (`occup_id`);
  
  -----------------------------------------------------------------------------------------
  
  CREATE TABLE `userhasoccupations` (
  `connection_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `occup_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `userhasoccupations` (`connection_id`, `user_id`, `occup_id`) VALUES
(1, 1, 3),
(2, 2, 1),
(3, 3, 4),
(4, 4, 2);

ALTER TABLE `userhasoccupations`
  ADD PRIMARY KEY (`connection_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `occup_id` (`occup_id`);
  
```

## Result Image
![result image](https://github.com/TopFlankerKiller/django_mysql_example/blob/master/results.png)


## Important links

* Django documentation [here](https://docs.djangoproject.com/en/2.0/)
* XAMPP installation [here](https://www.apachefriends.org/index.html)

## Installation

Clone the Github repository and contribute.
```
$ https://github.com/TopFlankerKiller/django_mysql_example.git
```


