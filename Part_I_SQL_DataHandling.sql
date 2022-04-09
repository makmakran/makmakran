/*Query #1*/
Select final.city, breakfast_basket, rest_basket efood_basket, breakfast_freq, rest_freq efood_freq, breakfast_Users3Freq, rest_Users3Freq efood_Users3Freq from (
Select br.city, breakfast_basket, breakfast_freq, breakfast_Users3Freq, rest_basket, rest_freq, rest_Users3Freq from 
(Select c.city, breakfast_basket, breakfast_freq, breakfast_Users3Freq from (Select city, (sum(amount)/count(order_id)) breakfast_basket, 
count(order_id)/count(distinct(user_id)) breakfast_freq 
FROM `efood2022-346516.main_assesment.orders`
where cuisine  like 'Breakfast'
group by city) c
left Join (Select a.city, (More_Than_3/All_Users) breakfast_Users3Freq   from (Select city, count(distinct(user_id)) All_Users from `efood2022-346516.main_assesment.orders` where cuisine  like 'Breakfast' group by city
) a
Left join (Select city, count(distinct(user_id)) More_Than_3 from `efood2022-346516.main_assesment.orders` where cuisine  like 'Breakfast' and user_id in (Select  user_id 
from `efood2022-346516.main_assesment.orders` 
where cuisine  like 'Breakfast'
group by user_id 
Having Count(user_id)>3) group by city) b
On a.city = b.city) d
on c.city = d.city) br 
Left Join (Select c.city, rest_basket, rest_freq, rest_Users3Freq from (Select city, (sum(amount)/count(order_id)) rest_basket, 
count(order_id)/count(distinct(user_id)) rest_freq 
FROM `efood2022-346516.main_assesment.orders`
group by city) c
left Join (Select a.city, (More_Than_3/All_Users) rest_Users3Freq   from (Select city, count(distinct(user_id)) All_Users from `efood2022-346516.main_assesment.orders`  group by city
) a
Left join (Select city, count(distinct(user_id)) More_Than_3 from `efood2022-346516.main_assesment.orders` where  user_id in (Select  user_id 
from `efood2022-346516.main_assesment.orders` 
group by user_id 
Having Count(user_id)>3) group by city) b
On a.city = b.city) d
on c.city = d.city) rest
On br.city = rest.city
where br.city in (SELECT city
from `efood2022-346516.main_assesment.orders` 
group by city 
HAVING count(city) >1000)) final 
Left Join (SELECT city, count(order_id) Total_Orders
from `efood2022-346516.main_assesment.orders` 
Where cuisine like 'Breakfast'
group by city ) ord
On final.city=ord.city
order by Total_Orders Desc Limit 5


/*Query #2*/
select a.city, sum(TTLOrders) AllTotalOrders, sum(Top10TotalOrders) Top10,sum(Top10TotalOrders)/ sum(TTLOrders) * 100 ContributionOfTop10inTTL from 
(Select city, count(user_id) TTLOrders from `efood2022-346516.main_assesment.orders`  group by city  
)a 
LEFT JOIN (Select city, sum(Total_Orders) Top10TotalOrders from (
select *
from
(
     select city, 
            user_id,
            row_number() over(partition by city order by count(user_id) desc) as ranking , count(order_id) Total_Orders
     from `efood2022-346516.main_assesment.orders`  
     group by city, user_id 
) temp
where ranking between 1 and 10
)
group by city) b
on a.city = b.city
group by city
