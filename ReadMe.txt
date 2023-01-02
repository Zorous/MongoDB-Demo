_____________________________________________________________MONGODB___________________________________________


------------------------------------Creating DBs and Collections---------------------------------
use DBname : 
=> if the db exists it will use it, if the db doesn't exist it will create it then use it

db.CollectionName.insert() :
=> if there's a collection with that name it will insert inside it, and if there isn't it will create one with that name and insert inside it

db.CollectionName.insert({}) : 
=>we can insert only an object

db.CollectionName.insert([{},{},...]) : 
=> and we can insert an array that has many objects

db.CollectionName.find() :
=> it will return all the available objects inside the specified collection


-------------------------------Deleting Documents-----------------------

To Delete a document we could use deleteOne() or the deleteMany() method and specify which document we want to delete
the best way is using the _id field
exe : 
db.books.deleteOne({_id:ObjectId("63b2027627a83016e4f51212")})
>> One Object that has that Unique ID will be deleted

db.books.deleteMany({author : "Davenchi"})
>> all the objects that has "Davenchi" as a value to it's author key will be deleted



-------------------------------Updating Documents-----------------------
To update a document we can use updateOne() or updateMany()
with the updateMany() method, we could update so many documents that has a commune field at once
the 2 methods accepts two object arguments the first one where we specify the id of our document and the second one has the $set operator
and a pair of key values of the elements we want to change.
ex : 
1/
db.books.updateOne(
{_id:ObjectId("63b2027627a83016e4f51212")}, 
{$set : {title : "new title", author : "Nicolas"} }
)

2/
db.books.updateMany(
{author : "Oussama"}, 
{$set : {Description : "Made by Oussama"} }
)

--------------------FIND()--------------

find() accepts actually two parametres the first is the condition inside an object and the second is the returned fields and inside an object also
giving the field's name, 1 as a value that means it will return it full, and giving it 0 that means it will return the field empty
ex :  => db.CollectionName.find({},{name : 1,age:0})


db.CollectionName.find({name : "Oussama"}) :
=> it will return all the available objects inside the specified collection BUT with a condition like filtering

---------------------------------------------METHODS-------------------------------------------
There's various of other methods or pre-defined functions we could use along with find, like : 

* sort() : it accepts a parametre as an object and it's the field we want to sort with, if its value was 1 it will sort it ASC and if it was -1 it will be DESC
=> db.CollectionName.find().sort({name : 1})
>> (Objects with only the name fields)

* count() : count only returns the number (INT) of the returned fields
=> db.CollectionName.find().count()
>> 7 (number)

* limit(n) : it limits the number of the returned objects to on a specific number
db.CollectionName.find().limit(3)
>> (3 objects)

------------------------------------------OPERATORS---------------------------------------------

ALL THE OPERATORS STARTS WITH THE DOLLAR SIGN "$"

__________ GREAT THAN / LESS THAN Operators _________

$gt : greater than and we use it like that => db.CollectionName.find({rating : {$gt : 5}})
$lt : less than and we use it like that => db.CollectionName.find({rating : {$lt : 10}})

$gte : greater than OR EQUALS and we use it like that => db.CollectionName.find({rating : {$gte : 5}})
$lte : less than OR EQUALS and we use it like that => db.CollectionName.find({rating : {$lte : 10}})


__________OR and ALL Operatores______________

$or : it takes an array as a value and it will returns every satisfief condition, IT MUST BE USED AS THE FIRST ARGUMENT INSIDE FIND()
and we use it like that
=> db.CollectionName.find( { $or : [{rating : 8} , {rating : 9}    ] })

$all (AND) : it takes an array as a value also and it returns the objects where all the conditions are satisfied
and we use it like that
=> db.CollectionName.find({category : {$all : ["Magic","Fantasy"] } })

__________IN and NOT IN Operators__________

the both takes an Array as a value and we use them like that : 
db.CollectionName.find({rating : {$in : [7,8,9] } })
>> 7 8 9

db.CollectionName.find({rating : {$nin : [7,8,9] } })
>> ..6   10..

________INC /PULL / PUSH / EACH Operators_________
- INC is considered as an updating operator since it could make changes on the fields, so we use INC always along with the update methode
it's can increment a specific field with a specific pace we define

INC accepts an object as a parametre and it's the field's name as a key and the INCRIMENTATION's PACE as a value
example : 
db.CollectionName.upateOne(
{_id:ObjectId("63b2027627a83016e4f51212")}, 
{$inc : {popularity points : 100} }
)

- PULL also considered as an updating operator since it makes changes and we use it along with the update method too
and it's can pull, pop or delete a specific element in a specific object

example : 
db.CollectionName.upateOne(
{_id:ObjectId("63b2027627a83016e4f51212")}, 
{$pull : {category : "horror"} }
)

- PUSH ; just same as INC and PULL we use it along with the update method 
it can add or push a new element inside a specific object
example : 
db.CollectionName.upateOne(
{_id:ObjectId("63b2027627a83016e4f51212")}, 
{$push : {category : "horror"} }
)

- EACH ; we use it with the update method also and it allow us to push or add or make several actions at once
also it accepts an array as a parametre and the elements inside this array are the elements which will be added

example : 
db.CollectionName.upateOne(
{_id:ObjectId("63b2027627a83016e4f51212")}, 
{$push : {category : {$each : ["horror","adventure","slice of life"] } } }
)


--------------------------------------------NESTED DOCUMENTS-----------------------------------------------------------

Just like JSON we could use freely an array of objects inside our object, we call that  Nested Documents here
ex : 
{
"name" : "ex1",
"nested docs" : [
{"title" : "a","review" : "xx"},
{"title" : "b","review" : "yy"},
{"title" : "c","review" : "zz"},
]
}

_____________COMPLEX QUERIES________________________
we can make complexe queries and make conditions on the nested documents easily : 
ex : 
db.books.find({categories : "Fantasy"})
>> (it will return all the objects that has Fantasy as one of their categories)

db.books.find({categories : ["Fantasy"] })
>> (it will return all the objects that has Fantasy as it's ONE and ONLY ONE value)

and we can make a condition in any sub-field that way : 

db.books.find({"reviewers.name" : "Mordred"})
>> It will return every object that has Mordred as one of its REVIEWERS's NAME




To interact with the MongoDB databases we made from our Application we need to use Drivers
for each programming language there's a specific driver which refers to a specific language bindings









