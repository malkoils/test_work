**Hello there , some recrut scripts**

it turns out that the automation task was optional, but I just forgot to read to the end and started to initially make an automated script in order 

Additional task. Automation system.

**my notes**

deposit 
part_number;deposit

data
part_number;manufacturer;main_part_number;category;origin

price
part_number;price

quantity
part_number;quantity;warehouse

weight
part_number  weight_unpacked  weight_packed



https://www.w3schools.com/mysql
main_part_number manufacturer category origin price deposit(if no,then 0) final_price(deposit+price, if <2.00 then no show) quantity(if 0 then not display) filter by warehouse with code A,H,J,3,9



ALTER TABLE quantity MODIFY quantity  INT(5);
ALTER TABLE deposit MODIFY deposit  INT(5) ;
ALTER TABLE price MODIFY price  INT(5) ;

SELECT data.main_part_number,data.manufacturer,data.category,data.origin,price.price,IFNULL(deposit.deposit,0) as deposit,(price.price + deposit.deposit) as final_price ,quantity.quantity,quantity.warehouse FROM data INNER JOIN price ON data.part_number=price.part_number INNER JOIN deposit ON data.part_number=deposit.part_number INNER JOIN quantity ON data.part_number=quantity.part_number WHERE (price.price + deposit.deposit)>2.00 and quantity.quantity > 0 AND quantity.warehouse LIKE 'A' OR quantity.warehouse LIKE 'h' OR quantity.warehouse LIKE 'j' OR quantity.warehouse LIKE '3' OR quantity.warehouse LIKE '9';
  

and quantity.warehouse LIKE '[AHJ39]%'
