%module GPIO

%{

#include <wiringPi.h>

extern struct libodroid libwiring;

int getModePinToGpio( int pin )
{
    return libwiring.getModeToGpio( libwiring.mode, pin );
}

%}

extern int wiringPiSetup( void );
extern int wiringPiSetupGpio( void );
extern int wiringPiSetupPhys( void );

int getModePinToGpio( int pin );

extern void pinMode( int pin, int mode );
extern int  digitalRead( int pin );
extern void digitalWrite( int pin, int value );