Create View artistinfo
as select Name, email, user_name, phone,  style_of_art, count(artwork.artist_id), count(sales.art_id) 
from artist
natural left join artwork natural left outer join sales group by artist.Artist_id;


Create View customer_info
as select name, email, user_name, phone, address, sum(price) 
from customer natural left outer join sales natural left outer join artwork
group by customer.Customer_id;
