#### Назначение: динамически добавляет объекту новые возможности, приводящие к изменению его состояния и/или поведения. Является гибкой альтернативой порождению подклассов с целью расширения функциональности.

#### Участники:

• Component (Компонент) — определяет интерфейс для объектов, к которым могут быть динамически добавлены новые возможности;

• ConcreteComponent (Конкретный компонент) — определяет объект, к которому могут быть добавлены новые возможности;

• Decorator (Декоратор) — хранит ссылку на объект Component и определяет интерфейс, соответствующий интерфейсу Component;

• ConcreteDecoratorA и ConcreteDecoratorB (Конкретные декораторы) — добавляют к компоненту новые возможности, изменяющие его состояние и/или поведение.

#### Задание 1. Реализовать иерархию классов, которая включает абстрактный класс Component с абстрактным методом Operation (не имеет параметров, возвращает строку), абстрактный класс Decorator, который является потомком класса Component и содержит защищенное поле comp — ссылку на объект типа Component, и конкретные классы ConcreteComponent (потомок класса Component), ConcreteDecoratorA и ConcreteDecoratorB (потомки класса Decorator).

#### Класс ConcreteComponent содержит строковое поле text, которое инициализируется в конструкторе с помощью одноименного параметра. Метод Operation класса ConcreteComponent возвращает строку text.

#### Классы ConcreteDecoratorA и ConcreteDecoratorB имеют поле comp, являющееся ссылкой на объект типа Component; класс ConcreteDecoratorA содержит также символьное поле ch. В конструкторах классов ConcreteDecoratorA и ConcreteDecoratorB поля инициализируются с помощью одноименных параметров.

#### Метод Operation конкретного декоратора A возвращает строку, полученную путем добавления символа ch перед и после текста, возвращенного методом Operation объекта comp. Метод Operation конкретного декоратора B возвращает строку, полученную путем добавления символа «(» перед текстом, возвращенным методом Operation объекта comp, и символа «)» после этого текста. Таким образом, каждый декоратор изменяет поведение метода Operation исходного объекта Component, добавляя к возвращаемому значению дополнительный префикс и суффикс; при этом декоратор A корректирует состояние исходного объекта, путем добавления к нему поля ch.

#### Тестирование разработанной системы классов. Дан символ C, целое число N (≤ 9) и N пар строк (S, D), причем строка S является непустой, а строка D содержит только буквы «A» и «B» и может быть пустой. Создать набор из N объектов типа Component, формируя каждый элемент этого набора на основе соответствующей пары строк (S, D) следующим образом: вначале создать объект типа ConcreteComponent, вызвав его конструктор с параметром S, а затем последовательно применять к результирующему объекту декораторы A или В, причем количество и порядок декораторов определяется строкой D (например, в случае строки «AAB» к исходному объекту типа ConcreteComponent надо последовательно применить декораторы A, A и B). В качестве второго параметра конструктора всех декораторов A использовать исходный символ C.

#### Перебирая созданный набор из N объектов в обратном порядке, вызвать для каждого из них метод Operation и вывести его возвращаемое значение. 