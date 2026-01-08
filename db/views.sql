create view vw_not_returned 
as
select m.name, m.surname, b.title, c.status, l.due_date from loans l 
join members m on m.id = l.member_id
join copies c on c.id = l.copy_id
join books b on b.id = c.book_id
where l.return_date is null;
    

create view vw_book_stat as
select
    b.title,
    count(l.id) AS amount_of_loans
from loans l
join copies c on c.id = l.copy_id
join books b on b.id = c.book_id
where l.return_date is null
group by b.title