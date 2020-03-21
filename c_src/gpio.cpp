#include <pybind11/pybind11.h>
#include <wiringPi.h>

namespace py = pybind11;

extern struct libodroid libwiring;

PYBIND11_MODULE(_GPIO, m) {
    m.def("wiringPiSetup", &wiringPiSetup)
        .def("wiringPiSetupGpio", &wiringPiSetupGpio)
        .def("wiringPiSetupPhys", &wiringPiSetupPhys)
        .def("getModePinToGpio",
             [](int pin) {
                 return libwiring.getModeToGpio(libwiring.mode, pin);
             })
        .def("pinMode", &pinMode)
        .def("digitalRead", &digitalRead)
        .def("digitalWrite", &digitalWrite);
}