#!/bin/sh

set -e

is_installed()
{
    [ -n "$(command -v "$1" 2>/dev/null)" ]
}

if ! (  ( is_installed gcc ) && ( is_installed git ) && ( is_installed swig ) && ( is_installed gpio ) ); then
    echo "\033[31m""\nSwig, odroid-wiringpi, and etc\n""\033[0m"
    add-apt-repository ppa:hardkernel/ppa
    apt update
    apt install -y build-essential swig odroid-wiringpi libwiringpi-dev
fi

if ! is_installed odroid-config; then
    echo "\033[31m""\nodroid-config installation\n""\033[0m"
    echo "Not yet supported."
fi

echo "\033[31m""\n============================================================\n""\033[0m"
