#include <iostream>
#include <sstream>

#include <Windows.h>

void fatal(const std::string& err, int exit_code=-1) {
    MessageBoxA(nullptr, err.c_str(), "SilentExecute", MB_OK);
}

void run_process(const std::string& args) {
    PROCESS_INFORMATION pi{};
    STARTUPINFOA si{};

    /* Maybe unnecessary */
    si.hStdOutput = nullptr;
    si.hStdInput = nullptr;
    si.hStdError = nullptr;
    si.wShowWindow = SW_HIDE;
    si.dwFlags = STARTF_USESTDHANDLES|STARTF_USESHOWWINDOW;
    
    bool is_created = CreateProcessA(
        nullptr, const_cast<char*>(args.c_str()),
        nullptr, nullptr, false, CREATE_NO_WINDOW, nullptr, nullptr, &si, &pi
    );

    if (!is_created) {
        std::stringstream ss;
        ss << "failed to create process: " << args;
        fatal(ss.str().c_str());
    }
    WaitForSingleObject(pi.hProcess, INFINITE);

    DWORD exit;
    GetExitCodeProcess(pi.hProcess, &exit);
    if (exit != 0) {
        std::stringstream ss;
        ss << "process \"" << args      << "\" exited with status code " << exit;
        fatal(ss.str().c_str(), exit);
    }

    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
}

int WinMain(HINSTANCE self, HINSTANCE prev, LPSTR cmdline, int showCmd) {
    run_process(cmdline);
}