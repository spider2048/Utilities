project('SilentExecute', 'cpp',
  version : '0.1',
  default_options : ['warning_level=3',
                     'cpp_std=c++20'])

exe = executable('Silent', 'silent.cpp',
  install : true,
  win_subsystem: 'windows')

test('basic', exe)
