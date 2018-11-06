#include <idc.idc>
static main() {
auto i;
auto a = 0x201020;
for (i = 0; i <= 54; i = i + 2) {
    Message("%c", Byte(a));
    a = a +2;
}

}