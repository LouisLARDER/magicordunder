# dunder or magic dounble underscore
from todo import Todo

k_todo = Todo(name='louis')
e_todo = Todo(name= 'loulou')

k_todo.add('buy milk')
k_todo.add('look for clothes')
k_todo.add('finish coding')
k_todo.add('have fun')
k_todo.add('buy stuff')



print(len(k_todo))
print(k_todo)
print(e_todo)
print(k_todo < e_todo)
print(k_todo > e_todo)
