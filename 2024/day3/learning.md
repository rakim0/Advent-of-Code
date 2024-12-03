Regex solution was pretty straightforward.

Learnt about lambdas, map, all function (lil bit about programming too (difference between foreach and for) from weeb server, thanks kagerou and middo)

all() -> returns true if all elements in the list are true
map(function, iterable) -> returns an iterator which can be converted to list.
for and foreach (for i in vec) loops -> foreach iterates through a list so changes to i does not persist where as regular in regular for loops it's incremented so we can just modify value (which is dangerous) and can lead to infinite loop.

for each i -> {1,2,3} after 1 it'll go 2 regardless of current value

So for each is better since we can avoid unintentional infinite loops.

Lambda functions are a bit complicated but my major use I think will
lambda x: x == 'a' or x == 'b'
and passing it into map.
