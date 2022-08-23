-- create user
-- birinchi bo'lib 
create user data with password '1';

-- create database 
create database data

-- create role 
alter role user with createdb superuser;

-- connect database 
\c databasename -- connect database

-- shuw users userlarni ko'rish kamandasi
select current_user;

-- show database;
\l -- databaselarni ko'rish kamandasi

-- delete user
drop user userName

-- delete database;
drop database databasename

-- git conflig berishi
<h1>Git bilan ishlayotganda</h1>
<!-- agarda bitta fileda ikkita odam ishalayotgan bulsa 
    va ikkalsi ham bitta joyni o'zgartirsa git comflig beradi 
    buni oldini olish uchun alohida faylda ishlagan maqul birinchidan 
    lekin shunday bulib qolsa 
-->
<h3>git checkout --theirs .</h3>
<h3>git checkout --ours .</h3>
<!-- tanlash kerak buladi -->
