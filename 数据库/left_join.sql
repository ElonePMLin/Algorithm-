-- left join table on condition1(xxx = yyy)
-- finally do not miss the ";"

select firstName, lastName, city, state from Person
    left join Address
        on Address.personId = Person.personId;
