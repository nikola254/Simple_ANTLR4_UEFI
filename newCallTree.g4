grammar newCallTree;

start : efi_main ;

efi_main : ENTER_efi_main statement* EXIT_efi_main ; 

statement
    : functionCall  # FunctionCallStmt
    | variableDeclaration  # VariableDeclarationStmt
    | loopStatement  # LoopStatementStmt
    | returnStatement  # ReturnStatementStmt
    ;

functionCall : IDENTIFIER '(' argumentList? ')' ';' ;
variableDeclaration : TYPE IDENTIFIER ('=' expression)? ';' ;
loopStatement : 'while' '(' expression ')' '{' statement* '}' ;
returnStatement : 'return' expression? ';' ;

// Терминалы
ENTER_efi_main : '[ENTER] efi_main' ;
EXIT_efi_main : '[EXIT] efi_main' ;
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;
TYPE : 'int' | 'char' | 'void' | 'EFI_STATUS' ;
DIGIT : [0-9] ;  // ✅ Исправлено, теперь DIGIT определен как токен
argumentList : expression (',' expression)* ;
expression : IDENTIFIER | DIGIT+ ;  // Используем DIGIT здесь
WS : [ \t\r\n]+ -> skip ;
