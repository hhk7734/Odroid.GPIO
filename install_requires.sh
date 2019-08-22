#!/bin/sh

is_installed()
{
    [ -n "$(command -v "$1" 2>/dev/null)" ]
}

if ! (  ( is_installed gcc ) && ( is_installed git ) && ( is_installed swig ) ); then
    echo "\033[31m""\n============================================================\n""\033[0m"
    apt update
    apt install -y build-essential git swig
fi

if ! is_installed gpio; then
    echo "\033[31m""\n============================================================\n""\033[0m"
    if [ -e /tmp/wiringPi ]; then
        rm -r /tmp/wiringPi
    fi
    git clone https://github.com/hardkernel/wiringPi /tmp/wiringPi &&
    cd /tmp/wiringPi &&
    ./build
fi

if ! is_installed odroid-config; then
    echo "\033[31m""\n============================================================\n""\033[0m"
    if [ -e /tmp/odroid-config ]; then
        rm -r /tmp/odroid-config
    fi
    git clone https://github.com/hhk7734/odroid-config /tmp/odroid-config &&
    cd /tmp/odroid-config &&
    ./install.sh
fi

echo "\033[31m""\n============================================================\n""\033[0m"