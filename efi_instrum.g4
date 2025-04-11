grammar efi_instrum;

start : main;

main :
    TRACE_ENTER1 efi_main TRACE_EXIT1;

efi_main :
    TRACE_ENTER2 waitForKey TRACE_EXIT2
    TRACE_ENTER3 conditionalBranch
    ( TRACE_ENTER4 bootkit_hook_call TRACE_EXIT4
    | TRACE_ENTER5 resetSystem_call TRACE_EXIT5 )
    TRACE_EXIT3;

waitForKey : ; 
conditionalBranch : ; 
bootkit_hook_call : ; 
resetSystem_call : ;

TRACE_ENTER1 : 'ENTER_main';
TRACE_EXIT1  : 'EXIT_main';
TRACE_ENTER2 : 'ENTER_key';
TRACE_EXIT2  : 'EXIT_key';
TRACE_ENTER3 : 'ENTER_conditional';
TRACE_EXIT3  : 'EXIT_conditional';
TRACE_ENTER4 : 'ENTER_hook';
TRACE_EXIT4  : 'EXIT_hook';
TRACE_ENTER5 : 'ENTER_reset';
TRACE_EXIT5  : 'EXIT_reset';

WS : [ \t\r\n]+ -> skip;
