-- Active: 1662625253896@@127.0.0.1@3306

### membuat table berisi Kolom ID, tweet sebelum diklining, tweet setelah diklining ###
create table tweet
(tweet_id INTEGER PRIMARY KEY AUTOINCREMENT, tweet_kotor text, tweet_bersih text);

select * from tweet;