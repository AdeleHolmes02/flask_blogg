INSERT INTO posts (title, body)
VALUES
('My First Flask Application', 'Building my first Flask application was one of the most important milestones in this project. I learned how routes connect URLs to Python functions and how Flask renders HTML templates. At first it felt difficult to understand how all the pieces worked together, but after creating multiple pages and testing different routes, I gained confidence in building web applications with Python.'),

('Learning SQLite Databases', 'This project introduced me to SQLite and relational databases. I learned how to create tables, insert records, update existing data, and retrieve information using SQL queries. Understanding how data is stored and connected was an important step in becoming more comfortable with backend development.'),

('Understanding CRUD Operations', 'CRUD stands for Create, Read, Update and Delete. These operations form the foundation of many web applications. In this project I implemented all four operations for blog posts. Building CRUD functionality helped me understand how applications interact with databases and user input.'),

('Working with Git and GitHub', 'Version control became an important part of my workflow during this project. Using Git allowed me to save progress through commits, while GitHub acted as a backup and collaboration platform. I learned how to stage changes, commit code, push updates, and keep track of project development over time.'),

('Debugging Flask Errors', 'Debugging was one of the most valuable learning experiences during development. I encountered errors such as missing return statements, route issues, template problems, and indentation mistakes. By reading error messages carefully and testing changes step by step, I improved my problem-solving skills and became more confident as a developer.'),

('Using Jinja Templates', 'Jinja templates made it possible to separate application logic from presentation. I used template inheritance to create a shared layout that could be reused across different pages. This reduced repetition and made the project easier to maintain and extend.'),

('Building a Comment System', 'The comment system allowed users to interact with blog posts. Implementing comments required creating relationships between database tables and displaying related information on the page. This feature helped me better understand foreign keys and database design principles.'),

('Adding Tags to Blog Posts', 'Tags improve organisation and make it easier to find related content. To implement this feature, I created a many-to-many relationship using a separate post_tags table. This was one of the most advanced database concepts I used in the project and gave me experience working with SQL JOIN queries.'),

('Writing Automated Tests', 'Testing helps ensure that applications continue to work as expected after changes are made. In this project I created automated tests for database functions and Flask routes. These tests verify important functionality and reduce the risk of introducing bugs when the application evolves.'),

('What I Learned from Backend Development', 'This project brought together many technologies and concepts, including Python, Flask, SQLite, HTML, CSS, Git, and testing. More importantly, it taught me how to approach problems systematically, debug issues effectively, and build complete applications from start to finish. The experience has given me a strong foundation for further studies in software and web development.');

INSERT INTO tags (name)
VALUES
('Flask'),
('Python'),
('SQLite'),
('Database'),
('CRUD'),
('Git'),
('GitHub'),
('Debugging'),
('Jinja'),
('Testing'),
('Backend'),
('Reflection');

INSERT INTO post_tags (post_id, tag_id)
VALUES
(1, 1),
(1, 2),
(1, 11),

(2, 3),
(2, 4),
(2, 11),

(3, 5),
(3, 1),
(3, 11),

(4, 6),
(4, 7),

(5, 8),
(5, 1),
(5, 2),

(6, 9),
(6, 1),

(7, 4),
(7, 1),
(7, 11),

(8, 3),
(8, 4),
(8, 11),

(9, 10),
(9, 2),

(10, 12),
(10, 11);

INSERT INTO comments (post_id, title, body)
VALUES
(1, 'Great milestone', 'Building the first Flask application is always exciting. It is impressive how quickly you can create dynamic web pages with only a few lines of code.'),
(1, 'Nice work', 'I like how this post explains the learning process. Flask is a great framework for understanding backend fundamentals.'),

(2, 'Databases are essential', 'Understanding databases is one of the most important backend skills. SQLite is a great place to start.'),
(2, 'Good explanation', 'The description of relational databases is clear and easy to understand.'),

(5, 'Been there', 'Debugging can be frustrating, but it is also one of the best ways to learn how an application really works.'),
(5, 'Helpful reflection', 'Learning to read error messages carefully is a skill that saves a lot of time in the long run.'),
(5, 'Good lesson', 'Every developer spends time debugging. It is great that you included what you learned from the process.'),

(9, 'Testing matters', 'Automated tests make projects more reliable and easier to maintain as they grow.'),
(9, 'Important practice', 'It is good to see testing included in a student project. Many projects skip this step.');