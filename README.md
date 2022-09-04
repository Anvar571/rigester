### Python orqali user registratsiya PostgreSQL bilan
-- create user
-- birinchi bo'lib 
<h5>create user data with password '1';<h5>

-- create database 
<h5>create database data</h5>

-- create role 
<h5>alter role user with createdb superuser;</h5>

-- connect database 
<h5>\c databasename -- connect database</h5>

-- shuw users userlarni ko'rish kamandasi
<h5>select current_user;</h5>

-- show database;
<h5>\l -- databaselarni ko'rish kamandasi</h5>

-- delete user
<h5>drop user userName</h5>

-- delete database;
<h5>drop database databasename</h5>

-- git conflig berishi
<h1>Git bilan ishlayotganda</h1>
<h4> 
Agarda bitta fileda ikkita odam ishalayotgan bulsa 
va ikkalsi ham bitta joyni o'zgartirsa git comflig beradi 
buni oldini olish uchun alohida faylda ishlagan maqul birinchidan 
lekin shunday bulib qolsa 
</h4>
<h3>git checkout --theirs .</h3>
<h3>git checkout --ours .</h3>
<p> tanlash kerak buladi </p>
