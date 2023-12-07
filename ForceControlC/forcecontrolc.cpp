#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cstdlib>
#include <Windows.h>

PROCESS_INFORMATION pi;
void terminate_child_process();
void spawn_process(const std::string& command_line);
BOOL WINAPI ctrl_handler(DWORD fdwCtrlType);

int main(int argc, char** argv) {
    SetConsoleCtrlHandler(ctrl_handler, TRUE);

    std::stringstream ss;
    for (int i=1; i<argc; ++i) {
        ss << argv[i] << " ";
    }

    spawn_process(ss.str());
}

void spawn_process(const std::string& command_line) {
    memset(&pi, 0, sizeof(PROCESS_INFORMATION));

    STARTUPINFOA si;
    memset(&si, 0, sizeof(STARTUPINFOA));

    bool ret = CreateProcessA(
        nullptr,
        const_cast<char*>(command_line.c_str()),
        nullptr,
        nullptr,
        false,
        0,
        nullptr,
        nullptr,
        &si,
        &pi
    );

    if (!ret) {
        std::cerr << "[-] Creating process failed." << std::endl;
        return;
    }

    WaitForSingleObject(pi.hProcess, INFINITE);

    DWORD exit{};
    GetExitCodeProcess(pi.hProcess, &exit);
    TerminateProcess(GetCurrentProcess(), exit);
}

void terminate_child_process() {
    std::cout << "[+] Quitting ..." << std::endl;
    if (pi.hThread) {
        TerminateProcess(pi.hProcess, 777);
    }
}


BOOL WINAPI ctrl_handler(DWORD fdwCtrlType) {
    switch (fdwCtrlType) {
    case CTRL_C_EVENT:
        terminate_child_process();
        return TRUE;
        default: return FALSE;
    }
}