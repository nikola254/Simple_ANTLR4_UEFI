grammar UEFI;

// Единица компиляции EOF - end of file конец всего
compilationUnit
    : (statement | functionDeclaration)* EOF
    ;

// Определение возможных операторов
statement
    : includeStatement
    | variableDeclaration
    | expressionStatement
    | comment
    | whileStatement
    ;

// Определение директивы включения
includeStatement
    : '#include' STRING
    ;

// Объявление переменной
variableDeclaration
    : type cursor identifier ('=' expression)? ';'
    | type identifier ('=' expression)? ';' // без указателя
    ;

// Определение функции
functionDeclaration
    : type macros? identifier '(' parameterList ')' block
    ;

// Список параметров функции
parameterList
    : parametr (',' parametr)*
    ;

// Определение параметров
parametr
    : type identifier
    | type cursor
    ;

// Определение блока кода
block
    : '{' statement* exit '}'
    | '{' warning? statement* exit '}'
    | ';'
    ;

// Предупреждение в коде
warning
    : '(' type ')' identifier ';' 
    ;

// Оператор выражения
expressionStatement
    : expression ';'
    ;

// Определение выражения
expression
    : assignmentExpression
    | methodCall 
    | literal
    | identifier
    | link
    | cursor
    | type
    ;

// Присваивание
assignmentExpression
    : identifier '=' expression
    ;

// Вызов метода
methodCall
    : identifier ('.' identifier | '->' identifier)* '(' argumentList? ')'
    ;

// Список аргументов для метода
argumentList
    : expression (',' expression | '->' expression)*
    ;


// Цикл while
whileStatement
    : 'while' '(' methodCall condition type')' ';'
    ;

condition
    : operator 
    ;

// Завершение функции
exit
    : 'return' (type | identifier) ';'
    ;

// Логические операторы
operator
    : '<'
    | '>' 
    | '==' 
    | '!=' 
    | '>=' 
    | '<=' 
    ;   

// Литералы
literal
    : STRING
    | CHAR_LITERAL
    | INT_LITERAL
    | FLOAT_LITERAL
    ;

// Типы данных
type
    : 'void'
    | 'EFI_STATUS'
    | 'EFI_HANDLE'
    | 'EFI_SYSTEM_TABLE'
    | 'EFI_INPUT_KEY'
    | 'EFI_TEXT_ATTR'
    | 'EFI_SUCCESS'
    | 'UINTN'
    | 'CHAR16'
    | 'CHAR8'
    | 'NULL'
    | 'EFI_YELLOW'
    | 'EFI_GREEN'
    | 'EFI_RED'
    | 'EFI_BLACK'
    | 'EfiResetShutdown'
    ;

// Идентификаторы
identifier
    : IDENTIFIER
    | type
    ;

// Макросы
macros
    : IDENTIFIER
    ;

// Указатели
cursor
    : '*' IDENTIFIER
    | '*' type
    ;

// Ссылки
link
    : '&' IDENTIFIER
    ;

// Комментарии
comment
    : '//' ~('\r' | '\n')* // однострочный комментарий
    | '/*' .*? '*/' // многострочный комментарий
    ;

// Лексические правила
STRING
    : ('u')?'"' ( ~["\\] | '\\' . )* WS?'"' // любой символ, кроме двойной кавычки и обратной косой черты
    ;

CHAR_LITERAL
    : '\'' . '\''
    ;

INT_LITERAL
    : [0-9]+
    ;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]*
    ;

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Пробелы и символы новой строки
WS  
    : [ \t\r\n]+ -> skip
    ;