import re

class X:

#ifdef _WIN32
    def windows_only(self):
        return 5
#else
    def unix_only(self):
        return 6
#endif


#ifdef DEBUG
debug = 25
#endif
