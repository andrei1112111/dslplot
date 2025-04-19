grammar GraphPlot;

parse       : statement+ EOF ;


statement
    : plotStatement
    | configStatement
    | labelStatement
    | styleStatement
    | scaleStatement
    | subplotStatement
    | saveStatement
    ;


plotStatement
    : 'PLOT' dimension chartType dataSpec plotOptions?
    ;

configStatement
    : 'SET' configKey '=' configValue
    ;

labelStatement
    : 'LABEL' labelType STRING
    ;

styleStatement
    : 'STYLE' styleKey '=' styleValue
    ;

scaleStatement
    : 'SCALE' axis '=' scaleType
    ;

subplotStatement
    : 'SUBPLOT' 'GRID' gridSize
    | 'SUBPLOT' 'SELECT' position
    ;

saveStatement
    : 'SAVE' 'AS' STRING
    ;

dimension
    : '1D'
    | '2D'
    ;

chartType
    : 'LINE'
    | 'SCATTER'
    | 'BAR'
    | 'HIST'
    | 'PIE'
    | 'BOX'
    | 'HEATMAP'
    ;

dataSpec
    : LBRACE IDENTIFIER (',' IDENTIFIER)* RBRACE
    ;


plotOptions
    : '(' option (',' option)* ')'
    ;

option
    : IDENTIFIER '=' value
    ;

value
    : NUMBER
    | STRING
    | IDENTIFIER
    ;

axis
    : 'X'
    | 'Y'
    ;

scaleType
    : 'LINEAR'
    | 'LOG'
    ;

gridSize
    : NUMBER 'x' NUMBER
    ;

position
    : NUMBER ',' NUMBER
    ;

labelType
    : 'TITLE'
    | 'X'
    | 'Y'
    ;

configKey
    : 'FIGSIZE'
    | 'THEME'
    | 'GRID'
    ;

configValue
    : STRING
    | NUMBER
    ;

styleKey
    : 'COLOR'
    | 'LINESTYLE'
    | 'MARKER'
    ;

styleValue
    : STRING
    ;


LBRACE : '{' ;
RBRACE : '}' ;
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING      : '"' (~["\\] | '\\' .)* '"' ;
NUMBER      : '-'? [0-9]+ ('.' [0-9]+)? ;
WS          : [ \t\r\n]+ -> skip ;
