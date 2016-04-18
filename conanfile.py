from conans import ConanFile
import os

class UtfCppConan(ConanFile):
    name = "utfcpp"
    version = "2.3.4"
    generators = "cmake"
    url="https://github.com/tyroxx/utfcpp"
    license="Boost"
    exports="source/*"

    def package(self):
        self.copy(pattern="*.h", dst="include", src="source", keep_path=True)
