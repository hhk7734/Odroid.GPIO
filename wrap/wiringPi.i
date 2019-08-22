%module GPIO

%{
    #include <wiringPi.h>
%}

extern int wiringPiSetup( void );
extern int wiringPiSetupGpio( void );
extern int wiringPiSetupPhys( void );

extern void pinMode( int pin, int mode );
extern int  digitalRead( int pin );
extern void digitalWrite( int pin, int value );