
### Ключевые слова nonlocal и global
Начнем с переменных в области видимости объемлющих (внешних) функций. Для доступа к именам из
области видимости вложенной функции не нужно ничего делать. Но для изменения этих переменных
необходим оператор `nonlocal`.

Запустите код, посмотрите на результат. Если во второй функции вместо `nonlocal` написать 
`global`, то
изменится значение переменной `x`, лежащей в глобальной области видимости. Проделайте это
самостоятельно :)
>По возможности, старайтесь не использовать глобальные перменные. Если сначала их 
> использование кажется логичным и удобным, то при росте проекта они могут привести к следующей куче проблем: нарушение инкапсуляции, сложности в модульном тестировании, ухудшение читаемости кода и т.д.
