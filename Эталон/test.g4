grammar test;

start: body exit <EOF> ;

body: variable+ ;

variable: type IDENTIFIER ;

IDENTIFIER: [A-Z]+ { log("matched rule"); } ;

exit: return ;

// Rule
type : int #typeInt
| short #typeShort
| long #typeLong
| string #typeString
;
// Tokens
int : 'int' ;
short : 'short' ;
long : 'long' ;
string : 'string' ;

return: 'return' ;