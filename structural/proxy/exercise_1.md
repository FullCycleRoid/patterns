#### Задание 1. Реализовать иерархию классов, включающую абстрактный класс Subject с абстрактными методами RequestA, RequestB, RequestC, RequestD и конкретные классы RealSubject и Proxy — потомки класса Subject. Указанные методы не имеют параметров и возвращают строку. Класс RealSubject не имеет полей, его методы возвращают строки «A (Real)», «B (Real)», «C (Real)», «D (Real)».

#### Класс Proxy является заместителем класса RealSubject, комбинирующим черты виртуального и защищающего заместителя. Предполагается, что запросы A и B являются простыми и могут быть реализованы в самом заместителе, в то время как запросы C и D являются сложными и доступны только в классе RealSubject. Кроме того, запросы A и C являются безопасными, а запросы B и D — потенциально опасными, и в некоторых ситуациях их целесообразно заблокировать. Поэтому класс Proxy содержит два логических поля: deferredMode (отложенный режим) и protectedMode (защищенный режим), которые задаются в его конструкторе с помощью одноименных параметров и определяют его поведение по отношению к реальному субъекту. Кроме того, класс Proxy содержит поле rsubj — ссылку на объект типа RealSubject.

#### Если поле deferredMode равно False, то объект RealSubject создается в конструкторе класса Proxy (и связывается со ссылкой rsubj), если deferredMode равно True, то начальное значение ссылки rsubj является пустым. Если поле protectedMode равно False и при этом ссылка rsubj не является пустой, то все запросы переадресуются объекту, на который ссылается rsubj. Если protectedMode равно False, а ссылка rsubj является пустой, то простые запросы A и B выполняются самим объектом Proxy и при этом возвращаются строки «A (Proxy)» и «B (Proxy)», а в случае вызова запроса C или D объект RealSubject создается и связывается со ссылкой rsubj, после чего этот запрос переадресуется ему. Если protectedMode равно True, то выполнение запросов A и C не отличается от ранее описанного, а при попытке вызова запросов B и D они отменяются (независимо от значения ссылки rsubj), причем соответствующие методы возвращают строки «B denied» и «D denied».

#### Тестирование разработанной системы классов. Дан набор из трех целых чисел, принимающих значения от −1 до 3, и строка, содержащая только символы «A», «B», «C», «D» — имена запросов. Создать массив из трех ссылочных элементов типа Subject, инициализировав элементы конкретными объектами в зависимости от значения исходных чисел: −1 — RealSubject, 0 — Proxy(False, False), 1 — Proxy(True, False), 2 — Proxy(False, True), 3 — Proxy(True, True). Для каждого из созданных объектов выполнить набор запросов, определяемый исходной строкой, и вывести результат, возвращаемый каждым запросом. 